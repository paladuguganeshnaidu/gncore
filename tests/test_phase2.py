import importlib.util
import json
from pathlib import Path
import subprocess
import sys

import pytest

from gncore import GncoreCli
from gncore.audit import audit_catalog
from gncore.installation import install_skills, verify_installation
from gncore.routing import context_from_file, route_task


@pytest.mark.parametrize(("brief", "category"), [
    ("Check gradients in a neural network", "neural-networks"), ("Use mixed precision", "deep-learning"),
    ("Image segmentation", "computer-vision"), ("Fix token alignment", "natural-language-processing"),
    ("Monitor model drift", "mlops"), ("Train a churn classifier", "machine-learning"),
    ("Evaluate RAG retrieval", "ai-engineering"), ("Build a landing page", "web-frontend"),
    ("Implement a FastAPI endpoint", "web-backend"), ("Refactor a function", "code-build"),
    ("Specify a user flow", "design-ux"), ("Build a Python package", "python"),
    ("Design a CLI", "developer-tools"), ("Write an API reference", "documentation"),
    ("Design integration tests", "testing"), ("Perform a security audit", "cybersecurity"),
    ("Review Kubernetes rollout", "cloud-devops-sre"), ("Prepare a release candidate", "release-engineering"),
    ("Automate a repetitive script", "automation"), ("Create an Android mobile app", "mobile-development"),
    ("Make a playable game", "game-development"), ("Repair an ETL data pipeline", "data-engineering"),
    ("Check join fanout", "data-science"), ("Review a Postgres query plan", "databases"),
    ("Define a Rust FFI ABI", "systems-programming"), ("Fix firmware timer wraparound", "embedded-systems"),
    ("Profile tail latency", "performance-engineering"), ("Propagate trace context", "observability"),
    ("Plan a paper reproduction", "developer-research"), ("Design a message queue retry budget", "distributed-systems"),
])
def test_developer_routing_is_explainable_across_every_category(brief, category):
    result = route_task(brief)
    assert result["skill_id"] == category
    assert result["status"] == "suggested"
    assert result["alternatives"][0]["matched"]


def test_routing_abstains_and_explicit_choices_override_preferences(tmp_path):
    assert route_task("Write a wedding speech")["status"] == "needs-context"
    assert route_task("Build a website and mobile app")["status"] == "ambiguous"
    path = tmp_path / "project.json"
    path.write_text(json.dumps({"stack": "Python", "preferred_skills": ["web-frontend"]}))
    context = context_from_file(path)
    assert route_task("Build a website", skill_id="neural-networks", context=context)["skill_id"] == "neural-networks"
    path.write_text(json.dumps({"api_key": "do-not-echo-me"}))
    with pytest.raises(ValueError, match="permits") as error:
        context_from_file(path)
    assert "do-not-echo-me" not in str(error.value)


def test_active_catalog_audit_checks_all_procedures_hashes_links_and_helpers():
    report = audit_catalog()
    assert report["ok"], report["issues"]
    assert report["categories"] == 30 and report["workflows"] == 374
    assert report["resources_verified"] == 1660
    assert report["python_helpers_parsed"] == 73
    assert report["baseline_workflows_accounted"] == 553


def test_packaged_resource_corruption_is_detected_before_export(tmp_path, monkeypatch):
    import gncore.skills.bundles as bundles
    root = tmp_path / "unified_data/example"
    root.mkdir(parents=True)
    (root / "sample.txt").write_bytes(b"tampered")
    monkeypatch.setattr(bundles, "files", lambda package: tmp_path)
    monkeypatch.setattr(bundles, "bundle_manifest", lambda directory: ({"id": "example", "resources": ["sample.txt"], "resource_sha256": {"sample.txt": "0" * 64}},))
    with pytest.raises(ValueError, match="digest mismatch"):
        bundles.bundle_resources("unified_data", "example")


def test_retirement_removes_only_pristine_tracked_skills_and_preserves_backup(tmp_path):
    root = tmp_path / "skills"
    initial = {"retired": {"SKILL.md": b"old"}, "customized": {"SKILL.md": b"original"}}
    install_skills(root, initial, version="6")
    (root / "customized/SKILL.md").write_bytes(b"user edit")
    result = install_skills(root, {"new": {"SKILL.md": b"new"}}, version="7", retire={"retired", "customized"})
    assert result["retire"] == ["retired"] and result["preserved_retired"] == ["customized"]
    assert not (root / "retired").exists()
    assert (Path(result["backup"]) / "retired/SKILL.md").read_bytes() == b"old"
    assert (root / "customized/SKILL.md").read_bytes() == b"user edit"


def probe_module():
    path = Path(__file__).resolve().parents[1] / "src/gncore/skills/unified_data/neural-networks/scripts/gradient_probe.py"
    spec = importlib.util.spec_from_file_location("gncore_gradient_probe", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_neural_network_gradient_probe_and_tiny_batch_learning():
    module = probe_module()
    parameters = module.initial_parameters()
    original = parameters.copy()
    assert module.gradient_error(parameters) < 1e-5
    assert parameters == original  # Numerical probes must restore the model.
    report = module.train()
    assert report["passed"] and report["final_loss"] < report["initial_loss"] / 10
    assert [p >= 0.5 for p in report["predictions"]] == [False, True, True, False]


def test_tiny_sgd_checkpoint_roundtrip_preserves_continuation():
    module = probe_module()
    def run(parameters, steps):
        for _ in range(steps):
            gradient = module.loss_and_gradient(parameters)[1]
            parameters = [p-0.7*g for p, g in zip(parameters, gradient)]
        return parameters
    uninterrupted = run(module.initial_parameters(), 200)
    checkpoint = json.loads(json.dumps({"step": 100, "parameters": run(module.initial_parameters(), 100)}))
    resumed = run(checkpoint["parameters"], 200-checkpoint["step"])
    assert resumed == uninterrupted
    with pytest.raises(ValueError, match="17 finite"):
        module.loss_and_gradient([float("nan")] * 17)


def test_offline_catalog_and_evaluation_builds_are_reproducible():
    root = Path(__file__).resolve().parents[1]
    for script in ("build_catalog.py", "build_evaluations.py"):
        result = subprocess.run([sys.executable, str(root / "scripts" / script), "--check"], cwd=root, capture_output=True, text=True, encoding="utf-8", timeout=60)
        assert result.returncode == 0, result.stdout + result.stderr


def test_route_cli_and_invalid_pruning_are_actionable(capsys, tmp_path):
    cli = GncoreCli()
    assert cli.run(["route", "Build a neural network"]) == 0
    assert json.loads(capsys.readouterr().out)["skill_id"] == "neural-networks"
    assert cli.run(["export", "--specific", "python", "--prune-retired", "--directory", str(tmp_path)]) == 2
    assert "requires --all" in capsys.readouterr().err
    assert list(tmp_path.iterdir()) == []
