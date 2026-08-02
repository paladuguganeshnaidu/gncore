"""Provider contracts for external AI execution engines."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Iterator


class ProviderHealth(str, Enum):
    """Health states reported by provider adapters."""

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


@dataclass(frozen=True, slots=True)
class ProviderStatus:
    """Provider health details suitable for CLI display and logs."""

    name: str
    health: ProviderHealth
    message: str


@dataclass(frozen=True, slots=True)
class ProviderResponse:
    """Normalized provider execution response."""

    content: str
    provider_name: str
    metadata: dict[str, str]


class Provider(ABC):
    """Abstract interface implemented by AI provider adapters."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the provider name."""

    @abstractmethod
    def run(self, prompt: str) -> ProviderResponse:
        """Execute a prompt and return a normalized response."""

    @abstractmethod
    def stream(self, prompt: str) -> Iterator[str]:
        """Stream provider output chunks for a prompt."""

    @abstractmethod
    def health(self) -> ProviderStatus:
        """Return provider availability details."""

    @abstractmethod
    def cancel(self) -> None:
        """Cancel any in-flight provider execution."""
