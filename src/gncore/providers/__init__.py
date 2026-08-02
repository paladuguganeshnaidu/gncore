"""Provider adapters and discovery helpers for GNCore."""

from .api import AnthropicProvider, GeminiAPIProvider, OllamaProvider, OpenAIProvider, OpenRouterProvider
from .base import Provider, ProviderHealth, ProviderResponse, ProviderStatus
from .catalog import ProviderInfo, ProviderKind, discover_providers, provider_by_name, resolve_provider
from .credentials import CredentialError, CredentialStore
from .copilot import GitHubCopilotAgentProvider
from .external import ClaudeCodeProvider, CodexProvider, ExternalCliProvider, GeminiCLIProvider, OpenCodeProvider
from .factory import ProviderFactory
from .mock import MockProvider

__all__ = [
	"AnthropicProvider",
	"ClaudeCodeProvider",
	"CodexProvider",
	"CredentialError",
	"CredentialStore",
	"discover_providers",
	"ExternalCliProvider",
	"GeminiAPIProvider",
	"GeminiCLIProvider",
	"GitHubCopilotAgentProvider",
	"MockProvider",
	"OllamaProvider",
	"OpenAIProvider",
	"OpenCodeProvider",
	"OpenRouterProvider",
	"Provider",
	"ProviderFactory",
	"ProviderHealth",
	"ProviderInfo",
	"ProviderKind",
	"ProviderResponse",
	"ProviderStatus",
	"provider_by_name",
	"resolve_provider",
]
