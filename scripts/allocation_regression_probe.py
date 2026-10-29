"""Exploratory regression discovered after the frozen holdout was executed.

Keep these results separate from the predeclared 16-case test score. Apply the
same cases to every eligible saved condition; never rewrite the original code.
"""
import argparse
import json
from pathlib import Path
from grade_comparison_artifacts import inspect_source

def probe(source):
    inspect_source(source)
    namespace={}
    exec(compile(source,"<inspected-allocation>","exec"),namespace)
    records=[]
    for total,weights,expected in [(2,[1,2,3],[0,1,1]),(3,[1,2,3],[1,1,1]),(4,[1,2,3],[1,1,2])]:
        actual=namespace["allocate_cents"](total,weights)
        records.append({"total_cents":total,"weights":weights,"expected":expected,"actual":actual,"passed":actual==expected})
    return {"phase":"exploratory regression, added after inspecting a generated failure","reason":"A zero remainder must not outrank a positive remainder; conservation alone is insufficient.","tests":records,"passed":sum(t["passed"] for t in records),"total":len(records)}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source",type=Path)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    report=probe(args.source.read_text(encoding="utf-8"))
    args.output.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
