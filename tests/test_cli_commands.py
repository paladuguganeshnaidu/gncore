import json
from pathlib import Path
from zipfile import ZipFile

from gncore import GncoreCli, builtin_skills, render_skill
from gncore.skills.bundles import packaged_resources


def test_list_search_show_and_legacy_alias_are_read_only(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    cli = GncoreCli()
    assert cli.run(["list", "skills"]) == 0
    assert "web-frontend" in capsys.readouterr().out
    assert cli.run(["list", "workflows"]) == 0
    assert "train: Train a Machine Learning Model -> machine-learning" in capsys.readouterr().out
    assert cli.run(["list", "domains"]) == 0
    assert "AI and Machine Learning (7 skills" in capsys.readouterr().out
    assert cli.run(["search", "train", "model"]) == 0
    assert "machine-learning" in capsys.readouterr().out
    assert cli.run(["show", "train"]) == 0
    shown = capsys.readouterr().out
    assert "name: machine-learning\n" in shown
    assert "train" in shown and "evaluate" in shown
    assert list(tmp_path.iterdir()) == []


def test_alias_export_merges_workflows_into_one_complete_skill(tmp_path, capsys):
    output = tmp_path / "skills.zip"
    cli = GncoreCli()
    assert cli.run(["export", "--skills", "train", "evaluate", "--output", str(output)]) == 0
    assert "Exported 1 skill(s)" in capsys.readouterr().out
    with ZipFile(output) as archive:
        assert [n for n in archive.namelist() if n.endswith("/SKILL.md")] == ["machine-learning/SKILL.md"]
        assert "license:" in archive.read("machine-learning/SKILL.md").decode()
        for name, content in packaged_resources("machine-learning").items():
            assert archive.read(f"machine-learning/{name}") == content


def test_directory_export_installs_standard_entrypoint_and_all_resources(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert GncoreCli().run(["export", "--specific", "web-front-minimalism"]) == 0
    root = tmp_path / ".agents/skills/web-frontend"
    assert (root / "SKILL.md").is_file()
    for name, content in packaged_resources("web-frontend").items():
        assert (root / name).read_bytes() == content
    assert (root / "references/web-front-react/metadata.json").is_file()
    assert not (root.parent / "web-front-minimalism").exists()


def test_full_catalog_archive_contains_only_active_developer_skills(tmp_path):
    output = tmp_path / "all.zip"
    assert GncoreCli().run(["export", "--all", "--output", str(output)]) == 0
    with ZipFile(output) as archive:
        assert len(archive.namelist()) == len(set(archive.namelist()))
        assert len([n for n in archive.namelist() if n.endswith("/SKILL.md")]) == 30
        assert not any(name.startswith(("finance-accounting/", "company-leadership/")) for name in archive.namelist())
        for skill in builtin_skills():
            assert archive.read(f"{skill.metadata.skill_id}/SKILL.md").decode() == render_skill(skill)


def test_invalid_inputs_and_destination_conflicts_fail_without_writes(tmp_path, capsys):
    cli = GncoreCli()
    assert cli.run(["export", "--skills", "train", "train", "--directory", str(tmp_path / "skills")]) == 2
    assert "unique" in capsys.readouterr().err
    assert not (tmp_path / "skills").exists()
    assert cli.run(["export", "--specific", "train", "--output", str(tmp_path / "x.zip"), "--directory", str(tmp_path)]) == 2
    capsys.readouterr()
    assert cli.run(["show", "no-such-skill"]) == 2
    assert "no-such-skill" in capsys.readouterr().err


def test_plan_command_infers_theme_and_honors_constraints(capsys):
    cli = GncoreCli()
    assert cli.run(["plan", "A premium hotel website, no animation"]) == 0
    plan = json.loads(capsys.readouterr().out)
    assert plan["skill_id"] == "web-frontend"
    assert plan["theme"] == "luxury" and plan["motion"] == "none"
    assert cli.run(["plan", "A dashboard", "--theme", "maximalizm"]) == 0
    assert json.loads(capsys.readouterr().out)["theme"] == "maximalism"


def test_cli_version_and_no_application_orchestration_commands(capsys):
    cli = GncoreCli()
    assert cli.run(["version"]) == 0
    assert capsys.readouterr().out.strip() == "7.0.0"
    for removed in ("activate", "install", "uninstall", "backup", "restore", "doctor"):
        assert cli.run([removed]) == 2
        capsys.readouterr()
