"""Atomic journals survive transient locks without erasing old recovery state."""
import json
from pathlib import Path
import pytest
import gncore.installation as installer

def busy(code=5):
    error=PermissionError("simulated Windows file lock")
    error.winerror=code
    return error

def test_journal_retries_transient_locks_and_switches_complete_bytes(tmp_path,monkeypatch):
    path=tmp_path/"journal.json"
    path.write_text('{"status":"prepared"}',encoding="utf-8")
    replace=installer.os.replace
    attempts=[]
    sleeps=[]
    def locked(source,destination):
        attempts.append(source)
        assert json.loads(path.read_text(encoding="utf-8"))=={"status":"prepared"}
        assert json.loads(Path(source).read_text(encoding="utf-8"))=={"status":"committed"}
        if len(attempts)<3:raise busy()
        return replace(source,destination)
    monkeypatch.setattr(installer.os,"replace",locked)
    monkeypatch.setattr(installer.time,"sleep",sleeps.append)
    installer._write_json(path,{"status":"committed"})
    assert json.loads(path.read_text(encoding="utf-8"))=={"status":"committed"}
    assert len(attempts)==3 and len(sleeps)==2
    assert list(tmp_path.glob("*.tmp"))==[]

@pytest.mark.parametrize("code,expected_attempts",[(5,8),(32,8),(33,8),(87,1)])
def test_permanent_lock_preserves_previous_journal_and_bounds_retries(tmp_path,monkeypatch,code,expected_attempts):
    path=tmp_path/"journal.json"
    old=b'{"status":"prepared"}\n'
    path.write_bytes(old)
    attempts=[]
    sleeps=[]
    def fail(source,destination):
        attempts.append(source)
        raise busy(code)
    monkeypatch.setattr(installer.os,"replace",fail)
    monkeypatch.setattr(installer.time,"sleep",sleeps.append)
    with pytest.raises(PermissionError):installer._write_json(path,{"status":"committed"})
    assert path.read_bytes()==old
    assert len(attempts)==expected_attempts
    assert len(sleeps)==expected_attempts-1
    assert sum(sleeps)<=1.2
    assert list(tmp_path.glob("*.tmp"))==[]
