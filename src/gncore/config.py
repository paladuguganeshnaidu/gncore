"""Project configuration handling for GNCore."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import json
from typing import Any

from gncore.providers.catalog import ProviderInfo, ProviderKind, discover_providers, resolve_provider
from gncore.state.models import utc_now_iso


class ConfigError(RuntimeError):
    """Raised when a project configuration file is missing or invalid."""


@dataclass(slots=True)
class GncoreConfig:
    """Persisted configuration stored in .gncore/config.json."""

    project_name: str
    selected_provider: str
    available_providers: list[str] = field(default_factory=list)
    provider_kind: str = "unknown"
    initialized_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    version: str = "1.0.0"

    def to_dict(self) -> dict[str, Any]:
        """Serialize the config to JSON-compatible data."""
        return {
            "project_name": self.project_name,
            "provider": self.selected_provider,
            "selected_provider": self.selected_provider,
            "available_providers": self.available_providers,
            "provider_kind": self.provider_kind,
            "initialized_at": self.initialized_at,
            "updated_at": self.updated_at,
            "version": self.version,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "GncoreConfig":
        """Deserialize config from JSON-compatible data."""
        selected_provider = str(data.get("selected_provider", data.get("provider", "mock")))
        available = [str(item) for item in data.get("available_providers", [])]
        return cls(
            project_name=str(data.get("project_name", "")),
            selected_provider=selected_provider,
            available_providers=available,
            provider_kind=str(data.get("provider_kind", "unknown")),
            initialized_at=str(data.get("initialized_at", utc_now_iso())),
            updated_at=str(data.get("updated_at", utc_now_iso())),
            version=str(data.get("version", "1.0.0")),
        )

    def save(self, config_file: Path) -> None:
        """Persist config to disk."""
        self.updated_at = utc_now_iso()
        config_file.parent.mkdir(parents=True, exist_ok=True)
        config_file.write_text(json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, config_file: Path) -> "GncoreConfig":
        """Load config from disk and validate it."""
        if not config_file.is_file():
            raise ConfigError(f"Missing project config: {config_file}")
        try:
            data = json.loads(config_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ConfigError(f"Invalid JSON in {config_file}: {exc}") from exc
        config = cls.from_dict(data)
        config.validate()
        return config

    def validate(self) -> None:
        """Validate the config fields and provider selection."""
        if not self.project_name.strip():
            raise ConfigError("project_name is required")
        if not self.selected_provider.strip():
            raise ConfigError("selected_provider is required")
        if self.available_providers and self.selected_provider not in self.available_providers:
            raise ConfigError(
                f"Selected provider '{self.selected_provider}' is not in the discovered provider list"
            )

    @classmethod
    def detect(cls, project_name: str) -> "GncoreConfig":
        """Create a config using the best available provider."""
        providers = discover_providers()
        chosen = resolve_provider(providers)
        return cls(
            project_name=project_name,
            selected_provider=chosen.name,
            available_providers=[provider.name for provider in providers if provider.available],
            provider_kind=chosen.kind.value,
        )

    def update_provider(self, provider_info: ProviderInfo) -> None:
        """Update the chosen provider and record its category."""
        self.selected_provider = provider_info.name
        self.provider_kind = provider_info.kind.value
        if provider_info.name not in self.available_providers:
            self.available_providers.append(provider_info.name)
