"""GNCore orchestration framework public API."""

from gncore.cli.app import CliConfig, CliSelection, GncoreCli
from gncore.core.executor import (
    DependencyError,
    ExecutionEngine,
    ExecutionResult,
    MissingSkillError,
    ProviderError,
    StateError,
)
from gncore.core.prompt import PromptBuilder, PromptInput
from gncore.core.stages import StageDefinition, StageRegistry, default_stage_registry
from gncore.core.workflow import StagePreparation, StageWorkflow
from gncore.config import ConfigError, GncoreConfig
from gncore.providers.api import AnthropicProvider, GeminiAPIProvider, OllamaProvider, OpenAIProvider, OpenRouterProvider
from gncore.providers.catalog import ProviderInfo, ProviderKind, discover_providers
from gncore.providers.credentials import CredentialError, CredentialStore
from gncore.providers.copilot import GitHubCopilotAgentProvider
from gncore.providers.base import Provider, ProviderHealth, ProviderResponse, ProviderStatus
from gncore.providers.external import (
    ClaudeCodeProvider,
    CodexProvider,
    ExternalCliProvider,
    GeminiCLIProvider,
    OpenCodeProvider,
)
from gncore.providers.factory import ProviderFactory
from gncore.providers.mock import MockProvider
from gncore.runtime import GncoreRuntime, ProjectValidationError, ValidationIssue
from gncore.skills.loader import SkillLoader
from gncore.state.manager import ProjectStateManager
from gncore.state.models import ProjectState

__version__ = "2.1.2"

__all__ = [
    "CliConfig",
    "GncoreCli",
    "CliSelection",
    "ConfigError",
    "GncoreConfig",
    "GncoreRuntime",
    "ProjectValidationError",
    "ValidationIssue",
    "StateError",
    "ProviderError",
    "MissingSkillError",
    "ExecutionResult",
    "ExecutionEngine",
    "DependencyError",
    "ProviderInfo",
    "ProviderKind",
    "discover_providers",
    "CredentialError",
    "CredentialStore",
    "OpenAIProvider",
    "OpenRouterProvider",
    "AnthropicProvider",
    "GeminiAPIProvider",
    "OllamaProvider",
    "GitHubCopilotAgentProvider",
    "MockProvider",
    "PromptBuilder",
    "PromptInput",
    "ProjectState",
    "ProjectStateManager",
    "Provider",
    "ProviderFactory",
    "OpenCodeProvider",
    "GeminiCLIProvider",
    "ClaudeCodeProvider",
    "CodexProvider",
    "ExternalCliProvider",
    "ProviderStatus",
    "ProviderHealth",
    "ProviderResponse",
    "SkillLoader",
    "StageDefinition",
    "StageRegistry",
    "StagePreparation",
    "StageWorkflow",
    "default_stage_registry",
]
