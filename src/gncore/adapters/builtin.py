"""Built-in adapters for supported applications."""

from __future__ import annotations

from pathlib import Path

from gncore.adapters.base import AdapterTemplate, ApplicationAdapter
from gncore.config import platform_config_dir


class VSCodeChatAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="vscode-chat",
                name="VS Code Chat",
                config_roots=(platform_config_dir("Code", "User"), Path.home() / ".vscode"),
                executable_names=("code",),
            )
        )


class GitHubCopilotChatAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="github-copilot-chat",
                name="GitHub Copilot Chat",
                config_roots=(platform_config_dir("Code", "User"), Path.home() / ".github" / "copilot"),
                executable_names=("gh", "code"),
            )
        )


class ClaudeDesktopAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="claude-desktop",
                name="Claude Desktop",
                config_roots=(platform_config_dir("Claude"), Path.home() / ".claude"),
                executable_names=("claude",),
            )
        )


class ClaudeCodeAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="claude-code",
                name="Claude Code",
                config_roots=(Path.home() / ".claude" / "code", Path.home() / ".claude"),
                executable_names=("claude", "claude-code"),
            )
        )


class CursorAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="cursor",
                name="Cursor",
                config_roots=(Path.home() / ".cursor", platform_config_dir("Cursor")),
                executable_names=("cursor",),
            )
        )


class WindsurfAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="windsurf",
                name="Windsurf",
                config_roots=(Path.home() / ".windsurf", platform_config_dir("Windsurf")),
                executable_names=("windsurf",),
            )
        )


class ContinueAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="continue-dev",
                name="Continue.dev",
                config_roots=(Path.home() / ".continue", platform_config_dir("Continue")),
                executable_names=("continue",),
            )
        )


class GeminiCLIAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="gemini-cli",
                name="Gemini CLI",
                config_roots=(Path.home() / ".gemini", platform_config_dir("Gemini")),
                executable_names=("gemini",),
            )
        )


class OpenAICodexCLIAdapter(ApplicationAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="openai-codex-cli",
                name="OpenAI Codex CLI",
                config_roots=(Path.home() / ".codex", platform_config_dir("Codex")),
                executable_names=("codex",),
            )
        )


def builtin_adapters() -> tuple[ApplicationAdapter, ...]:
    return (
        VSCodeChatAdapter(),
        GitHubCopilotChatAdapter(),
        ClaudeDesktopAdapter(),
        ClaudeCodeAdapter(),
        CursorAdapter(),
        WindsurfAdapter(),
        ContinueAdapter(),
        GeminiCLIAdapter(),
        OpenAICodexCLIAdapter(),
    )
