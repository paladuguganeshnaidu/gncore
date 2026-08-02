"""GNCore public API."""

from __future__ import annotations

from gncore.adapters import AdapterRegistry, ApplicationAdapter, builtin_adapters, get_adapter_registry
from gncore.cli.app import GncoreCli, main
from gncore.config import GncoreConfig, GncoreConfigManager, default_config_root, platform_config_dir
from gncore.core.managers import AdapterManager, BackupManager, ConfigurationManager, DiagnosticsManager, Installer, RollbackManager, SkillManager, Validator, VersionManager
from gncore.core.models import ApplicationDiscovery, ApplicationSummary, BackupArchive, InstallReport, InstalledApplication, InstalledSkill, SkillCommand, SkillDefinition, SkillExample, SkillMetadata, ValidationIssue, ValidationReport
from gncore.version import __version__

__all__ = [
    "__version__",
    "AdapterManager",
    "AdapterRegistry",
    "ApplicationAdapter",
    "ApplicationDiscovery",
    "ApplicationSummary",
    "BackupArchive",
    "BackupManager",
    "ConfigurationManager",
    "DiagnosticsManager",
    "GncoreCli",
    "GncoreConfig",
    "GncoreConfigManager",
    "InstallReport",
    "InstalledApplication",
    "InstalledSkill",
    "Installer",
    "RollbackManager",
    "SkillCommand",
    "SkillDefinition",
    "SkillExample",
    "SkillManager",
    "SkillMetadata",
    "ValidationIssue",
    "ValidationReport",
    "Validator",
    "VersionManager",
    "builtin_adapters",
    "default_config_root",
    "get_adapter_registry",
    "main",
    "platform_config_dir",
]
