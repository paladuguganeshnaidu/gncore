"""Build the full developer scenario corpus from versioned authoring inputs."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "catalog"))
from evaluation_specs import SCENARIOS


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    entries = json.loads((ROOT / "src/gncore/skills/unified_data/manifest.json").read_text(encoding="utf-8"))
    base = json.loads((ROOT / "catalog/base_evaluations.json").read_text(encoding="utf-8"))
    cases = []
    for entry in entries:
        ids = {w["id"] for w in entry["workflows"]}
        reused = [case for case in base if case["category"] == entry["id"]]
        if reused:
            for case in reused:
                case["workflows"] = [name for name in case["workflows"] if name in ids]
                if not case["workflows"]:
                    raise ValueError(f"empty expected mode: {case['id']}")
            cases.extend(reused)
            continue
        for kind, (mode, prompt, context, artifact) in zip(("normal", "underspecified", "boundary"), SCENARIOS[entry["id"]]):
            if mode not in ids:
                raise ValueError(f"unknown evaluation mode: {entry['id']}/{mode}")
            cases.append({"id": entry["id"] + "-" + kind, "category": entry["id"], "kind": kind,
                          "prompt": prompt, "context": context, "workflows": [mode], "artifact": artifact,
                          "properties": [entry["description"], "Preserve the concrete input contracts and constraints; identify material unknowns."],
                          "prohibited": ["Invented measurements, source facts, available tools or completed external actions.", "Ignoring the explicit boundary or silently changing the requested stack/contract."],
                          "verification": "Use the concrete fixture or observable review specified in the context; distinguish executed checks from unavailable tools.",
                          "human_review": ["Does the artifact complete this specific task rather than provide a generic checklist?", "Are assumptions, evidence and remaining limits traceable to the actual context?"]})
    if len(cases) != 3 * len(entries):
        raise ValueError("three scenarios are required per active category")
    data = {"schema_version": 1, "scope": "developer-catalog", "categories": [e["id"] for e in entries], "cases": cases}
    raw = (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    path = ROOT / "src/gncore/evaluation_cases.json"
    changed = not path.is_file() or path.read_bytes() != raw
    if not args.check:
        path.write_bytes(raw)
    print(json.dumps({"categories": len(entries), "cases": len(cases), "changed": changed, "mode": "check" if args.check else "build"}))
    return int(args.check and changed)


if __name__ == "__main__":
    raise SystemExit(main())
