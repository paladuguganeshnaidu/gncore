"""Test provider implementation that records deterministic responses."""

from __future__ import annotations

from typing import Iterator

from .base import Provider, ProviderHealth, ProviderResponse, ProviderStatus


class MockProvider(Provider):
    """Provider used by tests and local dry runs."""

    @property
    def name(self) -> str:
        """Return the stable provider name."""
        return "mock"

    def run(self, prompt: str) -> ProviderResponse:
        """Return a deterministic response containing prompt metadata."""
        return ProviderResponse(
            content=f"Mock response generated for prompt with {len(prompt)} characters.\n",
            provider_name=self.name,
            metadata={"prompt_length": str(len(prompt)), "tokens": str(len(prompt.split()))},
        )

    def stream(self, prompt: str) -> Iterator[str]:
        """Yield the deterministic mock response as one chunk."""
        yield self.run(prompt).content

    def health(self) -> ProviderStatus:
        """Report that the mock provider is always available."""
        return ProviderStatus(self.name, ProviderHealth.AVAILABLE, "Mock provider is available")

    def cancel(self) -> None:
        """Cancel mock execution, which is a no-op because it is synchronous."""
