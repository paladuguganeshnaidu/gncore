"""Base adapter interfaces and shared file-system installation logic."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
import re
import shutil
from typing import Iterable, Sequence

from gncore.core.models import ApplicationDiscovery, ApplicationSummary, InstallReport, InstalledSkill, SkillDefinition, ValidationIssue, ValidationReport
from gncore.skills.library import builtin_skills
from gncore.utilities.io import atomic_write_text, read_json, write_json


@dataclass(frozen=True, slots=True)
class AdapterTemplate:
    key: str
    name: str
    config_roots: tuple[Path, ...]
    executable_names: tuple[str, ...] = field(default_factory=tuple)
    supports_prompts: bool = True
    supports_commands: bool = True
    supports_mcp: bool = True
    supports_permissions: bool = True
    supports_settings: bool = True


class ApplicationAdapter:
    """Abstract adapter that can detect, install, uninstall, and validate a target application."""

    template: AdapterTemplate

    def __init__(self, template: AdapterTemplate) -> None:
        self.template = template

    @property
    def key(self) -> str:
        return self.template.key

    @property
    def name(self) -> str:
        return self.template.name

    def discover(self, workspace_root: Path | None = None) -> ApplicationDiscovery:
        config_root = self.resolve_config_root(workspace_root)
        executable_found = any(shutil.which(name) for name in self.template.executable_names)
        detected = config_root.exists() or executable_found
        notes = []
        if config_root.exists():
            notes.append("config-root-found")
        if executable_found:
            notes.append("executable-found")
        return ApplicationDiscovery(
            key=self.key,
            name=self.name,
            detected=detected,
            executable_found=executable_found,
            config_root=config_root,
            notes=tuple(notes),
        )

    def summary(self, workspace_root: Path | None = None) -> ApplicationSummary:
        discovery = self.discover(workspace_root)
        writable = self.ensure_writable(discovery.config_root)
        return ApplicationSummary(
            key=self.key,
            name=self.name,
            detected=discovery.detected,
            writable=writable,
            config_root=discovery.config_root,
            features=self.feature_flags(),
        )

    def feature_flags(self) -> tuple[str, ...]:
        features = ["skills"]
        if self.template.supports_prompts:
            features.append("prompts")
        if self.template.supports_commands:
            features.append("commands")
        if self.template.supports_mcp:
            features.append("mcp")
        if self.template.supports_permissions:
            features.append("permissions")
        if self.template.supports_settings:
            features.append("settings")
        return tuple(features)

    def resolve_config_root(self, workspace_root: Path | None = None) -> Path:
        for candidate in self.template.config_roots:
            if candidate.exists():
                return candidate.resolve()
        return self.template.config_roots[0].resolve()

    def ensure_writable(self, path: Path) -> bool:
        try:
            path.mkdir(parents=True, exist_ok=True)
            probe = path / ".gncore-write-test"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink(missing_ok=True)
            return True
        except OSError:
            return False

    def install(self, skills: Sequence[SkillDefinition] | None = None, workspace_root: Path | None = None, scope: str = "user") -> InstallReport:
        selected_skills = tuple(skills or builtin_skills())
        root = self.resolve_config_root(workspace_root)
        root.mkdir(parents=True, exist_ok=True)

        manifest_path = root / "manifest.json"
        bundle_root = root / "gncore"
        bundle_root.mkdir(parents=True, exist_ok=True)

        installed: list[str] = []
        skipped: list[str] = []
        installed_records: list[InstalledSkill] = []

        for skill in selected_skills:
            skill_root = bundle_root / "skills" / skill.metadata.skill_id
            skill_root.mkdir(parents=True, exist_ok=True)
            self._write_skill(skill_root, skill)
            installed.append(skill.metadata.skill_id)
            installed_records.append(
                InstalledSkill(
                    skill_id=skill.metadata.skill_id,
                    version=skill.metadata.version,
                    files=tuple(sorted(path for path in skill_root.rglob("*") if path.is_file())),
                )
            )

        self._write_manifest(manifest_path, root, installed_records)
        self._write_bootstrap_files(bundle_root, selected_skills)

        report = self.validate(root)
        return InstallReport(
            application=self.name,
            installed=tuple(installed),
            skipped=tuple(skipped),
            verified=report.valid,
            details=tuple(issue.message for issue in report.issues),
        )

    def uninstall(self, workspace_root: Path | None = None, scope: str = "user") -> None:
        root = self.resolve_config_root(workspace_root)
        bundle_root = root / "gncore"
        manifest_path = root / "manifest.json"
        if bundle_root.exists():
            shutil.rmtree(bundle_root)
        if manifest_path.exists():
            manifest_path.unlink()

    def validate(self, root: Path | None = None, scope: str = "user", workspace_root: Path | None = None) -> ValidationReport:
        root = root or self.resolve_config_root(None)
        manifest_path = root / "manifest.json"
        issues: list[ValidationIssue] = []

        if not manifest_path.exists():
            issues.append(ValidationIssue("error", "manifest file is missing", manifest_path))
            return ValidationReport(application=self.name, valid=False, issues=tuple(issues))

        manifest = read_json(manifest_path)
        for skill_entry in manifest.get("skills", []):
            skill_root = root / "gncore" / "skills" / skill_entry["skill_id"]
            if not skill_root.exists():
                issues.append(ValidationIssue("error", f"skill directory is missing for {skill_entry['skill_id']}", skill_root))
            for relative_path in skill_entry.get("files", []):
                file_path = root / relative_path
                if not file_path.exists():
                    issues.append(ValidationIssue("error", f"expected file is missing: {relative_path}", file_path))

        return ValidationReport(application=self.name, valid=not issues, issues=tuple(issues))

    def _write_skill(self, skill_root: Path, skill: SkillDefinition) -> None:
        write_json(skill_root / "metadata.json", asdict(skill.metadata))
        atomic_write_text(skill_root / "prompt.md", skill.prompt + "\n")
        write_json(skill_root / "configuration.json", skill.configuration)
        write_json(skill_root / "examples.json", [asdict(example) for example in skill.examples])
        write_json(skill_root / "commands.json", [asdict(command) for command in skill.commands])
        write_json(skill_root / "permissions.json", list(skill.metadata.permissions))

        if self.template.supports_prompts:
            prompts_root = skill_root.parent.parent / "prompts"
            prompts_root.mkdir(parents=True, exist_ok=True)
            atomic_write_text(prompts_root / f"{skill.metadata.skill_id}.md", skill.prompt + "\n")

        if self.template.supports_commands:
            commands_root = skill_root.parent.parent / "commands" / skill.metadata.skill_id
            commands_root.mkdir(parents=True, exist_ok=True)
            for command in skill.commands:
                atomic_write_text(commands_root / f"{command.name}.md", command.body + "\n")

    def _write_manifest(self, manifest_path: Path, root: Path, skills: Sequence[InstalledSkill]) -> None:
        manifest = {
            "application": self.name,
            "key": self.key,
            "config_root": str(root),
            "skills": [
                {
                    "skill_id": skill.skill_id,
                    "version": skill.version,
                    "files": [str(file_path.relative_to(root)) for file_path in skill.files],
                }
                for skill in skills
            ],
        }
        write_json(manifest_path, manifest)

    def _write_bootstrap_files(self, bundle_root: Path, skills: Sequence[SkillDefinition]) -> None:
        write_json(
            bundle_root / "bundle.json",
            {
                "application": self.name,
                "features": self.feature_flags(),
                "skills": [skill.metadata.skill_id for skill in skills],
            },
        )
        if self.template.supports_settings:
            write_json(
                bundle_root / "settings.json",
                {
                    "application": self.name,
                    "managed_by": "gncore",
                    "skill_count": len(skills),
                },
            )
        if self.template.supports_mcp:
            write_json(
                bundle_root / "mcp.json",
                {
                    "servers": [
                        {
                            "name": "gncore",
                            "command": "gncore",
                            "args": ["activate"],
                        }
                    ]
                },
            )


class NativeSkillAdapter(ApplicationAdapter):
    """Install skills in the standard SKILL.md folder layout used by agent clients."""

    workspace_relative_dir: Path
    user_relative_dir: Path

    def __init__(self, template: AdapterTemplate, workspace_relative_dir: Path, user_relative_dir: Path) -> None:
        super().__init__(template)
        self.workspace_relative_dir = workspace_relative_dir
        self.user_relative_dir = user_relative_dir

    def skill_root(self, workspace_root: Path | None = None, scope: str = "user") -> Path:
        if scope not in {"workspace", "user"}:
            raise ValueError("scope must be 'workspace' or 'user'")
        if scope == "workspace":
            if workspace_root is None:
                raise ValueError("workspace scope requires a workspace root")
            return (workspace_root / self.workspace_relative_dir).resolve()
        return (Path.home() / self.user_relative_dir).resolve()

    def manifest_path(self, skill_root: Path) -> Path:
        return skill_root.parent / ".gncore" / f"{self.key}-skills.json"

    def _is_managed(self, marker: Path, skill_id: str) -> bool:
        if not marker.is_file():
            return False
        try:
            data = read_json(marker)
        except (OSError, ValueError):
            return False
        if not isinstance(data, dict):
            return False
        return data.get("managed_by") == "gncore" and data.get("skill_id") == skill_id

    def install(self, skills: Sequence[SkillDefinition] | None = None, workspace_root: Path | None = None, scope: str = "user") -> InstallReport:
        selected = tuple(skills or builtin_skills())
        root = self.skill_root(workspace_root, scope)
        root.mkdir(parents=True, exist_ok=True)
        manifest_path = self.manifest_path(root)
        installed: list[str] = []
        skipped: list[str] = []
        details: list[str] = []
        records: list[dict[str, str]] = []

        for skill in selected:
            skill_id = skill.metadata.skill_id
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
                raise ValueError(f"invalid skill id: {skill_id}")
            skill_dir = root / skill_id
            marker = skill_dir / ".gncore-managed.json"
            if skill_dir.exists() and not self._is_managed(marker, skill_id):
                skipped.append(skill_id)
                details.append(f"Skipped {skill_id}: {skill_dir} already exists and is not GNCore-managed")
                continue
            skill_dir.mkdir(parents=True, exist_ok=True)
            frontmatter = "---\n" + f"name: {skill_id}\n" + f"description: {json.dumps(skill.metadata.description, ensure_ascii=False)}\n" + "---\n\n"
            atomic_write_text(skill_dir / "SKILL.md", frontmatter + skill.prompt.strip() + "\n")
            old_marker = read_json(marker) if marker.is_file() else {}
            owners = set(old_marker.get("managed_apps", []))
            if old_marker.get("managed_by") == "gncore" and isinstance(old_marker.get("application"), str):
                owners.add(old_marker["application"])
            owners.add(self.key)
            write_json(marker, {"managed_by": "gncore", "application": self.key, "managed_apps": sorted(owners), "skill_id": skill_id, "version": skill.metadata.version})
            installed.append(skill_id)
            records.append({"skill_id": skill_id, "version": skill.metadata.version})

        # Preserve other GNCore-managed skills already installed in this target.
        previous = read_json(manifest_path) if manifest_path.exists() else {}
        by_id = {
            entry["skill_id"]: entry
            for entry in previous.get("skills", [])
            if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry.get("skill_id", ""))
            and self._is_managed(root / entry["skill_id"] / ".gncore-managed.json", entry["skill_id"])
        }
        by_id.update({entry["skill_id"]: entry for entry in records})
        write_json(manifest_path, {"application": self.key, "scope": scope, "skills": list(by_id.values())})

        report = self.validate(root, scope=scope)
        return InstallReport(self.name, tuple(installed), tuple(skipped), report.valid, tuple(details + [issue.message for issue in report.issues]))

    def uninstall(self, workspace_root: Path | None = None, scope: str = "user") -> None:
        root = self.skill_root(workspace_root, scope)
        manifest_path = self.manifest_path(root)
        if not manifest_path.is_file():
            return
        manifest = read_json(manifest_path)
        for entry in manifest.get("skills", []):
            skill_id = entry.get("skill_id", "")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
                continue
            skill_dir = root / skill_id
            marker = skill_dir / ".gncore-managed.json"
            if self._is_managed(marker, skill_id):
                marker_data = read_json(marker)
                owners = set(marker_data.get("managed_apps", []))
                if not owners:
                    owners.add(marker_data.get("application", self.key))
                owners.discard(self.key)
                if owners:
                    marker_data["managed_apps"] = sorted(owners)
                    marker_data["application"] = sorted(owners)[0]
                    write_json(marker, marker_data)
                else:
                    (skill_dir / "SKILL.md").unlink(missing_ok=True)
                    marker.unlink(missing_ok=True)
                    for child in sorted(skill_dir.rglob("*"), reverse=True):
                        if child.is_dir():
                            try:
                                child.rmdir()
                            except OSError:
                                pass
                    try:
                        skill_dir.rmdir()
                    except OSError:
                        pass
        manifest_path.unlink(missing_ok=True)

    def validate(self, root: Path | None = None, scope: str = "user", workspace_root: Path | None = None) -> ValidationReport:
        skill_root = root or self.skill_root(workspace_root, scope)
        manifest_path = self.manifest_path(skill_root)
        issues: list[ValidationIssue] = []
        if not manifest_path.is_file():
            issues.append(ValidationIssue("error", "GNCore skills manifest is missing", manifest_path))
            return ValidationReport(self.name, False, tuple(issues))
        manifest = read_json(manifest_path)
        for entry in manifest.get("skills", []):
            skill_id = entry.get("skill_id", "")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
                issues.append(ValidationIssue("error", f"invalid skill id in manifest: {skill_id}", manifest_path))
                continue
            skill_dir = skill_root / skill_id
            if not (skill_dir / "SKILL.md").is_file():
                issues.append(ValidationIssue("error", f"SKILL.md is missing for {skill_id}", skill_dir / "SKILL.md"))
            if not self._is_managed(skill_dir / ".gncore-managed.json", skill_id):
                issues.append(ValidationIssue("error", f"GNCore ownership marker is missing for {skill_id}", skill_dir))
        return ValidationReport(self.name, not issues, tuple(issues))


class AdapterRegistry:
    """Container for all supported adapters."""

    def __init__(self, adapters: Iterable[ApplicationAdapter]) -> None:
        self._adapters = tuple(adapters)

    @property
    def adapters(self) -> tuple[ApplicationAdapter, ...]:
        return self._adapters

    def by_key(self, key: str) -> ApplicationAdapter:
        for adapter in self._adapters:
            if adapter.key == key:
                return adapter
        raise KeyError(key)

    def discover(self, workspace_root: Path | None = None) -> tuple[ApplicationDiscovery, ...]:
        return tuple(adapter.discover(workspace_root) for adapter in self._adapters)

    def summaries(self, workspace_root: Path | None = None) -> tuple[ApplicationSummary, ...]:
        return tuple(adapter.summary(workspace_root) for adapter in self._adapters)


_REGISTRY: AdapterRegistry | None = None


def get_adapter_registry() -> AdapterRegistry:
    global _REGISTRY
    if _REGISTRY is None:
        from gncore.adapters.builtin import builtin_adapters

        _REGISTRY = AdapterRegistry(builtin_adapters())
    return _REGISTRY
