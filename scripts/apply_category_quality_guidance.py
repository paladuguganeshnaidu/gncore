"""Apply original GNCore guidance, separately from upstream workflow provenance."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    path = ROOT / "catalog/categories.json"
    catalog = json.loads(path.read_text(encoding="utf-8"))
    guidance = json.loads((ROOT / "catalog/category-quality-guidance.json").read_text(encoding="utf-8"))
    assert set(guidance) == {entry["id"] for entry in catalog["categories"]}
    for entry in catalog["categories"]:
        previous = entry.get("extra", "").split("## Anticipate failure and verify the boundary")[0].strip()
        addition = "## Anticipate failure and verify the boundary\n\n" + guidance[entry["id"]]
        entry["extra"] = (previous + "\n\n" if previous else "") + addition
    path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"categories_updated": len(guidance), "workflow_procedures_changed": 0}))

if __name__ == "__main__":
    main()
