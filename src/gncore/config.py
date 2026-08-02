"""Configuration and platform path helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
import json
import os
from pathlib import Path
import sys
from typing import Any

from gncore.version import __version__


def utc_now() -> datetime:
    return datetime.now(UTC)


def default_config_root() -> Path:
    override = os.environ.get("GNCORE_HOME")
    if override:
        return Path(override).expanduser().resolve()

    if sys.platform == "win32":
        base = os.environ.get("APPDATA") or os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Roaming")
        return Path(base).expanduser().resolve() / "gncore"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "gncore"

    xdg = os.environ.get("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg).expanduser().resolve() / "gncore"
    return Path.home() / ".config" / "gncore"


def platform_config_dir(*parts: str) -> Path:
    if sys.platform == "win32":
        base = os.environ.get("APPDATA") or os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Roaming")
        return Path(base).expanduser().resolve().joinpath(*parts)
    if sys.platform == "darwin":
        return (Path.home() / "Library" / "Application Support").joinpath(*parts)
    xdg = os.environ.get("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg).expanduser().resolve().joinpath(*parts)
    return (Path.home() / ".config").joinpath(*parts)


@dataclass(slots=True)
class GncoreConfig:
    """Persisted GNCore configuration."""

    version: str = __version__
    selected_applications: tuple[str, ...] = field(default_factory=tuple)
    selected_skills: tuple[str, ...] = field(default_factory=tuple)
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "version": self.version,
            "selected_applications": list(self.selected_applications),
            "selected_skills": list(self.selected_skills),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GncoreConfig":
        return cls(
            version=str(data.get("version", __version__)),
            selected_applications=tuple(str(value) for value in data.get("selected_applications", [])),
            selected_skills=tuple(str(value) for value in data.get("selected_skills", [])),
            created_at=datetime.fromisoformat(str(data.get("created_at", utc_now().isoformat()))),
            updated_at=datetime.fromisoformat(str(data.get("updated_at", utc_now().isoformat()))),
        )


class GncoreConfigManager:
    """Load and store the global GNCore configuration file."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = (root or default_config_root()).expanduser().resolve()
        self.config_file = self.root / "config.json"

    def load(self) -> GncoreConfig:
        if not self.config_file.exists():
            return GncoreConfig()
        return GncoreConfig.from_dict(json.loads(self.config_file.read_text(encoding="utf-8")))

    def save(self, config: GncoreConfig) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        config.updated_at = utc_now()
        self.config_file.write_text(json.dumps(config.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def reset(self) -> GncoreConfig:
        config = GncoreConfig()
        self.save(config)
        return config
