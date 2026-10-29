"""Read-only catalog, merge, hash, link and helper-syntax audit."""

import ast
from collections import Counter
import hashlib
import re
from urllib.parse import unquote

from gncore.skills.bundles import packaged_resources
from gncore.skills.library import builtin_skills, migration_manifest, validate_skill_definition
from gncore.skills.unified import unified_manifest


def audit_catalog() -> dict:
    entries = unified_manifest()
    ids = [w["id"] for entry in entries for w in entry["workflows"]]
    duplicate_ids = [name for name, count in Counter(ids).items() if count > 1]
    duplicate_procedures = [count for count in Counter(w["procedure"].strip() for entry in entries for w in entry["workflows"]).values() if count > 1]
    issues, resource_count, helper_count = [], 0, 0
    skills = {s.metadata.skill_id: s for s in builtin_skills()}
    for entry in entries:
        name, declared = entry["id"], set(entry["resources"])
        skill = skills[name]
        issues.extend(f"{name}: {issue}" for issue in validate_skill_definition(skill))
        resources = packaged_resources(name)  # Includes declared digest checks.
        resource_count += len(resources)
        for workflow in entry["workflows"]:
            if workflow["procedure"].strip() not in skill.prompt or f"`{workflow['id']}`" not in skill.prompt:
                issues.append(f"missing merged procedure: {name}/{workflow['id']}")
        for target in re.findall(r"\]\(([^)]+)\)", skill.prompt):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative not in declared and relative != "SKILL.md":
                issues.append(f"broken entrypoint resource link: {name}/{relative}")
        for path, raw in resources.items():
            if path.endswith(".py"):
                helper_count += 1
                try:
                    ast.parse(raw.decode("utf-8-sig"), filename=f"{name}/{path}")
                except (SyntaxError, UnicodeError) as error:
                    issues.append(f"helper syntax: {name}/{path}: {error}")
        if set(entry.get("resource_sha256", {})) != declared:
            issues.append(f"incomplete digest inventory: {name}")
    ledger = migration_manifest()["workflows"]
    if len(ledger) != 553 or len({w["id"] for w in ledger}) != len(ledger):
        issues.append("phase-one migration accounting is incomplete")
    targets = {entry["id"] for entry in entries}
    owners = {w["id"]: (entry["id"], w["procedure"]) for entry in entries for w in entry["workflows"]}
    for item in ledger:
        if item["target"] is not None:
            owner, procedure = owners.get(item["id"], (None, ""))
            if owner != item["target"] or item["target"] not in targets:
                issues.append(f"unaccounted retained workflow: {item['id']}")
            if hashlib.sha256(procedure.encode()).hexdigest() != item.get("procedure_sha256"):
                issues.append(f"unexpected merged procedure change: {item['id']}")
    issues.extend(f"duplicate workflow ID: {name}" for name in duplicate_ids)
    if duplicate_procedures:
        issues.append(f"shared procedure text remains in {len(duplicate_procedures)} groups")
    return {"ok": not issues, "categories": len(entries), "workflows": len(ids), "resources_verified": resource_count,
            "python_helpers_parsed": helper_count, "baseline_workflows_accounted": len(ledger),
            "retired_workflows": sum(w["target"] is None for w in ledger), "issues": issues,
            "limits": "Hash/link/procedure and syntax checks; imported helpers were not executed, and arbitrary AI output quality is not certified."}
