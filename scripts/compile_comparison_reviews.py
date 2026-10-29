"""Compile explicit manual decisions and executed logs; never guess missing scores."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "web-results/comparison"
UI_KEYS = {"initially_disabled", "invalid_email_disabled", "valid_inputs_enable", "selected_values_confirmation", "radio_focus_visible", "narrow_no_overflow"}

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def compile_reviews():
    rubrics = {x["id"]: x for x in read(ROOT / "benchmarks/comparison/rubrics.json")}
    result = []
    for notes_path in sorted((ROOT / "benchmarks/comparison").glob("*review-notes.json")):
        for run_id, notes in read(notes_path)["reviews"].items():
            folder = DEST / "runs" / run_id
            response_path = folder / "response.json"
            if not response_path.exists():
                raise ValueError(f"Review without saved response: {run_id}")
            response = read(response_path)
            answers = {a["id"]: a for a in response["answers"]}
            assert set(notes) == set(answers), (run_id, set(answers)-set(notes))
            cases = []
            for case_id, note in sorted(notes.items()):
                rubric = rubrics[case_id]
                failure = dict(note["fail"])
                pending = set(note.get("pending", []))
                na = {}
                # These conditional rubric items are inapplicable to the supplied
                # read-only feed / hand-alignment development tasks, in ALL arms.
                if case_id == "D20":
                    na["c5"] = "Read-only feed; no user mutation or remote write/retry identity requested."
                if case_id == "D21":
                    na["c4"] = "Hand-alignment example supplies no training/evaluation dataset to split."
                if case_id == "H14":
                    na["c4"] = "The supplied stale-writer fixture has no remote side effect or unknown remote outcome."
                ui_path = folder / f"{case_id}-browser.json"
                ui = read(ui_path) if ui_path.exists() else None
                if ui and rubric["category"] == "web-frontend":
                    by_name = {c["name"]: c for c in ui["checks"]}
                    required = {"c2": [], "c3": ["initially_disabled", "invalid_email_disabled", "valid_inputs_enable"],
                                "c4": ["selected_values_confirmation"], "c5": ["radio_focus_visible"], "c6": ["narrow_no_overflow"]}
                    for criterion, names in required.items():
                        if all(name in by_name for name in names):
                            pending.discard(criterion)
                            if not all(by_name[name]["passed"] for name in names):
                                failure[criterion] = "; ".join(by_name[n].get("evidence", n+" failed") for n in names if not by_name[n]["passed"])
                    # Labels, exact controls and offline structure were inspected
                    # in source and real AX snapshots before each browser journey.
                checks = []
                for check in rubric["checks"]:
                    key = check["id"]
                    status = "not-applicable" if key in na else "not-measured" if key in pending else "fail" if key in failure else "pass"
                    checks.append({**check, "status": status, "evidence": na.get(key) or failure.get(key) or note["basis"]})
                measured = [c for c in checks if c["status"] in {"pass", "fail"}]
                case = {"id": case_id, "category": rubric["category"], "checks": checks,
                        "passed": sum(c["status"] == "pass" for c in measured), "total": len(measured),
                        "complete": not pending, "review_note": note["basis"]}
                if ui:
                    selected = [c for c in ui["checks"] if c["name"] in UI_KEYS]
                    assert len(selected) == len({c["name"] for c in selected})
                    case["browser"] = {"passed": sum(c["passed"] for c in selected), "total": len(selected), "evidence": ui_path.relative_to(ROOT).as_posix()}
                artifact_path = folder / f"{case_id}-tests.json"
                if artifact_path.exists():
                    artifact = read(artifact_path)
                    case["execution"] = {k: artifact.get(k) for k in ("passed", "total", "error", "compute_seconds")}
                    case["execution"]["evidence"] = artifact_path.relative_to(ROOT).as_posix()
                if rubric["category"] == "cybersecurity":
                    findings = answers[case_id]["findings"]
                    prefix = "S" if case_id.startswith("D") else "H"
                    seeded = {f"{prefix}{i}" for i in range(1,7)}
                    controls = {f"{('C' if prefix=='S' else 'K')}{i}" for i in range(1,5)}
                    # Correct identification/repair was manually reviewed above.
                    ids = {f["id"] for f in findings}
                    case["security"] = {"found": len(ids & seeded), "seeded": 6,
                                        "safe_controls_flagged": len(ids & controls), "safe_controls": 4,
                                        "repairs_passed": case["passed"], "repairs_total": case["total"],
                                        "method": "Manual fixture review; exploits not executed."}
                cases.append(case)
            result.append({"run": run_id, "host": run_id.split("-",1)[0], "profile": response["benchmark_run"].rsplit("-",1)[0],
                           "split": response["benchmark_run"].rsplit("-",1)[1], "cases": cases,
                           "response_sha256": hashlib.sha256(response_path.read_bytes()).hexdigest(),
                           "review_notes": notes_path.relative_to(ROOT).as_posix(), "review_method": "Manual, unblinded, single evaluator; not an independent audit."})
    output = {"schema_version": 1, "runs": result, "target_percent": 95,
              "interpretation": "Percentage of applicable task checks, not universal efficiency, security assurance or company ranking. Missing results remain unmeasured."}
    (DEST / "review-results.json").write_text(json.dumps(output, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps([{"run": r["run"], "reviewed": len(r["cases"]), "complete": sum(c["complete"] for c in r["cases"])} for r in result], indent=2))
    return output

if __name__ == "__main__":
    compile_reviews()
