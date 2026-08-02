"""Provider adapters for local external AI assistant CLIs."""

from __future__ import annotations

from dataclasses import dataclass
import shutil
import subprocess
from typing import Iterator

from .base import Provider, ProviderHealth, ProviderResponse, ProviderStatus


@dataclass(frozen=True, slots=True)
class CliProviderConfig:
    """Configuration for a provider backed by a local executable."""

    name: str
    executable: str
    args: tuple[str, ...] = ()
    timeout_seconds: int = 600


class ExternalCliProvider(Provider):
    """Provider adapter that sends prompts to a local CLI process."""

    def __init__(self, config: CliProviderConfig) -> None:
        """Create a provider for a configured local executable."""
        self.config = config
        self._process: subprocess.Popen[str] | None = None

    @property
    def name(self) -> str:
        """Return the provider name."""
        return self.config.name

    def run(self, prompt: str) -> ProviderResponse:
        """Run the configured executable with the prompt on stdin."""
        command = (self.config.executable, *self.config.args)
        completed = subprocess.run(
            command,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=self.config.timeout_seconds,
            check=False,
        )
        if completed.returncode != 0:
            raise RuntimeError(completed.stderr.strip() or f"{self.name} exited with {completed.returncode}")
        return ProviderResponse(completed.stdout, self.name, {"returncode": str(completed.returncode)})

    def stream(self, prompt: str) -> Iterator[str]:
        """Stream stdout lines from the configured executable."""
        command = (self.config.executable, *self.config.args)
        self._process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        assert self._process.stdin is not None
        assert self._process.stdout is not None
        self._process.stdin.write(prompt)
        self._process.stdin.close()
        yield from self._process.stdout
        self._process.wait(timeout=self.config.timeout_seconds)

    def health(self) -> ProviderStatus:
        """Report whether the configured executable is discoverable."""
        if shutil.which(self.config.executable) is None:
            return ProviderStatus(self.name, ProviderHealth.UNAVAILABLE, f"Executable not found: {self.config.executable}")
        return ProviderStatus(self.name, ProviderHealth.AVAILABLE, f"Executable found: {self.config.executable}")

    def cancel(self) -> None:
        """Terminate an in-flight CLI process if one exists."""
        if self._process is not None and self._process.poll() is None:
            self._process.terminate()


class CodexProvider(ExternalCliProvider):
    """Provider adapter for a locally installed Codex CLI."""

    def __init__(self) -> None:
        super().__init__(CliProviderConfig("codex", "codex"))


class ClaudeCodeProvider(ExternalCliProvider):
    """Provider adapter for a locally installed Claude Code CLI."""

    def __init__(self) -> None:
        super().__init__(CliProviderConfig("claude-code", "claude"))


class GeminiCLIProvider(ExternalCliProvider):
    """Provider adapter for a locally installed Gemini CLI."""

    def __init__(self) -> None:
        super().__init__(CliProviderConfig("gemini-cli", "gemini"))


class OpenCodeProvider(ExternalCliProvider):
    """Provider adapter for a locally installed OpenCode CLI."""

    def __init__(self) -> None:
        super().__init__(CliProviderConfig("opencode", "opencode"))
