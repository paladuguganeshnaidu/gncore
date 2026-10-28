"""Failure-path checks use small real trees, never the developer's skills."""

import json
import os
from pathlib import Path
import subprocess
import sys

import pytest

import gncore.installation as installer
from gncore.installation import STATE, install_skills, recover_installation, verify_installation


OLD = {"alpha": {"SKILL.md": b"GNCore alpha old", "references/a.txt": b"old"}}
NEW = {"alpha": {"SKILL.md": b"GNCore alpha new", "references/b.txt": b"new"}, "beta": {"SKILL.md": b"beta"}}


def snapshot(root):
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob("*") if p.is_file()}


def test_full_preflight_rejects_late_collision_without_migrating_or_writing(tmp_path):
    root = tmp_path / "skills"
    (root / "old").mkdir(parents=True)
    (root / "old/SKILL.md").write_bytes(b"known legacy")
    (root / "beta").mkdir()
    (root / "beta/SKILL.md").write_bytes(b"custom GNCore text is not proof of ownership")
    before = snapshot(tmp_path)
    with pytest.raises(ValueError, match="unmanaged"):
        install_skills(root, NEW, version="2", legacy={"old": {"SKILL.md": b"known legacy"}})
    assert snapshot(tmp_path) == before
    assert not (root / "alpha").exists()


def test_dry_run_adoption_is_read_only_and_retains_extra_files(tmp_path):
    root = tmp_path / "skills"
    (root / "alpha/references").mkdir(parents=True)
    for name, content in OLD["alpha"].items():
        (root / "alpha" / name).write_bytes(content)
    (root / "alpha/custom.txt").write_bytes(b"my additions")
    before = snapshot(tmp_path)
    result = install_skills(root, OLD, version="1", dry_run=True)
    assert result["adopt"] == ["alpha"]
    assert snapshot(tmp_path) == before
    install_skills(root, OLD, version="1")
    assert verify_installation(root)["unmanaged"] == ["alpha/custom.txt"]


def test_update_removes_only_obsolete_managed_files_and_backs_up_everything(tmp_path):
    root = tmp_path / "my skills 甲"
    install_skills(root, OLD, version="1")
    (root / "alpha/custom.txt").write_bytes(b"user notes")
    (root / ".gncore-install.tmp").write_bytes(b"user file with a temporary-looking name")
    (root / "other").mkdir()
    (root / "other/SKILL.md").write_bytes(b"another publisher")
    before = snapshot(root)
    result = install_skills(root, NEW, version="2")
    assert snapshot(Path(result["backup"])) == before
    assert not (root / "alpha/references/a.txt").exists()
    assert (root / "alpha/references/b.txt").read_bytes() == b"new"
    assert (root / "alpha/custom.txt").read_bytes() == b"user notes"
    report = verify_installation(root)
    assert report["ok"] and report["skills"] == 2 and report["files"] == 3
    assert report["unmanaged"] == [".gncore-install.tmp", "alpha/custom.txt", "other/SKILL.md"]
    assert (root / ".gncore-install.tmp").read_bytes() == b"user file with a temporary-looking name"


@pytest.mark.parametrize("change", ["modify", "delete", "new-collision"])
def test_customized_managed_install_is_preserved(tmp_path, change):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    if change == "modify":
        (root / "alpha/SKILL.md").write_bytes(b"my new instruction")
    elif change == "delete":
        (root / "alpha/references/a.txt").unlink()
    else:
        (root / "alpha/references/b.txt").write_bytes(b"my personal b")
    before = snapshot(tmp_path)
    with pytest.raises(ValueError, match="modified managed"):
        install_skills(root, NEW, version="2")
    assert snapshot(tmp_path) == before


def test_only_exact_legacy_tree_is_migrated_and_backup_preserves_it(tmp_path):
    root = tmp_path / "skills"
    for name in ["old", "custom-old"]:
        (root / name).mkdir(parents=True)
        (root / name / "SKILL.md").write_bytes(b"GNCore legacy")
    (root / "custom-old/notes.txt").write_bytes(b"custom")
    legacy = {name: {"SKILL.md": b"GNCore legacy"} for name in ["old", "custom-old"]}
    result = install_skills(root, OLD, version="1", legacy=legacy)
    assert result["migrate"] == ["old"] and result["preserved_legacy"] == ["custom-old"]
    assert not (root / "old").exists()
    assert (Path(result["backup"]) / "old/SKILL.md").read_bytes() == b"GNCore legacy"
    assert (root / "custom-old/notes.txt").read_bytes() == b"custom"


@pytest.mark.parametrize("had_root", [False, True])
def test_failed_switch_restores_original_or_absence(tmp_path, monkeypatch, had_root):
    root = tmp_path / "skills"
    if had_root:
        install_skills(root, OLD, version="1")
    before = snapshot(root)
    original = Path.rename

    def fail_switch(path, target):
        if path.name == "staged":
            raise PermissionError("simulated switch failure")
        return original(path, target)

    monkeypatch.setattr(Path, "rename", fail_switch)
    with pytest.raises(PermissionError, match="simulated"):
        install_skills(root, NEW, version="2")
    assert snapshot(root) == before and root.exists() == had_root
    journals = [json.loads(p.read_text()) for p in installer._transaction_base(root).glob("*/journal.json")]
    assert journals[-1]["status"] == "rolled-back" or any(j["status"] == "rolled-back" for j in journals)


def test_staging_permission_failure_does_not_touch_install(tmp_path, monkeypatch):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    before = snapshot(root)
    def fail_copy(*args, **kwargs):
        raise PermissionError("simulated staging failure")
    monkeypatch.setattr(installer.shutil, "copytree", fail_copy)
    with pytest.raises(PermissionError, match="staging"):
        install_skills(root, NEW, version="2")
    assert snapshot(root) == before


@pytest.mark.parametrize("after_switch", [False, True])
def test_explicit_crash_recovery_restores_backup(tmp_path, after_switch):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    before = snapshot(root)
    transaction = installer._transaction_base(root) / ("a" * 32)
    transaction.mkdir()
    root.rename(transaction / "backup")
    stage = transaction / "staged"
    stage.mkdir()
    (stage / "SKILL.md").write_bytes(b"partial new tree")
    if after_switch:
        stage.rename(root)
    journal = transaction / "journal.json"
    journal.write_text(json.dumps({"schema_version": 1, "root": str(root), "had_root": True, "status": "switching"}))
    with pytest.raises(ValueError, match="unfinished"):
        install_skills(root, NEW, version="2")
    assert recover_installation(root, journal)["status"] == "rolled-back"
    assert snapshot(root) == before


def test_readonly_verification_reports_missing_and_modified(tmp_path):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    (root / "alpha/SKILL.md").write_bytes(b"customized")
    (root / "alpha/references/a.txt").unlink()
    before = snapshot(tmp_path)
    report = verify_installation(root)
    assert not report["ok"]
    assert report["missing"] == ["alpha/references/a.txt"]
    assert report["modified"] == ["alpha/SKILL.md"]
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("content", ['{', '{"schema_version":2,"skills":{}}', '{"schema_version":1,"skills":{"../escape":{}}}'])
def test_corrupt_state_fails_without_writes(tmp_path, content):
    root = tmp_path / "skills"
    root.mkdir()
    (root / STATE).write_text(content)
    before = snapshot(tmp_path)
    with pytest.raises(ValueError, match="invalid installation state"):
        install_skills(root, OLD, version="1")
    assert snapshot(tmp_path) == before


@pytest.mark.parametrize("resource", ["../escape", "/escape", "x/../../escape", "C:/escape", "x\\escape", "a/./b"])
def test_unsafe_payload_is_rejected_before_writes(tmp_path, resource):
    with pytest.raises(ValueError, match="unsafe"):
        install_skills(tmp_path / "skills", {"alpha": {"SKILL.md": b"alpha", resource: b"bad"}}, version="1")
    assert list(tmp_path.iterdir()) == []


def test_recovery_rejects_journal_outside_its_root(tmp_path):
    with pytest.raises(ValueError, match="outside"):
        recover_installation(tmp_path / "skills", tmp_path / "journal.json")


def test_second_writer_is_rejected_without_changes(tmp_path):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    lock = root.parent / ".gncore-skills.lock"
    lock.write_text("active writer")
    before = snapshot(tmp_path)
    with pytest.raises(ValueError, match="lock exists"):
        install_skills(root, NEW, version="2")
    assert snapshot(tmp_path) == before


def test_actual_process_exit_during_switch_can_be_recovered(tmp_path):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    before = snapshot(root)
    code = """
import os
from pathlib import Path
import sys
from gncore.installation import install_skills
rename = Path.rename
def stop_before_switch(path, target):
    if path.name == 'staged':
        os._exit(77)
    return rename(path, target)
Path.rename = stop_before_switch
install_skills(Path(sys.argv[1]), {'alpha': {'SKILL.md': b'new'}}, version='2')
"""
    environment = {**os.environ, "PYTHONPATH": str(Path(installer.__file__).parents[1])}
    result = subprocess.run([sys.executable, "-c", code, str(root)], cwd=tmp_path, env=environment, timeout=30, capture_output=True)
    assert result.returncode == 77, result.stderr.decode(errors="replace")
    assert not root.exists()
    journals = [p for p in installer._transaction_base(root).glob("*/journal.json") if json.loads(p.read_text())["status"] == "switching"]
    assert len(journals) == 1
    recover_installation(root, journals[0])
    assert snapshot(root) == before
    assert not (root.parent / ".gncore-skills.lock").exists()


def test_committed_journal_finishes_lock_cleanup_without_rollback(tmp_path):
    root = tmp_path / "skills"
    result = install_skills(root, OLD, version="1")
    before = snapshot(root)
    (root.parent / ".gncore-skills.lock").write_text("interrupted cleanup")
    report = recover_installation(root, Path(result["journal"]))
    assert report["status"] == "committed" and snapshot(root) == before
    assert not (root.parent / ".gncore-skills.lock").exists()


def test_concurrent_user_edit_during_staging_aborts_without_losing_edit(tmp_path, monkeypatch):
    root = tmp_path / "skills"
    install_skills(root, OLD, version="1")
    copytree = installer.shutil.copytree
    def edit_after_copy(*args, **kwargs):
        result = copytree(*args, **kwargs)
        (root / "alpha/SKILL.md").write_bytes(b"user edited during install")
        return result
    monkeypatch.setattr(installer.shutil, "copytree", edit_after_copy)
    with pytest.raises(ValueError, match="changed while staging"):
        install_skills(root, NEW, version="2")
    assert (root / "alpha/SKILL.md").read_bytes() == b"user edited during install"
    assert (root / "alpha/references/a.txt").read_bytes() == b"old"


def test_linked_resource_is_rejected_without_modifying_external_file(tmp_path):
    root = tmp_path / "skills"
    (root / "alpha").mkdir(parents=True)
    external = tmp_path / "external"
    external.write_bytes(b"do not modify")
    try:
        (root / "alpha/SKILL.md").symlink_to(external)
    except OSError:
        pytest.skip("creating symlinks is unavailable to this Windows account")
    with pytest.raises(ValueError, match="linked"):
        install_skills(root, OLD, version="1")
    assert external.read_bytes() == b"do not modify"
