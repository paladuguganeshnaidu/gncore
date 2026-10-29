"""Build one adaptive SKILL.md per category with complete workflow coverage."""

from __future__ import annotations

from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

from category_blueprints import CANONICAL_IDS, GUIDES
from research_categories import WORK

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "src/gncore/skills/unified_data"
sys.path.insert(0, str(ROOT / "src"))
from gncore.skills.domains import DOMAIN_SPECS

DOMAIN_FOCUS = {skill_id: focus for _, _, _, specs in DOMAIN_SPECS for skill_id, _, _, focus in specs}
DOMAIN_TITLES = {category: title for category, title, _, _ in DOMAIN_SPECS}


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def copy_file(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def eligible_files(root):
    return [p for p in root.rglob("*") if p.is_file() and not p.is_symlink() and not ({".git", "node_modules", "__pycache__", ".pytest_cache"} & set(p.relative_to(root).parts)) and p.suffix not in {".pyc", ".pyo"}]


def license_review(record, repo_licenses):
    root = Path(record["staged"])
    supplied = dict(record.get("notices", {}))
    repo_notice = repo_licenses.get(record["repository"], {})
    if repo_notice.get("text"):
        supplied["repository-" + Path(repo_notice.get("path") or "LICENSE").name] = repo_notice["text"]
    for file in eligible_files(root):
        if re.fullmatch(r"(licen[cs]e|notice|copying)(\.[^/]*)?", file.name, re.I):
            supplied[file.relative_to(root).as_posix()] = file.read_text(encoding="utf-8-sig", errors="replace")
    declared = str((record.get("metadata") or {}).get("license", ""))
    if re.search(r"proprietary|source.available|non.commercial|research.only|\b[AL]?GPL\b", declared, re.I):
        return [], supplied, "research-only: restrictive or noncommercial declaration"
    text = "\n".join(supplied.values())
    if "GNU GENERAL PUBLIC LICENSE" in text.upper() or "GNU AFFERO GENERAL PUBLIC LICENSE" in text.upper():
        return [], supplied, "research-only: copyleft scope needs separate review"
    licenses = set()
    if re.search(r"MIT License|Permission is hereby granted, free of charge", text, re.I):
        licenses.add("MIT")
    if "Apache License" in text:
        licenses.add("Apache-2.0")
    if "Attribution-ShareAlike 4.0" in text:
        licenses.add("CC-BY-SA-4.0")
    elif "Attribution 4.0 International" in text:
        licenses.add("CC-BY-4.0")
    if "BSD 3-Clause" in text or "Neither the name of" in text and "Redistribution and use in source and binary forms" in text:
        licenses.add("BSD-3-Clause")
    elif "BSD 2-Clause" in text:
        licenses.add("BSD-2-Clause")
    if not licenses:
        return [], supplied, "research-only: redistribution license not verified"
    return sorted(licenses), supplied, "licensed-reference"


def mode_procedure(skill):
    metadata = skill["metadata"]
    skill_id = metadata["skill_id"]
    if skill_id in DOMAIN_FOCUS:
        return DOMAIN_FOCUS[skill_id]
    text = skill["prompt"].split("\nExecution loop:", 1)[0].strip()
    text = re.split(r"\n## (?:Working agreement|Implementation references|Detailed guidance|GNCore execution scope|Skill selection)", text, maxsplit=1)[0]
    text = re.sub(r"^# [^\n]+\n+", "", text)
    text = re.sub(r"^You are GNCore[^\n]*\n+", "", text)
    # Keep the authored task procedure rather than repeating shared scaffolding.
    return text.strip() or metadata["description"]


def source_relevance(category, record):
    text = (record["name"] + " " + str((record.get("metadata") or {}).get("description", ""))).lower()
    if category == "healthcare-operations":
        return bool(re.search(r"healthcare|patient|clinic|hospital|scheduling|medical.billing", text)) and not bool(re.search(r"diagnos|prescrib|treatment.plan", text))
    if category in {"word-documents", "pdf-documents", "presentations-powerpoint", "spreadsheets"}:
        return bool(re.search({"word-documents": r"docx|word.document", "pdf-documents": r"\bpdf\b", "presentations-powerpoint": r"pptx|powerpoint|presentation", "spreadsheets": r"xlsx|spreadsheet|excel"}[category], text))
    tokens = {t for t in category.replace("-", " ").split() if len(t) > 3}
    return bool(tokens & set(re.findall(r"[a-z]+", text))) or category in {"general", "code-engineering", "backend-engineering", "web-frontend"}


def main():
    snapshot = WORK / "legacy-catalog.json"
    if not snapshot.exists():
        from gncore.skills.library import legacy_skills
        write(snapshot, json.dumps([skill.to_dict() for skill in legacy_skills()], indent=2))
    legacy = json.loads(snapshot.read_text(encoding="utf-8"))
    groups = defaultdict(list)
    for skill in legacy:
        groups[skill["metadata"]["category"]].append(skill)
    if set(groups) != set(GUIDES):
        raise ValueError(f"Missing category guidance: {set(groups) ^ set(GUIDES)}")
    research = json.loads((WORK / "candidates.json").read_text(encoding="utf-8"))
    if len(research["searches"]) != 60:
        raise ValueError("All 60 categories must have a recorded search")
    search_by_category = {r["category"]: r for r in research["searches"]}
    downloads = {(r["repository"], r["name"]): r for r in research["downloads"]}
    repo_licenses = {r["repository"]: r for r in research.get("licenses", [])}
    old_bundles = {}
    for directory in ("frontend_data", "backend_data"):
        for entry in json.loads((ROOT / "src/gncore/skills" / directory / "manifest.json").read_text(encoding="utf-8")):
            old_bundles[entry["id"]] = (directory, entry)
    entries, audits = [], []
    for category, skills in sorted(groups.items()):
        skill_id = CANONICAL_IDS.get(category, category)
        target = DESTINATION / skill_id
        title = DOMAIN_TITLES.get(category, category.replace("-", " ").title())
        description, decisions, validation = GUIDES[category]
        sections = [f"# GNCore {title}", "", "## Select the work from the user's intent", "", decisions, "", "Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.", "", "Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.", "", "## Execute and verify", "", "1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.", "2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.", "3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.", "4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.", "5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.", "", "## Category quality criteria", "", validation, "", "Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions."]
        if category == "web-frontend":
            sections.extend(["", (ROOT / "scripts/frontend_playbook.md").read_text(encoding="utf-8").strip()])
        sections.extend(["", "## Workflow map", "", "| Workflow | Use it for |", "| --- | --- |"])
        workflows = []
        licenses = {"MIT"}
        for skill in skills:
            metadata = skill["metadata"]
            workflow_id = metadata["skill_id"]
            sections.append(f"| `{workflow_id}` | {metadata['description'].replace('|', chr(92)+'|')} |")
            workflows.append({"id": workflow_id, "title": metadata["name"], "description": metadata["description"], "procedure": mode_procedure(skill)})
            if workflow_id in old_bundles:
                directory, bundled = old_bundles[workflow_id]
                source_root = ROOT / "src/gncore/skills" / directory / workflow_id
                for name in bundled["resources"]:
                    copy_file(source_root / name, target / "references" / workflow_id / name)
                if bundled.get("repository") == "trailofbits/skills":
                    licenses.add("CC-BY-SA-4.0")
                if any("LICENSE" in name and "Apache License" in (source_root / name).read_text(encoding="utf-8", errors="replace") for name in bundled["resources"] if Path(name).name.upper().startswith(("LICENSE", "UPSTREAM-LICENSE"))):
                    licenses.add("Apache-2.0")
        sections.extend(["", "## Focused procedures"])
        for workflow in workflows:
            sections.extend(["", f"### {workflow['title']} (`{workflow['id']}`)", "", workflow["procedure"]])
            reference = target / "references" / workflow["id"] / "UPSTREAM.md"
            if reference.exists():
                sections.extend(["", f"For task-specific technical depth, read [the attributed source guide](references/{workflow['id']}/UPSTREAM.md) and only the supporting references needed. Resolve its paths from that reference folder. Check tool/runtime availability before using source commands."])
        accepted = []
        seen = set()
        for candidate in search_by_category[category]["candidates"]:
            key = (candidate["source"], candidate.get("skillId") or candidate["name"])
            if key in seen:
                continue
            seen.add(key)
            record = downloads.get(key, {"status": "not-downloaded"})
            audit = {"category": category, "repository": key[0], "name": key[1], "download_status": record["status"], "snapshot_hash": record.get("snapshot_hash"), "revision": record.get("revision"), "source_url": record.get("source_url", f"https://github.com/{key[0]}")}
            if record["status"] == "downloaded-for-review":
                approved, supplied, status = license_review(record, repo_licenses)
                if status == "licensed-reference" and not source_relevance(category, record):
                    status = "research-only: category relevance not established"
                audit.update({"review_status": status, "licenses": approved, "file_count": len(record.get("file_sha256", {}))})
                if status == "licensed-reference":
                    folder = re.sub(r"[^a-zA-Z0-9.-]", "-", key[0] + "-" + key[1])
                    destination = target / "research" / folder
                    relocated = {}
                    for source in eligible_files(Path(record["staged"])):
                        relative = source.relative_to(record["staged"])
                        if relative.name == "SKILL.md":
                            original_path = relative.as_posix()
                            relative = relative.with_name("GUIDE.md")
                            relocated[original_path] = relative.as_posix()
                        copy_file(source, destination / relative)
                    if relocated:
                        write(destination / "RESOURCE_PATHS.json", json.dumps(relocated, indent=2))
                    for number, (origin, text) in enumerate(supplied.items(), 1):
                        write(destination / "notices" / f"{number}-{Path(origin).name}", text)
                    write(destination / "SOURCE.json", json.dumps(audit, indent=2))
                    licenses.update(approved)
                    accepted.append({**audit, "guide": f"research/{folder}/GUIDE.md"})
            else:
                audit["review_status"] = "not-redistributed: download unavailable"
            audits.append(audit)
        research_root = target / "research"
        accepted_folders = {Path(source["guide"]).parent.name for source in accepted}
        if research_root.exists():
            for folder in research_root.iterdir():
                if folder.is_dir() and folder.name not in accepted_folders:
                    resolved_source = folder.resolve()
                    quarantine = (WORK / "excluded-from-distribution" / skill_id / folder.name).resolve()
                    if not resolved_source.is_relative_to(DESTINATION.resolve()) or not quarantine.is_relative_to(WORK.resolve()):
                        raise ValueError("Research quarantine path escaped its intended root")
                    quarantine.parent.mkdir(parents=True, exist_ok=True)
                    if quarantine.exists():
                        quarantine = quarantine.with_name(quarantine.name + "-" + hashlib.sha256(str(resolved_source).encode()).hexdigest()[:8])
                    shutil.move(str(resolved_source), str(quarantine))
        if accepted:
            sections.extend(["", "## Additional reviewed references", "", "These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.", ""])
            for source in accepted:
                sections.append(f"- [{source['repository']} / {source['name']}]({source['guide']}): {', '.join(source['licenses'])}.")
        sections.extend(["", "## Attribution and use", "", "GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.", "", "See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task."])
        expression = " AND ".join(sorted(licenses))
        body = "\n".join(sections)
        write(target / "SKILL.md", f"---\nname: {skill_id}\ndescription: {json.dumps(description, ensure_ascii=False)}\nlicense: {expression}\n---\n\n{body}")
        write(target / "SOURCES.json", json.dumps({"category": category, "entrypoint_author": "GNCore / Ganesh Naidu", "entrypoint_original_text_license": "MIT", "aggregate_licenses": sorted(licenses), "research": [a for a in audits if a["category"] == category], "legacy_reference_ids": [w["id"] for w in workflows if w["id"] in old_bundles]}, indent=2))
        copy_file(ROOT / "LICENSE", target / "GNCORE-LICENSE")
        # A previous build can leave nested source entrypoints. Preserve their
        # bytes as references without exposing additional discoverable skills.
        for nested in target.rglob("SKILL.md"):
            if nested != target / "SKILL.md":
                destination = nested.with_name("SOURCE-ENTRYPOINT.md")
                nested.rename(destination)
        resources = sorted(p.relative_to(target).as_posix() for p in eligible_files(target) if p.name != "SKILL.md")
        entry = {"id": skill_id, "category": category, "title": f"GNCore {title}", "description": description, "version": "6.0.0", "license": expression, "tags": [category, "adaptive", "merged-workflows"], "workflows": workflows, "resources": resources, "research_references": accepted}
        entries.append(entry)
        print(f"Built {skill_id}: {len(workflows)} workflows, {len(accepted)} new references", flush=True)
    write(DESTINATION / "manifest.json", json.dumps(entries, indent=2, ensure_ascii=False))
    report = {"date": "2026-10-28", "categories_searched": len(research["searches"]), "distinct_candidates": len(research["downloads"]), "downloaded_candidates": sum(r["status"] == "downloaded-for-review" for r in research["downloads"]), "category_reviews": audits}
    write(ROOT / "docs/SOURCE_RESEARCH.json", json.dumps(report, indent=2))
    lines = ["# Category source research", "", "Search and download outcomes are recorded separately from license and relevance decisions. A downloaded candidate is not automatically incorporated. Restricted or unclear-license material stays in ignored local research storage.", "", f"Categories searched: **{report['categories_searched']}**. Distinct candidates: **{report['distinct_candidates']}**. Downloaded candidates: **{report['downloaded_candidates']}**.", "", "| Category | Candidates reviewed | Included references |", "| --- | --- | --- |"]
    for entry in entries:
        lines.append(f"| `{entry['category']}` | {len([a for a in audits if a['category'] == entry['category']])} | {len(entry['research_references'])} |")
    lines.extend(["", "Detailed source identities, immutable snapshot hashes or revisions, and exclusion reasons are in [SOURCE_RESEARCH.json](SOURCE_RESEARCH.json). Existing frontend and backend source guides retain their earlier pinned provenance in each reference folder.", "", "GNCore's new prose is MIT-licensed where independently authored. Bundled and adapted content retains its applicable MIT, Apache, Creative Commons, BSD, or other verified license terms. A project license does not erase third-party obligations."])
    write(ROOT / "docs/SOURCE_RESEARCH.md", "\n".join(lines))
    print(f"Built {len(entries)} unified categories covering {sum(len(e['workflows']) for e in entries)} existing workflows")


if __name__ == "__main__":
    main()
