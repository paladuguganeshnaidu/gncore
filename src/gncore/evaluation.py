"""Offline scenario validation and artifact checks; never executes supplied code."""

from __future__ import annotations

from importlib.resources import files
import json
from pathlib import Path, PurePosixPath

from gncore.skills.unified import unified_manifest

KINDS = {"normal", "underspecified", "boundary"}


def load_corpus(path: Path | None = None) -> dict:
    text = path.read_text(encoding="utf-8") if path else files("gncore").joinpath("evaluation_cases.json").read_text(encoding="utf-8")
    corpus = json.loads(text)
    validate_corpus(corpus)
    return corpus


def validate_corpus(corpus: dict) -> None:
    """Validate coverage and references against this installed catalog."""
    catalog = {entry["id"]: {workflow["id"] for workflow in entry["workflows"]} for entry in unified_manifest()}
    if not isinstance(corpus, dict) or corpus.get("schema_version") != 1 or not isinstance(corpus.get("cases"), list):
        raise ValueError("invalid evaluation corpus schema")
    categories = corpus.get("categories")
    if not isinstance(categories, list) or not all(isinstance(v, str) for v in categories) or len(categories) != len(set(categories)) or not categories or not set(categories) <= catalog.keys():
        raise ValueError("invalid evaluation categories")
    seen, covered = set(), set()
    for case in corpus["cases"]:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"] or case["id"] in seen:
            raise ValueError("evaluation case IDs must be nonempty and unique")
        seen.add(case["id"])
        category, kind = case.get("category"), case.get("kind")
        if not isinstance(category, str) or not isinstance(kind, str) or category not in categories or kind not in KINDS or (category, kind) in covered:
            raise ValueError(f"invalid or repeated category/kind: {case['id']}")
        covered.add((category, kind))
        for field in ("prompt", "context", "artifact", "verification"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                raise ValueError(f"missing {field}: {case['id']}")
        _artifact_path(case["artifact"])
        if not isinstance(case.get("workflows"), list) or not case["workflows"] or not all(isinstance(v, str) for v in case["workflows"]) or not set(case["workflows"]) <= catalog[category]:
            raise ValueError(f"unknown expected workflow: {case['id']}")
        for field in ("properties", "prohibited", "human_review"):
            if not isinstance(case.get(field), list) or not case[field] or not all(isinstance(v, str) and v.strip() for v in case[field]):
                raise ValueError(f"missing {field} rubric: {case['id']}")
        expected = case.get("decisions", {})
        if not isinstance(expected, dict) or not all(isinstance(k, str) and k for k in expected):
            raise ValueError(f"invalid expected decisions: {case['id']}")
    required = {(category, kind) for category in categories for kind in KINDS}
    if covered != required:
        raise ValueError("each evaluation category requires normal, underspecified, and boundary scenarios")


def _artifact_path(name: str) -> PurePosixPath:
    path = PurePosixPath(name)
    if not name or path.is_absolute() or any(part in {".", "..", ""} for part in name.split("/")) or "\\" in name or ":" in name:
        raise ValueError(f"unsafe evaluation artifact path: {name}")
    return path


def evaluate_response(case: dict, response: dict, artifact_root: Path) -> dict:
    """Check recorded selection/decisions and a real artifact's presence.

    These are necessary structural conditions, not semantic grading. Review of
    artifact properties and prohibited behavior remains explicitly pending.
    """
    if not isinstance(response, dict) or response.get("case_id") != case["id"]:
        raise ValueError("response case_id does not match the requested scenario")
    for field in ("categories", "workflows"):
        if not isinstance(response.get(field), list) or not all(isinstance(v, str) for v in response[field]):
            raise ValueError(f"response {field} must be a list of IDs")
    if not isinstance(response.get("decisions", {}), dict):
        raise ValueError("response decisions must be an object")
    root = artifact_root.expanduser().resolve()
    relative = _artifact_path(case["artifact"])
    target = root.joinpath(*relative.parts)
    if not target.resolve().is_relative_to(root):
        raise ValueError("evaluation artifact escapes the supplied directory")
    objective = [
        {"id": "category", "passed": case["category"] in response["categories"]},
        {"id": "workflow", "passed": bool(set(case["workflows"]) & set(response["workflows"]))},
        {"id": "artifact-present", "passed": target.is_file() and target.stat().st_size > 0, "path": case["artifact"]},
    ]
    for name, expected in case.get("decisions", {}).items():
        actual = response.get("decisions", {}).get(name)
        objective.append({"id": f"decision:{name}", "passed": actual == expected and type(actual) is type(expected), "expected": expected, "actual": actual})
    return {
        "case_id": case["id"], "objective": objective,
        "objective_passed": all(check["passed"] for check in objective),
        "human_review": {"status": "pending", "questions": case["human_review"], "artifact_properties": case["properties"], "prohibited": case["prohibited"]},
        "tool_checks": {"status": "not-run", "required_evidence": case["verification"]},
        "quality_status": "pending-review",
    }
