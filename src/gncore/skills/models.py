"""Immutable data models for GNCore skills."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class SkillMetadata:
    skill_id: str
    name: str
    description: str
    version: str
    dependencies: tuple[str, ...] = field(default_factory=tuple)
    permissions: tuple[str, ...] = field(default_factory=tuple)
    category: str = "general"
    tags: tuple[str, ...] = field(default_factory=tuple)
    license: str = "MIT"


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
class SkillDomain:
    """A discoverable collection of related built-in workflows."""

    domain_id: str
    name: str
    description: str
    skill_ids: tuple[str, ...]
    workflow_ids: tuple[str, ...] = field(default_factory=tuple)
