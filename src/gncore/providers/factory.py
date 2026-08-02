"""Provider factory for configured GNCore provider adapters."""

from __future__ import annotations

from .base import Provider
from .external import ClaudeCodeProvider, CodexProvider, GeminiCLIProvider, OpenCodeProvider
from .mock import MockProvider


class ProviderFactory:
    """Create provider adapters without coupling callers to implementations."""

    def create(self, provider_name: str) -> Provider:
        """Return a provider adapter for a configured provider name."""
        normalized = provider_name.strip().lower()
        providers: dict[str, Provider] = {
            "mock": MockProvider(),
            "codex": CodexProvider(),
            "claude": ClaudeCodeProvider(),
            "claude-code": ClaudeCodeProvider(),
            "gemini": GeminiCLIProvider(),
            "gemini-cli": GeminiCLIProvider(),
            "opencode": OpenCodeProvider(),
        }
        try:
            return providers[normalized]
        except KeyError as exc:
            raise ValueError(f"Unsupported provider: {provider_name}") from exc
