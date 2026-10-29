"""Digest-based, staged project skill installation with explicit recovery.

No imported helper is executed. Transactions are on the destination filesystem.
An interrupted two-rename switch can be restored using its journal path.
"""

from __future__ import annotations

from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import time
from uuid import uuid4

STATE = ".gncore-install.json"


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _rename(source: Path, destination: Path) -> None:
    """Bound transient Windows sharing/access locks; preserve permanent failures."""
    for attempt in range(8):
        try:
            source.rename(destination)
            return
        except PermissionError as error:
            if getattr(error, "winerror", None) not in {5, 32, 33} or attempt == 7:
                raise
            time.sleep(min(0.025 * (2 ** attempt), 0.2))


def _write_json(path: Path, value: dict) -> None:
    temporary = path.with_name(f".{path.name}.{uuid4().hex}.tmp")
    try:
        with temporary.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        # Indexers and sync clients can briefly hold the current journal open
        # on Windows. Retry the atomic replacement, never an unlink-and-write
        # fallback that would expose a missing or partially written journal.
        for attempt in range(8):
            try:
                os.replace(temporary, path)
                break
            except PermissionError as error:
                if getattr(error, "winerror", None) not in {5, 32, 33} or attempt == 7:
                    raise
                time.sleep(min(0.025 * (2 ** attempt), 0.2))
    finally:
        temporary.unlink(missing_ok=True)


def _relative(name: str) -> Path:
    path = PurePosixPath(name)
    if not name or path.is_absolute() or any(part in {".", ".."} for part in name.split("/")) or "\\" in name or ":" in name:
        raise ValueError(f"unsafe installed resource path: {name}")
    return Path(*path.parts)


def _no_links(path: Path) -> None:
    # Check ancestors once, then inspect entries without repeatedly resolving
    # every ancestor of every file in a large Windows installation.
    if path.absolute() != path.resolve():
        raise ValueError(f"linked installation path is unsupported: {path}")
    pending = [path] if path.is_dir() else []
    while pending:
        with os.scandir(pending.pop()) as children:
            for child in children:
                attributes = child.stat(follow_symlinks=False)
                link_tags = {getattr(stat, "IO_REPARSE_TAG_MOUNT_POINT", 0xA0000003), getattr(stat, "IO_REPARSE_TAG_SYMLINK", 0xA000000C)}
                if child.is_symlink() or getattr(attributes, "st_reparse_tag", 0) in link_tags:
                    raise ValueError(f"linked installed resource is unsupported: {child.path}")
                if child.is_dir(follow_symlinks=False):
                    pending.append(Path(child.path))


def _state(root: Path) -> dict:
    path = root / STATE
    if not path.exists():
        return {"schema_version": 1, "skills": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if data["schema_version"] != 1 or not isinstance(data["skills"], dict):
            raise ValueError("unsupported installation state")
        for skill_id, record in data["skills"].items():
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
                raise ValueError("invalid installed skill ID")
            if not isinstance(record["files"], dict) or "SKILL.md" not in record["files"]:
                raise ValueError("invalid installed file inventory")
            for name, digest in record["files"].items():
                _relative(name)
                if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                    raise ValueError("invalid installed digest")
        return data
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError(f"invalid installation state {path}: {error}") from error


def _files(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): _digest(p.read_bytes()) for p in sorted(root.rglob("*")) if p.is_file()}


def _preflight(root: Path, payloads: dict[str, dict[str, bytes]], legacy: dict[str, dict[str, bytes]], retire: set[str] | None = None) -> tuple[dict, dict]:
    _no_links(root)
    if root.exists() and not root.is_dir():
        raise ValueError(f"installation destination is not a directory: {root}")
    state = _state(root)
    actions = {"install": [], "update": [], "adopt": [], "migrate": [], "preserved_legacy": [], "retire": [], "preserved_retired": []}
    for skill_id, payload in payloads.items():
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id) or not payload or "SKILL.md" not in payload:
            raise ValueError(f"invalid skill payload: {skill_id}")
        for name, content in payload.items():
            _relative(name)
            if not isinstance(content, bytes):
                raise ValueError(f"resource must contain bytes: {skill_id}/{name}")
        folder = root / skill_id
        if not folder.exists():
            actions["install"].append(skill_id)
            continue
        if not folder.is_dir():
            raise ValueError(f"unmanaged destination collision: {folder}")
        for name in payload:
            target = folder / _relative(name)
            if target.exists() and not target.is_file():
                raise ValueError(f"unmanaged resource directory collision: {skill_id}/{name}")
            for ancestor in target.parents:
                if ancestor == folder:
                    break
                if ancestor.exists() and not ancestor.is_dir():
                    raise ValueError(f"unmanaged resource parent collision: {ancestor}")
        actual = _files(folder)
        expected = {name: _digest(content) for name, content in payload.items()}
        recorded = state["skills"].get(skill_id, {}).get("files")
        if recorded is None:
            # Older exports are adopted only when every known byte matches.
            # The word GNCore or a familiar filename is never ownership proof.
            if any(actual.get(name) != digest for name, digest in expected.items()):
                raise ValueError(f"unmanaged or customized skill would be overwritten: {skill_id}")
            actions["adopt"].append(skill_id)
        else:
            changed = [name for name, digest in recorded.items() if actual.get(name) != digest]
            collision = [name for name in expected if name in actual and name not in recorded and actual[name] != expected[name]]
            if changed or collision:
                raise ValueError(f"modified managed skill {skill_id}; preserved without changes: {', '.join(changed + collision)}")
            actions["update"].append(skill_id)
    for skill_id, expected in legacy.items():
        if skill_id in payloads:
            continue
        _relative(skill_id)
        if "/" in skill_id:
            raise ValueError("legacy skill ID must be one folder name")
        folder = root / skill_id
        if folder.exists():
            hashes = {name: _digest(content) for name, content in expected.items()}
            # Preserve extra/custom legacy files in place, never silently remove them.
            action = "migrate" if folder.is_dir() and _files(folder) == hashes else "preserved_legacy"
            actions[action].append(skill_id)
    for skill_id in sorted(retire or set()):
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id) or skill_id in payloads:
            raise ValueError(f"invalid retirement target: {skill_id}")
        folder = root / skill_id
        if folder.exists():
            recorded = state["skills"].get(skill_id, {}).get("files")
            action = "retire" if recorded and folder.is_dir() and _files(folder) == recorded else "preserved_retired"
            actions[action].append(skill_id)
    return state, actions


def _transaction_base(root: Path) -> Path:
    return root.parent / f".gncore-{root.name}-transactions"


@contextmanager
def _writer_lock(root: Path):
    path = root.parent / f".gncore-{root.name}.lock"
    try:
        descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as error:
        raise ValueError(f"installation lock exists: {path}; stop any active writer before recovery") from error
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            stream.write(str(os.getpid()))
        yield
    finally:
        path.unlink(missing_ok=True)


def install_skills(root: Path, payloads: dict[str, dict[str, bytes]], *, version: str,
                   dry_run: bool = False, legacy: dict[str, dict[str, bytes]] | None = None,
                   retire: set[str] | None = None) -> dict:
    """Preflight every destination, stage a full tree, then switch with backup.

    Modified managed files stop the whole install; unrelated files are copied
    verbatim. Backups are retained, including after a successful update.
    """
    root = root.expanduser().absolute()
    legacy = legacy or {}
    state, actions = _preflight(root, payloads, legacy, retire)
    result = {"directory": str(root), "dry_run": dry_run, **actions}
    if dry_run:
        return result
    base = _transaction_base(root)
    _no_links(base)
    if base.exists():
        for journal in base.glob("*/journal.json"):
            if json.loads(journal.read_text(encoding="utf-8")).get("status") in {"prepared", "switching", "recovery-required"}:
                raise ValueError(f"unfinished installation; recover before retrying: {journal}")
    root.parent.mkdir(parents=True, exist_ok=True)
    with _writer_lock(root):
        state, actions = _preflight(root, payloads, legacy, retire)
        transaction = base / uuid4().hex
        transaction.mkdir(parents=True)
        stage, backup = transaction / "staged", transaction / "backup"
        journal = transaction / "journal.json"
        record = {"schema_version": 1, "root": str(root), "had_root": root.exists(), "status": "prepared"}
        _write_json(journal, record)
        try:
            original = _files(root) if root.exists() else None
            if root.exists():
                shutil.copytree(root, stage)
            else:
                stage.mkdir()
            for skill_id in actions["migrate"] + actions["retire"]:
                target = stage / skill_id
                if not target.resolve().is_relative_to(stage.resolve()):
                    raise ValueError("migration escaped staged installation")
                shutil.rmtree(target)
                state["skills"].pop(skill_id, None)
            for skill_id, payload in payloads.items():
                folder = stage / skill_id
                old_files = state["skills"].get(skill_id, {}).get("files", {})
                for name in old_files.keys() - payload.keys():
                    (folder / _relative(name)).unlink()
                for name, content in payload.items():
                    target = folder / _relative(name)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_bytes(content)
                expected = {name: _digest(content) for name, content in payload.items()}
                actual = _files(folder)
                if any(actual.get(name) != digest for name, digest in expected.items()):
                    raise ValueError(f"staged content verification failed: {skill_id}")
                state["skills"][skill_id] = {"version": version, "files": expected}
            _write_json(stage / STATE, state)
            if (root.exists() != record["had_root"]) or (root.exists() and _files(root) != original):
                raise ValueError("installation changed while staging; original files preserved, retry after the edit finishes")
            record["status"] = "switching"
            _write_json(journal, record)
            if root.exists():
                _rename(root, backup)
            _rename(stage, root)
            record["status"] = "committed"
            _write_json(journal, record)
        except BaseException:
            try:
                _restore(root, transaction, record)
                record["status"] = "rolled-back"
            except OSError:
                record["status"] = "recovery-required"
            _write_json(journal, record)
            raise
        return {**result, **actions, "journal": str(journal), "backup": str(backup) if backup.exists() else None}


def _restore(root: Path, transaction: Path, record: dict) -> None:
    backup, stage = transaction / "backup", transaction / "staged"
    if backup.exists():
        if root.exists():
            _rename(root, transaction / "failed-install")
        _rename(backup, root)
    elif not record["had_root"] and root.exists() and not stage.exists():
        _rename(root, transaction / "failed-install")
    elif record["had_root"] and record["status"] in {"switching", "recovery-required"} and not stage.exists():
        raise OSError("original installation backup is missing; preserve the transaction for manual recovery")


def recover_installation(root: Path, journal: Path) -> dict:
    """Restore an interrupted switch; call only after the original writer stops."""
    root = root.expanduser().absolute()
    journal = journal.expanduser().absolute()
    _no_links(root)
    _no_links(journal.parent)
    if journal.name != "journal.json" or journal.parent.parent != _transaction_base(root) or not re.fullmatch(r"[a-f0-9]{32}", journal.parent.name):
        raise ValueError("recovery journal is outside this installation's transaction directory")
    record = json.loads(journal.read_text(encoding="utf-8"))
    if record.get("schema_version") != 1 or record.get("root") != str(root) or not isinstance(record.get("had_root"), bool):
        raise ValueError("recovery journal does not describe this installation")
    if record.get("status") == "committed":
        # A process can stop after committing the journal but before releasing
        # its lock. Finish that commit instead of rolling back a good install.
        if not verify_installation(root)["ok"]:
            raise ValueError("committed installation has changed; review it before clearing the writer lock")
        (root.parent / f".gncore-{root.name}.lock").unlink(missing_ok=True)
        return {"status": "committed", "directory": str(root), "journal": str(journal)}
    if record.get("status") not in {"prepared", "switching", "recovery-required"}:
        raise ValueError("only an unfinished installation can be recovered")
    _restore(root, journal.parent, record)
    record["status"] = "rolled-back"
    _write_json(journal, record)
    # A killed process cannot release its lock; explicit recovery clears it.
    (root.parent / f".gncore-{root.name}.lock").unlink(missing_ok=True)
    return {"status": record["status"], "directory": str(root), "journal": str(journal)}


def verify_installation(root: Path) -> dict:
    """Read-only comparison with recorded hashes; modifications are not deleted."""
    root = root.expanduser().absolute()
    _no_links(root)
    if not (root / STATE).is_file():
        raise ValueError(f"no GNCore installation inventory: {root / STATE}")
    state = _state(root)
    missing, modified, unmanaged = [], [], []
    expected = {f"{skill_id}/{name}": digest for skill_id, item in state["skills"].items() for name, digest in item["files"].items()}
    actual = _files(root)
    for name, digest in expected.items():
        if name not in actual:
            missing.append(name)
        elif actual[name] != digest:
            modified.append(name)
    unmanaged = sorted(set(actual) - set(expected) - {STATE})
    return {"directory": str(root), "skills": len(state["skills"]), "files": len(expected), "missing": missing,
            "modified": modified, "unmanaged": unmanaged, "ok": not (missing or modified)}
