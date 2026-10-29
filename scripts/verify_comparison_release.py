"""Verify installed candidate artifacts against the reviewed source; never upload."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys
import tarfile
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--installed", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    release = args.directory.resolve()
    installed = args.installed.resolve()
    sys.path.insert(0, str(installed))
    import gncore
    from gncore.audit import audit_catalog
    from gncore.installation import verify_installation
    from gncore.skills.bundles import packaged_resources
    from gncore.skills.unified import unified_manifest

    assert Path(gncore.__file__).resolve().is_relative_to(installed)
    version = gncore.__version__
    wheel = release / f"gncore-{version}-py3-none-any.whl"
    sdist = release / f"gncore-{version}.tar.gz"
    matched_code = 0
    with ZipFile(wheel) as archive, tarfile.open(sdist) as source:
        for path in (ROOT / "src/gncore").rglob("*.py"):
            if "__pycache__" in path.parts:
                continue
            relative = path.relative_to(ROOT / "src").as_posix()
            assert archive.read(relative) == path.read_bytes(), relative
            assert source.extractfile(f"gncore-{version}/src/" + relative).read() == path.read_bytes(), relative
            matched_code += 1
        assert "gncore = gncore.cli.app:main" in archive.read(f"gncore-{version}.dist-info/entry_points.txt").decode()
    audit = audit_catalog()
    assert audit["ok"], audit
    assert len(gncore.builtin_skills()) == 30 and len(gncore.list_workflows()) == 374
    project = release / "clean-project/.agents/skills"
    assert gncore.GncoreCli().run(["export", "--all", "--directory", str(project)]) == 0
    portable = release / f"gncore-{version}-skills.zip"
    assert gncore.GncoreCli().run(["export", "--all", "--output", str(portable)]) == 0
    resources = 0
    with ZipFile(portable) as archive:
        for entry in unified_manifest():
            category = entry["id"]
            content = gncore.render_skill(gncore.get_skill(category)).encode("utf-8")
            assert archive.read(category + "/SKILL.md") == content
            assert (project / category / "SKILL.md").read_bytes() == content
            assert (ROOT / ".agents/skills" / category / "SKILL.md").read_bytes() == content
            # The CLI adds a metadata wrapper to the stored guide when exporting.
            # Compare stored bytes with stored bytes, and rendered exports above.
            assert (ROOT / "src/gncore/skills/unified_data" / category / "SKILL.md").read_bytes() == (installed / "gncore/skills/unified_data" / category / "SKILL.md").read_bytes()
            for name, data in packaged_resources(category).items():
                assert archive.read(category + "/" + name) == data
                assert (project / category / name).read_bytes() == data
                assert (ROOT / ".agents/skills" / category / name).read_bytes() == data
                assert (ROOT / "src/gncore/skills/unified_data" / category / name).read_bytes() == data
                resources += 1
    verification = verify_installation(project)
    assert verification["ok"], verification
    artifacts = {p.name: {"sha256": hashlib.sha256(p.read_bytes()).hexdigest(), "bytes": p.stat().st_size} for p in (wheel, sdist, portable)}
    (release / "SHA256SUMS").write_text("".join(record["sha256"] + "  " + name + "\n" for name, record in artifacts.items()), encoding="utf-8")
    record = {"version": version, "categories": 30, "workflows": 374, "resources_compared": resources,
              "python_source_files_matched": matched_code, "installed_files": verification["files"],
              "installed_import_verified": True, "project_entrypoints_match_final_rendered_export": True,
              "packaged_entrypoints_match_source_bytes": True,
              "audit": audit, "artifacts": artifacts, "publication": "held"}
    args.report.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
