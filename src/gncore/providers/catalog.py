"""Provider discovery and selection for GNCore."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from shutil import which
from typing import Callable

from .api import AnthropicProvider, GeminiAPIProvider, OllamaProvider, OpenAIProvider, OpenRouterProvider
from .base import Provider, ProviderHealth
from .copilot import GitHubCopilotAgentProvider
from .external import ClaudeCodeProvider, CodexProvider, GeminiCLIProvider, OpenCodeProvider
from .mock import MockProvider


class ProviderKind(str, Enum):
    """Provider categories."""

    AGENT = "agent"
    API = "api"
    TEST = "test"


@dataclass(frozen=True, slots=True)
class ProviderInfo:
    """Discovered provider metadata."""

    name: str
    kind: ProviderKind
    available: bool
    description: str
    factory: Callable[[], Provider]
    aliases: tuple[str, ...] = ()

    def create(self) -> Provider:
        return self.factory()


def _agent_available(executable: str) -> bool:
    return which(executable) is not None


def discover_providers() -> list[ProviderInfo]:
    """Return known providers ordered by preferred default priority."""
    providers = [
        ProviderInfo("github-copilot-agent", ProviderKind.AGENT, _agent_available("gh"), "GitHub Copilot CLI", GitHubCopilotAgentProvider, ("copilot", "gh-copilot")),
        ProviderInfo("codex", ProviderKind.AGENT, _agent_available("codex"), "OpenAI Codex CLI", CodexProvider),
        ProviderInfo("claude-code", ProviderKind.AGENT, _agent_available("claude"), "Claude Code CLI", ClaudeCodeProvider, ("claude",)),
        ProviderInfo("gemini-cli", ProviderKind.AGENT, _agent_available("gemini"), "Gemini CLI", GeminiCLIProvider, ("gemini",)),
        ProviderInfo("opencode", ProviderKind.AGENT, _agent_available("opencode"), "OpenCode CLI", OpenCodeProvider),
        ProviderInfo("openai-api", ProviderKind.API, True, "OpenAI API", OpenAIProvider),
        ProviderInfo("openrouter", ProviderKind.API, True, "OpenRouter API", OpenRouterProvider),
        ProviderInfo("anthropic-api", ProviderKind.API, True, "Anthropic API", AnthropicProvider),
        ProviderInfo("gemini-api", ProviderKind.API, True, "Google Gemini API", GeminiAPIProvider),
        ProviderInfo("ollama", ProviderKind.API, True, "Ollama local server", OllamaProvider),
        ProviderInfo("mock", ProviderKind.TEST, True, "Mock provider", MockProvider),
    ]
    return [_with_health(provider_info) if provider_info.kind is ProviderKind.API else provider_info for provider_info in providers]


def resolve_provider(providers: list[ProviderInfo]) -> ProviderInfo:
    """Choose the best available provider, preferring agent providers."""
    available = [provider for provider in providers if provider.available]
    if not available:
        raise RuntimeError("No providers are available. Run `gncore provider list` to inspect installation and credentials.")
    for provider in available:
        if provider.kind is ProviderKind.AGENT:
            return provider
    for provider in available:
        if provider.kind is ProviderKind.API:
            return provider
    return available[0]


def provider_by_name(name: str) -> ProviderInfo:
    normalized = name.strip().lower()
    for provider in discover_providers():
        if normalized == provider.name or normalized in provider.aliases:
            return provider
    raise ValueError(f"Unsupported provider: {name}")


def provider_health(name: str) -> str:
    provider = provider_by_name(name)
    status = provider.create().health()
    return f"{status.health.value}: {status.message}"


def _with_health(provider_info: ProviderInfo) -> ProviderInfo:
    status = provider_info.create().health()
    return ProviderInfo(
        provider_info.name,
        provider_info.kind,
        status.health is ProviderHealth.AVAILABLE,
        f"{provider_info.description} ({status.message})",
        provider_info.factory,
        provider_info.aliases,
    )
