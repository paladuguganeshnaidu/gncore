from __future__ import annotations

import json
from pathlib import Path

from gncore import GncoreCli, ProjectStateManager
from gncore.runtime import GncoreRuntime


def test_init_command_creates_config_and_prompt(tmp_path: Path, capsys) -> None:
    cli = GncoreCli()

    cli.run(["init", str(tmp_path), "--provider", "mock"])

    output = capsys.readouterr().out
    assert "Initialized GNCore project" in output
    assert (tmp_path / ".gncore" / "config.json").is_file()
    assert (tmp_path / "prompt.md").is_file()


def test_run_command_executes_full_workflow(tmp_path: Path, capsys) -> None:
    cli = GncoreCli()
    cli.run(["init", str(tmp_path), "--provider", "mock"])
    capsys.readouterr()

    cli.run(["run", str(tmp_path)])

    output = capsys.readouterr().out
    assert "Workflow complete." in output
    assert (tmp_path / ".gncore" / "outputs" / "planning.md").is_file()
    assert (tmp_path / ".gncore" / "outputs" / "deployment.md").is_file()


def test_resume_command_continues_from_existing_state(tmp_path: Path, capsys) -> None:
    manager = ProjectStateManager(tmp_path)
    manager.initialize("ResumeProject", "mock")
    manager.write_prompt("# Build a product")
    manager.output_file("planning.md").write_text("planning artifact", encoding="utf-8")
    manager.complete_stage(1)
    capsys.readouterr()

    GncoreCli().run(["resume", str(tmp_path)])

    output = capsys.readouterr().out
    assert "Architecture" in output
    assert (tmp_path / ".gncore" / "outputs" / "architecture.md").is_file()


def test_doctor_reports_healthy_project(tmp_path: Path, capsys) -> None:
    cli = GncoreCli()
    cli.run(["init", str(tmp_path), "--provider", "mock"])
    capsys.readouterr()

    cli.run(["doctor", str(tmp_path)])

    output = capsys.readouterr().out
    assert "OK" in output


def test_provider_and_config_commands_update_selection(tmp_path: Path, capsys) -> None:
    cli = GncoreCli()
    cli.run(["init", str(tmp_path), "--provider", "mock"])
    capsys.readouterr()

    cli.run(["provider", str(tmp_path), "use", "mock"])
    capsys.readouterr()
    cli.run(["config", str(tmp_path), "show"])
    output = capsys.readouterr().out
    config = json.loads(output)
    assert config["selected_provider"] == "mock"


def test_auth_and_version_and_update_commands(monkeypatch, capsys) -> None:
    runtime = GncoreRuntime()
    store: dict[str, str] = {}

    monkeypatch.setattr(runtime, "auth_set", lambda provider, token: store.__setitem__(provider, token))
    monkeypatch.setattr(runtime, "auth_get", lambda provider: store.get(provider))
    monkeypatch.setattr(runtime, "auth_delete", lambda provider: store.pop(provider, None))
    monkeypatch.setattr(runtime, "update", lambda dry_run=False: None)

    cli = GncoreCli()
    cli.runtime = runtime

    cli.run(["auth", "login", "mock", "--token", "secret-token"])
    cli.run(["auth", "status", "mock"])
    cli.run(["auth", "logout", "mock"])
    cli.run(["version"])
    cli.run(["update", "--dry-run"])

    output = capsys.readouterr().out
    assert "Stored credential for mock" in output
    assert "mock: credential available" in output
    assert "Removed credential for mock" in output
    from gncore import __version__
    assert __version__ in output
    assert "Would run:" in output
