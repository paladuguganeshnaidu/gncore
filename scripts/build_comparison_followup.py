"""Create an explicitly adaptive follow-up for three changed entrypoints.

These reuse known tasks after error analysis. They are not unseen holdout data
and must never be spliced into the original 30-case score as if they were.
"""
import hashlib
import json
from pathlib import Path
import re
from build_comparison_packs import ROOT, OUTPUT, build

def main():
    original=OUTPUT/"gncore-after-holdout.md"
    metadata=json.loads(original.with_suffix(".json").read_text(encoding="utf-8"))
    text=original.read_text(encoding="utf-8")
    saved=ROOT/"web-results/comparison/initial-candidate"
    saved.mkdir(exist_ok=True)
    for case,category in [("H04","code-build"),("H24","performance-engineering"),("H30","web-frontend")]:
        match=re.search(rf"## Task {case}.*?<reference-guidance>\n(.*?)\n</reference-guidance>",text,re.S)
        content=match.group(1).encode("utf-8")
        assert hashlib.sha256(content).hexdigest()==metadata["source_sha256"][category]
        (saved/f"{category}-SKILL.md").write_bytes(content)
    (saved/"pack-metadata.json").write_text(json.dumps(metadata,indent=2)+"\n",encoding="utf-8")
    current=build("gncore-after","holdout")
    text=original.read_text(encoding="utf-8")
    sections=re.split(r"(?=^## Task H\d\d)",text,flags=re.M)
    selected=[s for s in sections[1:] if re.match(r"## Task (H04|H24|H30)\b",s)]
    assert len(selected)==3
    run_id="gncore-final-followup-holdout"
    header=sections[0].replace("30 independent","3 independent").replace("all 30","all 3").replace("gncore-after-holdout",run_id)
    header+="\nThis is an adaptive follow-up after earlier error analysis, not an unseen holdout. Complete the supplied tasks independently using the final entrypoints.\n\n"
    path=OUTPUT/f"{run_id}.md"
    path.write_text(header+"".join(selected),encoding="utf-8",newline="\n")
    record={"run_id":run_id,"phase":"adaptive follow-up, not unseen holdout","case_ids":["H04","H24","H30"],"pack_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"source_sha256":{k:v for k,v in current['source_sha256'].items() if k in {'code-build','performance-engineering','web-frontend'}}}
    (ROOT/"web-results/comparison/final-followup-input.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(record,indent=2))

if __name__=="__main__":main()
