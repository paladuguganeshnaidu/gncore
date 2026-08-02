"""Typed data models used by the installer core."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


def utc_now() -> datetime:
    return datetime.now(UTC)


@dataclass(frozen=True, slots=True)
class SkillMetadata:
    skill_id: str
    name: str
    description: str
    version: str
    dependencies: tuple[str, ...] = field(default_factory=tuple)
    permissions: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class SkillExample:
    title: str
    instruction: str
    output: str


@dataclass(frozen=True, slots=True)
class SkillCommand:
    name: str
    description: str
    body: str


@dataclass(frozen=True, slots=True)
class SkillDefinition:
    metadata: SkillMetadata
    prompt: str
    examples: tuple[SkillExample, ...] = field(default_factory=tuple)
    commands: tuple[SkillCommand, ...] = field(default_factory=tuple)
    configuration: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "metadata": asdict(self.metadata),
            "prompt": self.prompt,
            "examples": [asdict(example) for example in self.examples],
            "commands": [asdict(command) for command in self.commands],
            "configuration": self.configuration,
        }


@dataclass(frozen=True, slots=True)
class ApplicationSummary:
    key: str
    name: str
    detected: bool
    writable: bool
    config_root: Path
    features: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ApplicationDiscovery:
    key: str
    name: str
    detected: bool
    executable_found: bool
    config_root: Path
    notes: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class InstalledSkill:
    skill_id: str
    version: str
    files: tuple[Path, ...]


@dataclass(frozen=True, slots=True)
class InstalledApplication:
    key: str
    name: str
    config_root: Path
    manifest_path: Path
    skills: tuple[InstalledSkill, ...]


@dataclass(frozen=True, slots=True)
class InstallReport:
    application: str
    installed: tuple[str, ...]
    skipped: tuple[str, ...]
    verified: bool
    details: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    severity: str
    message: str
    path: Path | None = None


@dataclass(frozen=True, slots=True)
class ValidationReport:
    application: str
    valid: bool
    issues: tuple[ValidationIssue, ...]


@dataclass(frozen=True, slots=True)
class BackupArchive:
    path: Path
    created_at: datetime
    applications: tuple[str, ...]
