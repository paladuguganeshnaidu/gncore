"""Preserve a captured IDE response and validate its task identities."""
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]


def parse_response(text,run_id):
    decoder=json.JSONDecoder()
    matches=list(re.finditer(r'\{\s*"benchmark_run"\s*:',text))
    errors=[]
    for match in matches:
        try:
            result,end=decoder.raw_decode(text[match.start():])
        except json.JSONDecodeError as exc:
            errors.append(str(exc));continue
        if result.get("benchmark_run")==run_id:
            return result
    raise ValueError("No valid matching response JSON: "+"; ".join(errors[:2]))


def ingest(source,host,run_id,case_ids=None):
    raw=source.read_text(encoding="utf-8-sig")
    result=parse_response(raw,run_id)
    split=run_id.rsplit("-",1)[1]
    tasks=[t for t in json.loads((ROOT/"benchmarks/comparison/tasks.json").read_text(encoding="utf-8")) if t['split']==split]
    known={t['id']:t for t in tasks}
    if case_ids is not None:
        if not case_ids or not set(case_ids) <= set(known):
            raise ValueError("Subset must name known frozen task IDs")
        known={k:v for k,v in known.items() if k in case_ids}
    answers=result.get('answers')
    if not isinstance(answers,list):raise ValueError("answers must be an array")
    ids=[a.get('id') for a in answers if isinstance(a,dict)]
    if len(ids)!=len(set(ids)) or set(ids)!=set(known):
        raise ValueError(f"Task IDs differ: missing {set(known)-set(ids)}, extra {set(ids)-set(known)}, duplicate count {len(ids)-len(set(ids))}")
    destination=ROOT/'web-results/comparison/runs'/f'{host}-{run_id}'
    destination.mkdir(parents=True,exist_ok=True)
    summaries=[]
    for answer in answers:
        task=known[answer['id']]
        if not isinstance(answer.get('answer'),str):raise ValueError("Missing textual answer")
        code=answer.get('artifact_code')
        artifact=None
        if code is not None:
            if not isinstance(code,str):raise ValueError("artifact_code must be text or null")
            extension='html' if task['artifact']=='html' else 'py'
            artifact=f"{task['id']}.{extension}"
            (destination/artifact).write_text(code,encoding='utf-8',newline='\n')
        summaries.append({'id':task['id'],'category':task['category'],'artifact':artifact,'answer_characters':len(answer['answer'])})
    (destination/'response.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    metadata={'host':host,'run_id':run_id,'raw_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'cases':len(answers),
              'schema_status':'case identities and basic types valid; semantic review pending','answers':summaries}
    (destination/'import.json').write_text(json.dumps(metadata,indent=2)+'\n',encoding='utf-8')
    return metadata


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source',type=Path)
    parser.add_argument('--host',required=True,choices=['antigravity','vscode'])
    parser.add_argument('--run-id',required=True)
    parser.add_argument('--cases',nargs='+',help='Explicit subset for separately labeled adaptive follow-up; omitted requires the full split')
    args=parser.parse_args()
    print(json.dumps(ingest(args.source,args.host,args.run_id,args.cases),indent=2))
