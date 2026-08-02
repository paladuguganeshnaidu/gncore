from __future__ import annotations

from pathlib import Path

from gncore import GncoreCli


def test_list_skills_and_apps(capsys) -> None:
    cli = GncoreCli()

    assert cli.run(["list", "skills"]) == 0
    output = capsys.readouterr().out
    assert "requirements" in output
    assert "release" in output

    assert cli.run(["list", "apps"]) == 0
    output = capsys.readouterr().out
    assert "VS Code Chat" in output
    assert "Cursor" in output


def test_activate_validate_backup_and_restore(tmp_path: Path, capsys) -> None:
    cli = GncoreCli()

    assert cli.run(["activate", "--apps", "cursor", "--skills", "requirements", "architecture"]) == 0
    output = capsys.readouterr().out
    assert "Activated Cursor" in output

    config_root = cli.adapter_manager.by_key("cursor").discover(Path.cwd()).config_root
    manifest = config_root / "manifest.json"
    assert manifest.is_file()
    assert (config_root / "gncore" / "skills" / "requirements" / "metadata.json").is_file()

    assert cli.run(["validate", "--apps", "cursor"]) == 0
    validation_output = capsys.readouterr().out
    assert "Cursor: valid" in validation_output

    archive = tmp_path / "backup.zip"
    assert cli.run(["backup", "--output", str(archive)]) == 0
    backup_output = capsys.readouterr().out
    assert archive.is_file()
    assert "Backup created" in backup_output

    assert cli.run(["uninstall", "--apps", "cursor"]) == 0
    capsys.readouterr()
    assert not manifest.exists()

    assert cli.run(["restore", str(archive)]) == 0
    restore_output = capsys.readouterr().out
    assert "Restored" in restore_output
    assert manifest.is_file()
