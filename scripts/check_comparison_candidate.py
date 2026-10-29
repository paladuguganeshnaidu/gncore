"""Record catalog preservation and candidate identities without inference claims."""
import hashlib
import json
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
    before=json.loads(subprocess.check_output(["git","show","cd77d82:catalog/categories.json"],cwd=ROOT))
    after=json.loads((ROOT/"catalog/categories.json").read_text(encoding="utf-8"))
    old={x["id"]:x for x in before["categories"]}
    records=[]
    for entry in after["categories"]:
        original=old[entry["id"]]
        assert entry["workflows"]==original["workflows"], entry["id"]
        assert entry["resources"]==original["resources"], entry["id"]
        assert entry["licenses"]==original["licenses"], entry["id"]
        assert original.get("extra", "").strip() in entry["extra"]
        assert "## Anticipate failure and verify the boundary" in entry["extra"]
        path=ROOT/"src/gncore/skills/unified_data"/entry["id"]/"SKILL.md"
        records.append({"category":entry["id"],"entrypoint_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"workflow_count":len(entry["workflows"]),"existing_guidance_preserved":True})
    record={"baseline":"cd77d82","categories":len(records),"workflows":sum(r["workflow_count"] for r in records),"workflow_procedures_unchanged":True,"resources_and_licenses_preserved":True,"entrypoints":records}
    (ROOT/"web-results/comparison/candidate-integrity.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:v for k,v in record.items() if k!="entrypoints"}))
if __name__=="__main__":main()
