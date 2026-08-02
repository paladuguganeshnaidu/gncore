"""High-level managers used by the CLI."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
import json
from pathlib import Path
from typing import Iterable, Sequence
from zipfile import ZIP_DEFLATED, ZipFile

from gncore.adapters.base import AdapterRegistry, ApplicationAdapter, get_adapter_registry
from gncore.config import GncoreConfig, GncoreConfigManager, default_config_root
from gncore.core.models import ApplicationDiscovery, ApplicationSummary, BackupArchive, InstallReport, SkillDefinition, ValidationIssue, ValidationReport
from gncore.skills.library import builtin_skills
from gncore.version import __version__


class SkillManager:
    def __init__(self, skills: Sequence[SkillDefinition] | None = None) -> None:
        self._skills = tuple(skills or builtin_skills())

    @property
    def skills(self) -> tuple[SkillDefinition, ...]:
        return self._skills

    def by_id(self, skill_id: str) -> SkillDefinition:
        for skill in self._skills:
            if skill.metadata.skill_id == skill_id:
                return skill
        raise KeyError(skill_id)

    def select(self, skill_ids: Iterable[str] | None = None) -> tuple[SkillDefinition, ...]:
        if skill_ids is None:
            return self.skills
        selected: list[SkillDefinition] = []
        for skill_id in skill_ids:
            selected.append(self.by_id(skill_id))
        return tuple(selected)


class AdapterManager:
    def __init__(self, registry: AdapterRegistry | None = None) -> None:
        self.registry = registry or get_adapter_registry()

    @property
    def adapters(self) -> tuple[ApplicationAdapter, ...]:
        return self.registry.adapters

    def discover(self, workspace_root: Path | None = None) -> tuple[ApplicationDiscovery, ...]:
        return self.registry.discover(workspace_root)

    def summaries(self, workspace_root: Path | None = None) -> tuple[ApplicationSummary, ...]:
        return self.registry.summaries(workspace_root)

    def by_key(self, key: str) -> ApplicationAdapter:
        return self.registry.by_key(key)

    def detected(self, workspace_root: Path | None = None) -> tuple[ApplicationAdapter, ...]:
        return tuple(adapter for adapter in self.adapters if adapter.discover(workspace_root).detected)


class ConfigurationManager:
    def __init__(self, root: Path | None = None) -> None:
        self._manager = GncoreConfigManager(root or default_config_root())

    def load(self) -> GncoreConfig:
        return self._manager.load()

    def save(self, config: GncoreConfig) -> None:
        self._manager.save(config)

    def update(self, *, applications: Sequence[str] | None = None, skills: Sequence[str] | None = None) -> GncoreConfig:
        config = self.load()
        if applications is not None:
            config.selected_applications = tuple(applications)
        if skills is not None:
            config.selected_skills = tuple(skills)
        self.save(config)
        return config


class Validator:
    def __init__(self, adapter_manager: AdapterManager | None = None) -> None:
        self.adapter_manager = adapter_manager or AdapterManager()

    def validate(self, application_keys: Sequence[str] | None = None, workspace_root: Path | None = None) -> tuple[ValidationReport, ...]:
        adapters = self._resolve_adapters(application_keys)
        return tuple(adapter.validate() for adapter in adapters)

    def _resolve_adapters(self, application_keys: Sequence[str] | None) -> tuple[ApplicationAdapter, ...]:
        if application_keys is None:
            return self.adapter_manager.adapters
        return tuple(self.adapter_manager.by_key(key) for key in application_keys)


class Installer:
    def __init__(self, adapter_manager: AdapterManager | None = None, skill_manager: SkillManager | None = None, configuration_manager: ConfigurationManager | None = None, validator: Validator | None = None) -> None:
        self.adapter_manager = adapter_manager or AdapterManager()
        self.skill_manager = skill_manager or SkillManager()
        self.configuration_manager = configuration_manager or ConfigurationManager()
        self.validator = validator or Validator(self.adapter_manager)

    def install(self, application_keys: Sequence[str], skill_ids: Sequence[str] | None = None, workspace_root: Path | None = None) -> tuple[InstallReport, ...]:
        skills = self.skill_manager.select(skill_ids)
        reports = tuple(self.adapter_manager.by_key(key).install(skills, workspace_root) for key in application_keys)
        self.configuration_manager.update(applications=application_keys, skills=tuple(skill.metadata.skill_id for skill in skills))
        return reports

    def uninstall(self, application_keys: Sequence[str], workspace_root: Path | None = None) -> None:
        for key in application_keys:
            self.adapter_manager.by_key(key).uninstall(workspace_root)

    def activate(self, application_keys: Sequence[str], workspace_root: Path | None = None, skill_ids: Sequence[str] | None = None) -> tuple[InstallReport, ...]:
        return self.install(application_keys, skill_ids=skill_ids, workspace_root=workspace_root)

    def update(self, application_keys: Sequence[str], workspace_root: Path | None = None, skill_ids: Sequence[str] | None = None) -> tuple[InstallReport, ...]:
        return self.install(application_keys, skill_ids=skill_ids, workspace_root=workspace_root)


class BackupManager:
    def __init__(self, adapter_manager: AdapterManager | None = None) -> None:
        self.adapter_manager = adapter_manager or AdapterManager()

    def create(self, output_path: Path | None = None, workspace_root: Path | None = None) -> BackupArchive:
        timestamp = datetime.now(UTC)
        archive_path = output_path or (default_config_root() / f"backup-{timestamp:%Y%m%d-%H%M%S}.zip")
        archive_path.parent.mkdir(parents=True, exist_ok=True)

        manifest: dict[str, object] = {"created_at": timestamp.isoformat(), "applications": []}
        with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
            for adapter in self.adapter_manager.adapters:
                discovery = adapter.discover(workspace_root)
                if not discovery.config_root.exists():
                    continue
                manifest["applications"].append({"key": adapter.key, "name": adapter.name, "root": str(discovery.config_root)})
                for path in discovery.config_root.rglob("*"):
                    if path.is_file():
                        archive.write(path, arcname=f"{adapter.key}/{path.relative_to(discovery.config_root).as_posix()}")
            archive.writestr("backup_manifest.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")

        return BackupArchive(path=archive_path, created_at=timestamp, applications=tuple(entry["key"] for entry in manifest["applications"]))


class RollbackManager:
    def __init__(self, adapter_manager: AdapterManager | None = None) -> None:
        self.adapter_manager = adapter_manager or AdapterManager()

    def restore(self, archive_path: Path, workspace_root: Path | None = None) -> None:
        with ZipFile(archive_path, "r") as archive:
            manifest = json.loads(archive.read("backup_manifest.json").decode("utf-8"))
            applications = {entry["key"]: Path(entry["root"]) for entry in manifest.get("applications", [])}
            for adapter in self.adapter_manager.adapters:
                root = applications.get(adapter.key)
                if root is None:
                    continue
                root.mkdir(parents=True, exist_ok=True)
                prefix = f"{adapter.key}/"
                for member in archive.namelist():
                    if not member.startswith(prefix) or member.endswith("/") or member == "backup_manifest.json":
                        continue
                    relative = Path(member[len(prefix):])
                    if any(part == ".." for part in relative.parts):
                        continue
                    target = root / relative
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with archive.open(member) as source, target.open("wb") as destination:
                        destination.write(source.read())


class DiagnosticsManager:
    def __init__(self, adapter_manager: AdapterManager | None = None, validator: Validator | None = None) -> None:
        self.adapter_manager = adapter_manager or AdapterManager()
        self.validator = validator or Validator(self.adapter_manager)

    def report(self, workspace_root: Path | None = None) -> dict[str, object]:
        summaries = self.adapter_manager.summaries(workspace_root)
        validations = self.validator.validate(workspace_root=workspace_root)
        return {
            "applications": [
                {
                    "key": summary.key,
                    "name": summary.name,
                    "detected": summary.detected,
                    "writable": summary.writable,
                    "config_root": str(summary.config_root),
                    "features": list(summary.features),
                }
                for summary in summaries
            ],
            "validation": [
                {
                    "application": report.application,
                    "valid": report.valid,
                    "issues": [
                        {"severity": issue.severity, "message": issue.message, "path": str(issue.path) if issue.path else None}
                        for issue in report.issues
                    ],
                }
                for report in validations
            ],
        }


class VersionManager:
    def show(self) -> str:
        return __version__
