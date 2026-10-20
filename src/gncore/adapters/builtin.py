"""Built-in adapters for supported applications."""

from __future__ import annotations

from pathlib import Path

from gncore.adapters.base import AdapterTemplate, ApplicationAdapter, NativeSkillAdapter
from gncore.config import platform_config_dir


class VSCodeChatAdapter(NativeSkillAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="vscode-chat",
                name="VS Code Chat / Copilot Skills",
                config_roots=(platform_config_dir("Code", "User"), Path.home() / ".vscode"),
                executable_names=("code",),
                supports_prompts=False,
                supports_commands=False,
                supports_mcp=False,
                supports_permissions=False,
                supports_settings=False,
            ),
            workspace_relative_dir=Path(".github") / "skills",
            user_relative_dir=Path(".copilot") / "skills",
        )


class AntigravityAdapter(NativeSkillAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="antigravity",
                name="Google Antigravity Skills",
                config_roots=(Path.home() / ".gemini" / "config", Path.home() / ".gemini" / "antigravity"),
                executable_names=("agy", "antigravity"),
                supports_prompts=False,
                supports_commands=False,
                supports_mcp=False,
                supports_permissions=False,
                supports_settings=False,
            ),
            workspace_relative_dir=Path(".agents") / "skills",
            user_relative_dir=Path(".gemini") / "config" / "skills",
        )


class VSCodeCodexAdapter(NativeSkillAdapter):
    """Install into the workspace folder shared by VS Code's Codex harness."""

    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="vscode-codex",
                name="VS Code Codex Skills",
                config_roots=(platform_config_dir("Code", "User"), Path.home() / ".vscode"),
                executable_names=("code",),
                supports_prompts=False,
                supports_commands=False,
                supports_mcp=False,
                supports_permissions=False,
                supports_settings=False,
            ),
            workspace_relative_dir=Path(".agents") / "skills",
            user_relative_dir=Path(".agents") / "skills",
        )


class VSCodeClaudeAdapter(NativeSkillAdapter):
    """Install into the workspace folder shared by VS Code's Claude harness."""

    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="vscode-claude-code",
                name="VS Code Claude Code Skills",
                config_roots=(platform_config_dir("Code", "User"), Path.home() / ".vscode"),
                executable_names=("code",),
                supports_prompts=False,
                supports_commands=False,
                supports_mcp=False,
                supports_permissions=False,
                supports_settings=False,
            ),
            workspace_relative_dir=Path(".claude") / "skills",
            user_relative_dir=Path(".claude") / "skills",
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


class ClaudeCodeAdapter(NativeSkillAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="claude-code",
                name="Claude Code",
                config_roots=(Path.home() / ".claude" / "code", Path.home() / ".claude"),
                executable_names=("claude", "claude-code"),
            ),
            workspace_relative_dir=Path(".claude") / "skills",
            user_relative_dir=Path(".claude") / "skills",
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


class OpenAICodexCLIAdapter(NativeSkillAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="openai-codex-cli",
                name="OpenAI Codex CLI",
                config_roots=(Path.home() / ".codex", platform_config_dir("Codex")),
                executable_names=("codex",),
            ),
            workspace_relative_dir=Path(".agents") / "skills",
            user_relative_dir=Path(".agents") / "skills",
        )


class GeminiCLIAdapter(NativeSkillAdapter):
    def __init__(self) -> None:
        super().__init__(
            AdapterTemplate(
                key="gemini-cli",
                name="Gemini CLI Skills",
                config_roots=(Path.home() / ".gemini", platform_config_dir("Gemini")),
                executable_names=("gemini",),
                supports_prompts=False,
                supports_commands=False,
                supports_mcp=False,
                supports_permissions=False,
                supports_settings=False,
            ),
            workspace_relative_dir=Path(".gemini") / "skills",
            user_relative_dir=Path(".gemini") / "skills",
        )


def builtin_adapters() -> tuple[ApplicationAdapter, ...]:
    return (
        VSCodeChatAdapter(),
        VSCodeCodexAdapter(),
        VSCodeClaudeAdapter(),
        AntigravityAdapter(),
        GitHubCopilotChatAdapter(),
        ClaudeDesktopAdapter(),
        ClaudeCodeAdapter(),
        CursorAdapter(),
        WindsurfAdapter(),
        ContinueAdapter(),
        GeminiCLIAdapter(),
        OpenAICodexCLIAdapter(),
    )
