"""Provider factory for configured GNCore provider adapters."""

from __future__ import annotations

from .base import Provider
from .catalog import provider_by_name


class ProviderFactory:
    """Create provider adapters without coupling callers to implementations."""

    def create(self, provider_name: str) -> Provider:
        """Return a provider adapter for a configured provider name."""
        try:
            return provider_by_name(provider_name).create()
        except ValueError as exc:
            raise ValueError(f"Unsupported provider: {provider_name}") from exc
