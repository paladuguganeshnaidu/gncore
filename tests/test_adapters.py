from __future__ import annotations

from pathlib import Path

from gncore.adapters import get_adapter_registry
from gncore.adapters.base import AdapterTemplate, NativeSkillAdapter
from gncore.skills.library import get_skill


def test_supported_adapter_registry_contains_all_targets() -> None:
    registry = get_adapter_registry()
    keys = [adapter.key for adapter in registry.adapters]
    assert keys == [
        "vscode-chat",
        "vscode-codex",
        "vscode-claude-code",
        "antigravity",
        "github-copilot-chat",
        "claude-desktop",
        "claude-code",
        "cursor",
        "windsurf",
        "continue-dev",
        "gemini-cli",
        "openai-codex-cli",
    ]


def test_native_adapters_target_each_application_skill_folder() -> None:
    registry = get_adapter_registry()
    assert registry.by_key("vscode-chat").workspace_relative_dir == Path(".github") / "skills"
    assert registry.by_key("vscode-codex").workspace_relative_dir == Path(".agents") / "skills"
    assert registry.by_key("vscode-claude-code").workspace_relative_dir == Path(".claude") / "skills"
    assert registry.by_key("antigravity").workspace_relative_dir == Path(".agents") / "skills"
    assert registry.by_key("claude-code").workspace_relative_dir == Path(".claude") / "skills"
    assert registry.by_key("openai-codex-cli").workspace_relative_dir == Path(".agents") / "skills"
    assert registry.by_key("gemini-cli").workspace_relative_dir == Path(".gemini") / "skills"


def test_native_install_writes_invokable_skill_and_preserves_unmanaged_content(tmp_path: Path) -> None:
    adapter = NativeSkillAdapter(
        AdapterTemplate("test-agent", "Test Agent", (tmp_path / "user",)),
        Path(".agents") / "skills",
        Path(".agents") / "skills",
    )
    unmanaged = tmp_path / ".agents" / "skills" / "custom" / "SKILL.md"
    unmanaged.parent.mkdir(parents=True)
    unmanaged.write_text("user-owned", encoding="utf-8")

    report = adapter.install([get_skill("train")], workspace_root=tmp_path, scope="workspace")

    managed = tmp_path / ".agents" / "skills" / "train" / "SKILL.md"
    assert report.verified is True
    assert "name: train" in managed.read_text(encoding="utf-8")
    assert unmanaged.read_text(encoding="utf-8") == "user-owned"
    assert adapter.validate(workspace_root=tmp_path, scope="workspace").valid
    adapter.uninstall(workspace_root=tmp_path, scope="workspace")
    assert not managed.exists()
    assert unmanaged.exists()


def test_shared_native_folder_tracks_multiple_gncore_app_owners(tmp_path: Path) -> None:
    workspace_skills = Path(".agents") / "skills"
    codex = NativeSkillAdapter(
        AdapterTemplate("codex", "Codex", (tmp_path / "user",)), workspace_skills, workspace_skills
    )
    vscode = NativeSkillAdapter(
        AdapterTemplate("vscode-codex", "VS Code Codex", (tmp_path / "user",)), workspace_skills, workspace_skills
    )
    codex.install([get_skill("train")], workspace_root=tmp_path, scope="workspace")
    vscode.install([get_skill("train")], workspace_root=tmp_path, scope="workspace")
    extra = tmp_path / ".agents" / "skills" / "train" / "references" / "local-notes.md"
    extra.parent.mkdir()
    extra.write_text("user-owned", encoding="utf-8")

    codex.uninstall(workspace_root=tmp_path, scope="workspace")

    skill_md = tmp_path / ".agents" / "skills" / "train" / "SKILL.md"
    assert skill_md.is_file()
    assert extra.read_text(encoding="utf-8") == "user-owned"
    assert vscode.validate(workspace_root=tmp_path, scope="workspace").valid
    vscode.uninstall(workspace_root=tmp_path, scope="workspace")
    assert not skill_md.exists()
    assert extra.exists()
