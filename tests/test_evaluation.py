import copy
import json

import pytest

from gncore import GncoreCli
from gncore.evaluation import evaluate_response, load_corpus, validate_corpus


def test_corpus_covers_every_developer_category_with_three_real_scenarios_each():
    corpus = load_corpus()
    assert corpus["scope"] == "developer-catalog"
    assert len(corpus["categories"]) == 30 and len(corpus["cases"]) == 90
    assert len({case["prompt"] for case in corpus["cases"]}) == 90
    assert {case["kind"] for case in corpus["cases"]} == {"normal", "underspecified", "boundary"}


@pytest.mark.parametrize("mutation", ["duplicate", "missing-kind", "unknown-workflow", "unsafe-artifact", "missing-rubric"])
def test_invalid_corpus_cannot_be_reported_as_valid(mutation):
    corpus = copy.deepcopy(load_corpus())
    if mutation == "duplicate":
        corpus["cases"].append(corpus["cases"][0])
    elif mutation == "missing-kind":
        corpus["cases"].pop()
    elif mutation == "unknown-workflow":
        corpus["cases"][0]["workflows"] = ["not-a-real-workflow"]
    elif mutation == "unsafe-artifact":
        corpus["cases"][0]["artifact"] = "../escape"
    else:
        corpus["cases"][0]["human_review"] = []
    with pytest.raises(ValueError):
        validate_corpus(corpus)


def test_artifact_structure_pass_does_not_claim_semantic_or_tool_validation(tmp_path):
    case = next(c for c in load_corpus()["cases"] if c["id"] == "frontend-normal")
    (tmp_path / case["artifact"]).write_text("A file exists; this is not a finished booking page.")
    response = {"case_id": case["id"], "categories": [case["category"]], "workflows": case["workflows"], "decisions": case["decisions"]}
    report = evaluate_response(case, response, tmp_path)
    assert report["objective_passed"]
    assert report["quality_status"] == "pending-review"
    assert report["human_review"]["status"] == "pending"
    assert report["tool_checks"]["status"] == "not-run"


def test_missing_artifact_wrong_category_and_wrong_constraint_fail(tmp_path):
    case = next(c for c in load_corpus()["cases"] if c["id"] == "frontend-normal")
    response = {"case_id": case["id"], "categories": ["web-backend"], "workflows": [], "decisions": {"motion": "animated"}}
    report = evaluate_response(case, response, tmp_path)
    assert not report["objective_passed"]
    assert not any(check["passed"] for check in report["objective"])


def test_response_mismatch_and_bad_shape_are_actionable_errors(tmp_path):
    case = load_corpus()["cases"][0]
    with pytest.raises(ValueError, match="case_id"):
        evaluate_response(case, {}, tmp_path)
    with pytest.raises(ValueError, match="list"):
        evaluate_response(case, {"case_id": case["id"], "categories": "web-frontend"}, tmp_path)


def test_evaluation_cli_validates_and_reports_pending_reviews(tmp_path, capsys):
    cli = GncoreCli()
    assert cli.run(["evaluate", "--validate"]) == 0
    assert json.loads(capsys.readouterr().out) == {"schema_version": 1, "scope": "developer-catalog", "categories": 30, "cases": 90, "valid": True}
    case = next(c for c in load_corpus()["cases"] if c["id"] == "frontend-normal")
    response = tmp_path / "response.json"
    response.write_text(json.dumps({"case_id": case["id"], "categories": [case["category"]], "workflows": case["workflows"], "decisions": case["decisions"]}))
    args = ["evaluate", "--case", case["id"], "--response", str(response), "--artifacts", str(tmp_path)]
    assert cli.run(args) == 1
    assert not json.loads(capsys.readouterr().out)["objective_passed"]
    (tmp_path / case["artifact"]).write_text("prototype placeholder")
    assert cli.run(args) == 0
    assert json.loads(capsys.readouterr().out)["quality_status"] == "pending-review"
    assert cli.run(["evaluate", "--case", "bad"]) == 2
    assert "requires" in capsys.readouterr().err


def test_directory_export_dry_run_and_verify_cli(tmp_path, capsys):
    root = tmp_path / "skills"
    cli = GncoreCli()
    args = ["export", "--specific", "game-development", "--directory", str(root)]
    assert cli.run([*args, "--dry-run"]) == 0
    assert json.loads(capsys.readouterr().out)["install"] == ["game-development"]
    assert not root.exists()
    assert cli.run(args) == 0
    capsys.readouterr()
    assert cli.run(["verify", "--directory", str(root)]) == 0
    assert json.loads(capsys.readouterr().out)["ok"]
    (root / "game-development/SKILL.md").write_text("custom edit")
    assert cli.run(["verify", "--directory", str(root)]) == 1
    assert json.loads(capsys.readouterr().out)["modified"] == ["game-development/SKILL.md"]
