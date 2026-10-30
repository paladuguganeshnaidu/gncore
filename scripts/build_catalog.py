"""Offline deterministic build from versioned authoring inputs and references."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src/gncore/skills/unified_data"


def sha(content):
    return hashlib.sha256(content).hexdigest()


def document(entry, version):
    lines = ["---", f"name: {entry['id']}", f"description: {json.dumps(entry['description'], ensure_ascii=False)}",
             f"license: {' AND '.join(entry['licenses'])}", "---", "", f"# {entry['title']}", "",
             f"Version: {version}", "", "## Choose the work", "", entry["decisions"], "",
             "Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.", "",
             "Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.", "",
             "Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.", "",
             "## Deliver and verify", "", entry["deliverable"], "", entry["verification"], "",
             "Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful."]
    if entry.get("extra"):
        lines.extend(["", entry["extra"].strip()])
    if entry.get("completion_checks"):
        lines.extend(["", "## Critical completion checks", "", "Apply the checks relevant to this task; do not introduce unrelated work.", ""])
        lines.extend("- " + check for check in entry["completion_checks"])
    lines.extend(["", "## Workflow map", "", "| Workflow | Use it for |", "| --- | --- |"])
    for workflow in entry["workflows"]:
        lines.append(f"| `{workflow['id']}` | {workflow['description'].replace('|', chr(92)+'|')} |")
    lines.extend(["", "## Selected procedure", "", "Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default."])
    lines.extend(primary_references(entry))
    lines.extend(["", "## Attribution and resource integrity", "",
                  "Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.", "",
                  "See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task."])
    return "\n".join(lines).rstrip() + "\n"


def procedures(entry):
    lines = [f"# {entry['title']}: focused procedures", "", "Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task."]
    for workflow in entry["workflows"]:
        lines.extend(["", f"### {workflow['title']} (`{workflow['id']}`)", "", workflow["procedure"].strip()])
        guide = f"references/{workflow['id']}/UPSTREAM.md"
        if guide in entry["resources"]:
            lines.extend(["", f"Technical reference: [attributed source guide]({guide})."])
    return "\n".join(lines).rstrip() + "\n"


def primary_references(entry):
    lines = []
    if entry["id"] in {"neural-networks", "deep-learning", "computer-vision", "natural-language-processing", "machine-learning", "mlops"}:
        lines.extend(["", "## Primary technical references", "",
                      "Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.", "",
                      "- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)",
                      "- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)",
                      "- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)"])
    if entry["id"] == "neural-networks":
        lines.extend(["", "For a tiny CPU-only gradient and learning probe, run `python scripts/gradient_probe.py` from this skill folder. It checks a synthetic XOR fixture; it does not establish production model quality."])
    return lines


def generated():
    authored = json.loads((ROOT / "catalog/categories.json").read_text(encoding="utf-8"))
    manifest, output, workflow_ids = [], {}, set()
    for entry in sorted(authored["categories"], key=lambda item: item["id"]):
        skill_id = entry["id"]
        for workflow in entry["workflows"]:
            if workflow["id"] in workflow_ids or not workflow["procedure"].strip():
                raise ValueError(f"duplicate or empty workflow: {workflow['id']}")
            workflow_ids.add(workflow["id"])
        resources = set(entry["resources"]) | {"SOURCES.json", "GNCORE-LICENSE", "WORKFLOWS.md"}
        skill_root = DATA / skill_id
        for helper in skill_root.glob("scripts/*.py"):
            if "references" not in helper.parts:
                resources.add(helper.relative_to(skill_root).as_posix())
        sources = {"category": skill_id, "entrypoint_author": "GNCore / Ganesh Naidu", "original_guidance_license": "MIT",
                   "aggregate_licenses": entry["licenses"], "original_categories": entry["original_categories"],
                   "legacy_reference_ids": [w["id"] for w in entry["workflows"] if any(r.startswith(f"references/{w['id']}/") for r in resources)],
                   "review_scope": "Original workflow reference paths preserved; heuristic-only supplemental research retired in phase two. Helper syntax checked separately; installation never executes helpers."}
        local_output = {"SKILL.md": document(entry, authored["version"]).encode("utf-8"),
                        "WORKFLOWS.md": procedures(entry).encode("utf-8"),
                        "SOURCES.json": (json.dumps(sources, indent=2, ensure_ascii=False) + "\n").encode("utf-8"),
                        "GNCORE-LICENSE": (ROOT / "LICENSE").read_bytes()}
        hashes = {}
        for name in sorted(resources):
            content = local_output[name] if name in local_output else (skill_root / name).read_bytes()
            hashes[name] = sha(content)
        output.update({skill_root / name: content for name, content in local_output.items()})
        manifest.append({"id": skill_id, "category": skill_id, "title": entry["title"], "description": entry["description"],
                         "version": authored["version"], "license": " AND ".join(entry["licenses"]), "tags": entry["tags"],
                         "workflows": entry["workflows"], "resources": sorted(resources), "resource_sha256": hashes,
                         "entrypoint_sha256": sha(local_output["SKILL.md"]), "research_references": []})
    output[DATA / "manifest.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    return output, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Compare generated output without writing")
    args = parser.parse_args()
    output, manifest = generated()
    changed = []
    for path, content in output.items():
        if not path.is_file() or path.read_bytes() != content:
            changed.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
    print(json.dumps({"categories": len(manifest), "workflows": sum(len(e["workflows"]) for e in manifest),
                      "mode": "check" if args.check else "build", "changed": changed}, indent=2))
    return 1 if args.check and changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
