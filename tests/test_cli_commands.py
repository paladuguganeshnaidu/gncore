from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile

from gncore import GncoreCli


def test_list_search_and_show_skills(tmp_path: Path, monkeypatch, capsys) -> None:
    monkeypatch.chdir(tmp_path)
    cli = GncoreCli()

    assert cli.run(["list", "skills"]) == 0
    assert "train: Train a Machine Learning Model" in capsys.readouterr().out

    assert cli.run(["list", "domains"]) == 0
    domains = capsys.readouterr().out
    assert "Company Leadership" in domains
    assert "Microsoft Word and DOCX Documents" in domains
    assert "PDF Documents" in domains

    assert cli.run(["search", "train", "model"]) == 0
    assert "train: Train a Machine Learning Model" in capsys.readouterr().out

    assert cli.run(["show", "train"]) == 0
    shown = capsys.readouterr().out
    assert "name: train" in shown
    assert "held-out evaluation" in shown
    assert list(tmp_path.iterdir()) == []


def test_export_writes_only_portable_skill_folders(tmp_path: Path, capsys) -> None:
    output = tmp_path / "nested" / "skills.zip"
    cli = GncoreCli()

    assert cli.run(["export", "--skills", "train", "evaluate", "--output", str(output)]) == 0
    assert "Exported 2 skill(s)" in capsys.readouterr().out
    with ZipFile(output) as archive:
        names = set(archive.namelist())
        assert names == {"README.md", "train/SKILL.md", "evaluate/SKILL.md"}
        skill_md = archive.read("train/SKILL.md").decode("utf-8")
        assert "name: train" in skill_md
        assert "Establish a simple baseline" in skill_md


def test_all_export_and_unknown_skill_error(tmp_path: Path, capsys) -> None:
    output = tmp_path / "all.zip"
    cli = GncoreCli()
    assert cli.run(["export", "--all", "--output", str(output)]) == 0
    with ZipFile(output) as archive:
        assert len([name for name in archive.namelist() if name.endswith("/SKILL.md")]) == 403

    assert cli.run(["show", "not-a-skill"]) == 2
    assert "not-a-skill" in capsys.readouterr().err


def test_cli_has_no_application_or_orchestration_commands(capsys) -> None:
    cli = GncoreCli()
    assert cli.run([]) == 0
    help_text = capsys.readouterr().out
    assert all(command in help_text for command in ("list", "search", "show", "export", "version"))
    for removed_command in ("activate", "install", "uninstall", "backup", "restore", "doctor", "validate"):
        assert cli.run([removed_command]) == 2
        capsys.readouterr()

    assert cli.run(["list", "apps"]) == 2
    capsys.readouterr()


def test_version(capsys) -> None:
    assert GncoreCli().run(["version"]) == 0
    assert capsys.readouterr().out.strip() == "5.0.0"
