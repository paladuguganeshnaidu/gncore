"""High-level GNCore command orchestration."""

from __future__ import annotations

from dataclasses import dataclass
import importlib
from pathlib import Path
import shutil
import subprocess
import sys

from gncore.config import ConfigError, GncoreConfig
from gncore.core.executor import ExecutionEngine, ExecutionResult
from gncore.core.prompt import PromptBuilder
from gncore.core.stages import StageRegistry, default_stage_registry
from gncore.providers.catalog import ProviderInfo, discover_providers, provider_by_name, resolve_provider
from gncore.providers.credentials import CredentialStore
from gncore.providers.factory import ProviderFactory
from gncore.skills.loader import SkillLoader
from gncore.state.manager import ProjectStateManager
from gncore.state.models import ProjectState
from gncore.utils.logging import LoggerFactory


class ProjectValidationError(RuntimeError):
    """Raised when a project fails validation before execution."""


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    """A single actionable project validation result."""

    field: str
    message: str
    ok: bool = False


class GncoreRuntime:
    """Reusable command surface for the GNCore CLI."""

    def __init__(self, registry: StageRegistry | None = None) -> None:
        self.registry = registry or default_stage_registry()
        self.provider_factory = ProviderFactory()
        self.credentials = CredentialStore()
        self.logger_factory = LoggerFactory()

    def manager(self, project_dir: Path) -> ProjectStateManager:
        return ProjectStateManager(project_dir)

    def config_file(self, project_dir: Path) -> Path:
        return self.manager(project_dir).gncore_dir / "config.json"

    def load_config(self, project_dir: Path) -> GncoreConfig:
        return GncoreConfig.load(self.config_file(project_dir))

    def init(self, project_dir: Path, project_name: str | None = None, provider: str | None = None) -> GncoreConfig:
        project_name = project_name or project_dir.name
        manager = self.manager(project_dir)
        manager.initialize(project_name, provider or "mock")
        config = GncoreConfig.detect(project_name) if provider is None else GncoreConfig(
            project_name=project_name,
            selected_provider=provider,
            available_providers=[info.name for info in discover_providers() if info.available],
            provider_kind=provider_by_name(provider).kind.value,
        )
        config.save(self.config_file(project_dir))
        prompt_path = manager.prompt_file
        if not prompt_path.exists():
            prompt_path.write_text(f"# {project_name} Requirements\n", encoding="utf-8")
        self.logger_factory.create(manager.gncore_dir / "logs").info("Initialized GNCore project '%s'", project_name)
        return config

    def doctor(self, project_dir: Path) -> list[ValidationIssue]:
        return self.validate_project(project_dir)

    def provider_list(self) -> list[ProviderInfo]:
        return discover_providers()

    def provider_select(self, project_dir: Path, name: str) -> GncoreConfig:
        config = self.load_config(project_dir)
        info = provider_by_name(name)
        config.update_provider(info)
        config.save(self.config_file(project_dir))
        return config

    def provider_detect(self, project_dir: Path) -> GncoreConfig:
        config = self.load_config(project_dir)
        chosen = resolve_provider(discover_providers())
        config.update_provider(chosen)
        config.available_providers = [provider.name for provider in discover_providers() if provider.available]
        config.save(self.config_file(project_dir))
        return config

    def config_show(self, project_dir: Path) -> GncoreConfig:
        return self.load_config(project_dir)

    def config_validate(self, project_dir: Path) -> list[ValidationIssue]:
        return self.validate_project(project_dir)

    def auth_set(self, provider_name: str, token: str) -> None:
        self.credentials.save(provider_name, token)

    def auth_get(self, provider_name: str) -> str | None:
        return self.credentials.get(provider_name)

    def auth_delete(self, provider_name: str) -> None:
        self.credentials.delete(provider_name)

    def version(self) -> str:
        return getattr(importlib.import_module("gncore"), "__version__", "1.0.0")

    def update(self, dry_run: bool = False) -> subprocess.CompletedProcess[str] | None:
        command = [sys.executable, "-m", "pip", "install", "--upgrade", "gncore"]
        if dry_run:
            return None
        return subprocess.run(command, check=True, text=True, capture_output=True)

    def run(self, project_dir: Path) -> list[ExecutionResult]:
        self._prepare_for_run(project_dir)
        config = self.load_config(project_dir)
        manager = self.manager(project_dir)
        provider_info = self._provider_for_run(project_dir, config)
        provider = provider_info.create()
        engine = ExecutionEngine(self.registry, manager, SkillLoader(), PromptBuilder(), provider)
        state = manager.load()
        results: list[ExecutionResult] = []
        for stage in self._remaining_stages(state):
            result = engine.execute(stage.id)
            results.append(result)
            state = manager.load()
        return results

    def resume(self, project_dir: Path) -> list[ExecutionResult]:
        return self.run(project_dir)

    def _prepare_for_run(self, project_dir: Path) -> None:
        issues = self.validate_project(project_dir, strict_provider=False)
        if issues:
            messages = "\n".join(f"- {issue.field}: {issue.message}" for issue in issues)
            raise ProjectValidationError(f"Project validation failed:\n{messages}")

    def _remaining_stages(self, state: ProjectState) -> list:
        completed = set(state.completed_stages)
        if state.current_stage is not None:
            start = state.current_stage
        else:
            incomplete = [stage.id for stage in self.registry.all() if stage.id not in completed]
            start = incomplete[0] if incomplete else None
        if start is None:
            return []
        stages = list(self.registry.all())
        try:
            index = next(i for i, stage in enumerate(stages) if stage.id == start)
        except StopIteration:
            return []
        return [stage for stage in stages[index:] if stage.id not in completed]

    def write_config(self, project_dir: Path, config: GncoreConfig) -> None:
        config.save(self.config_file(project_dir))

    def selected_provider_status(self, project_dir: Path) -> tuple[str, str]:
        config = self.load_config(project_dir)
        provider = provider_by_name(config.selected_provider)
        status = provider.create().health()
        return status.health.value, status.message

    def _provider_for_run(self, project_dir: Path, config: GncoreConfig) -> ProviderInfo:
        provider = provider_by_name(config.selected_provider)
        status = provider.create().health()
        if status.health.value == "available":
            return provider
        providers = discover_providers()
        fallback = resolve_provider(providers)
        if fallback.name == provider.name:
            return provider
        config.update_provider(fallback)
        config.available_providers = [item.name for item in providers if item.available]
        config.save(self.config_file(project_dir))
        return fallback

    def validate_project(self, project_dir: Path, strict_provider: bool = True) -> list[ValidationIssue]:
        issues: list[ValidationIssue] = []
        manager = self.manager(project_dir)
        if not manager.gncore_dir.exists():
            issues.append(ValidationIssue("project", "Project is not initialized. Run `gncore init` first."))
            return issues
        if not manager.prompt_file.exists():
            issues.append(ValidationIssue("prompt.md", "prompt.md is missing. Re-run `gncore init` or create it manually."))
        try:
            config = self.load_config(project_dir)
        except ConfigError as exc:
            issues.append(ValidationIssue("config", str(exc)))
        else:
            try:
                provider_info = provider_by_name(config.selected_provider)
            except ValueError as exc:
                issues.append(ValidationIssue("provider", str(exc)))
            else:
                status = provider_info.create().health()
                if strict_provider and status.health.value != "available":
                    issues.append(ValidationIssue("provider", status.message))
        if shutil.which("git") is None:
            issues.append(ValidationIssue("git", "Git is not installed or not on PATH."))
        try:
            __import__("keyring")
        except Exception:
            issues.append(ValidationIssue("keyring", "keyring is unavailable; secure credential storage will not work."))
        return issues
