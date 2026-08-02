"""GitHub Copilot CLI provider adapter for GNCore."""

from __future__ import annotations

from dataclasses import dataclass
import shutil
import subprocess
from typing import Iterator

from .base import Provider, ProviderHealth, ProviderResponse, ProviderStatus


@dataclass(frozen=True, slots=True)
class CopilotProviderConfig:
    """Configuration for the GitHub Copilot CLI wrapper."""

    name: str = "github-copilot-agent"
    executable: str = "gh"
    args: tuple[str, ...] = ("copilot",)


class GitHubCopilotAgentProvider(Provider):
    """Provider adapter backed by the GitHub Copilot CLI."""

    def __init__(self, config: CopilotProviderConfig | None = None) -> None:
        self.config = config or CopilotProviderConfig()

    @property
    def name(self) -> str:
        return self.config.name

    def run(self, prompt: str) -> ProviderResponse:
        command = (
            self.config.executable,
            *self.config.args,
            "-p",
            prompt,
            "--allow-tool",
            "shell(git)",
        )
        completed = subprocess.run(command, capture_output=True, text=True, check=False)
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip() or f"{self.name} exited with {completed.returncode}")
        return ProviderResponse(completed.stdout, self.name, {"returncode": str(completed.returncode)})

    def stream(self, prompt: str) -> Iterator[str]:
        yield self.run(prompt).content

    def health(self) -> ProviderStatus:
        if shutil.which(self.config.executable) is None:
            return ProviderStatus(self.name, ProviderHealth.UNAVAILABLE, f"Executable not found: {self.config.executable}")
        return ProviderStatus(self.name, ProviderHealth.AVAILABLE, "GitHub Copilot CLI is available")

    def cancel(self) -> None:
        return None
