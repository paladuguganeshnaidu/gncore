import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile
from uuid import uuid4

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_website_rebuild_has_complete_internal_links_anchors_and_migration_targets(tmp_path):
    # Generate outside the committed website tree and check actual output files.
    destination = ROOT / ".work/website-test-builds" / uuid4().hex
    result = subprocess.run([sys.executable, str(ROOT / "scripts/build_website.py"), "--output", str(destination)], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", timeout=60)
    assert result.returncode == 0, result.stdout + result.stderr
    report = load_script("check_website").check(destination)
    assert report["ok"], report["issues"]
    assert report["html_pages"] == 42 and report["categories"] == 30 and report["workflows"] == 374
    assert report["redirects_checked"] > 500 and report["local_links_checked"] > 1000
    catalog = json.loads((destination / "assets/catalog.json").read_text(encoding="utf-8"))
    assert catalog["status"] == "candidate-preview"
    assert "Disallow: /" in (destination / "robots.txt").read_text()
    assert "Publication pending approval" in (destination / "index.html").read_text(encoding="utf-8")
    assert "/skills/ui-minimalism/ /skills/web-frontend/ 301" in (destination / "_redirects").read_text()
    (destination / "assets/favicon.svg").unlink()
    assert not load_script("check_website").check(destination)["ok"]


def make_assets(path):
    version = "7.0.0rc1"
    names = [f"gncore-{version}-py3-none-any.whl", f"gncore-{version}.tar.gz", f"gncore-{version}-skills.zip"]
    with ZipFile(path / names[0], "w") as archive:
        archive.writestr("gncore/version.py", f'__version__ = "{version}"\n')
    for name in names[1:]:
        (path / name).write_bytes(b"fixture")
    (path / "SHA256SUMS").write_text("".join(hashlib.sha256((path / name).read_bytes()).hexdigest()+"  "+name+"\n" for name in names))
    return names


def test_release_verifier_detects_modified_bytes_and_unexpected_inventory(tmp_path):
    verifier = load_script("verify_release_assets")
    names = make_assets(tmp_path)
    assert set(verifier.verify(tmp_path, "7.0.0rc1")) == set(names)
    (tmp_path / names[1]).write_bytes(b"changed artifact")
    with pytest.raises(ValueError, match="checksum mismatch"):
        verifier.verify(tmp_path, "7.0.0rc1")
    (tmp_path / "SHA256SUMS").write_text("0"*64+"  ../outside\n")
    with pytest.raises(ValueError, match="invalid"):
        verifier.verify(tmp_path, "7.0.0rc1")
