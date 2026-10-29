"""Reporting must never silently convert missing evidence to success."""
import importlib.util
import json
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[1]

@pytest.mark.skipif(not (ROOT/"benchmarks/comparison/rubrics.json").exists(),reason="Repository comparison evidence is intentionally excluded from the source distribution")
def test_review_files_cover_saved_answers_and_frozen_checks():
    rubrics = {x["id"]: {c["id"] for c in x["checks"]} for x in json.loads((ROOT/"benchmarks/comparison/rubrics.json").read_text(encoding="utf-8"))}
    for path in (ROOT/"benchmarks/comparison").glob("*review-notes.json"):
        for run, notes in json.loads(path.read_text(encoding="utf-8"))["reviews"].items():
            answers = json.loads((ROOT/"web-results/comparison/runs"/run/"response.json").read_text(encoding="utf-8"))["answers"]
            assert set(notes) == {a["id"] for a in answers}
            for case, note in notes.items():
                assert set(note["fail"]) <= rubrics[case]
                assert set(note.get("pending", [])) <= rubrics[case]
                assert note["basis"].strip()
                assert all(isinstance(reason,str) and reason.strip() for reason in note["fail"].values())

def test_guidance_application_retains_existing_frontend_modes():
    catalog = json.loads((ROOT/"catalog/categories.json").read_text(encoding="utf-8"))
    frontend = next(x for x in catalog["categories"] if x["id"]=="web-frontend")
    assert "## Available visual modes" in frontend["extra"]
    assert "## Anticipate failure and verify the boundary" in frontend["extra"]
    assert "Scrollytelling" in frontend["extra"]
