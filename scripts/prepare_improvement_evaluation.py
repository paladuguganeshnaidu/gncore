"""Freeze task-only inputs for a separate internal improvement-cycle block."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'.work/improvement-cycle-1'
OUT=ROOT/'web-results/improvement-cycle-1'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--profile',required=True,choices=['baseline','reference','candidate','control'])
    args=parser.parse_args()
    tasks=[x for x in json.loads((ROOT/'benchmarks/comparison/tasks.json').read_text(encoding='utf-8')) if x['split']=='holdout']
    sources={x['category']:x for x in json.loads((ROOT/'web-results/comparison/source-snapshots.json').read_text(encoding='utf-8'))}
    packs=[]
    for index in range(3):
        batch=tasks[index*10:(index+1)*10]
        cases=[]
        for task in batch:
            category=task['category']
            if args.profile=='baseline':
                guide=WORK/'baseline-guides'/category/'SKILL.md'
                support=ROOT/'src/gncore/skills/unified_data'/category
            elif args.profile=='reference':
                item=sources[category]
                guide=ROOT/item['local_snapshot']/item['entrypoint']
                support=guide.parent
            elif args.profile=='candidate':
                support=ROOT/'src/gncore/skills/unified_data'/category
                guide=support/'SKILL.md'
            else:guide=support=None
            cases.append({**task,'guidance_file':str(guide) if guide else None,
                          'support_folder':str(support) if support else None,
                          'guidance_sha256':hashlib.sha256(guide.read_bytes()).hexdigest() if guide else None})
        path=WORK/f'{args.profile}-batch-{index+1}.json'
        value={'run_id':f'internal-{args.profile}-batch-{index+1}',
               'scope':'Adaptive replay of previously used tasks; separate host/model block from historical IDE pilot.',
               'cases':cases,
               'response_shape':{'benchmark_run':'exact run_id','answers':[{'id':'case ID','answer':'specific proposed solution','artifact_code':'complete requested Python/HTML, otherwise null','findings':[{'id':'security snippet ID','issue':'concrete defect','repair':'specific repair'}],'verification':'proposed checks; do not claim unexecuted checks'}]}}
        path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        packs.append({'input':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'cases':[x['id'] for x in batch]})
    (OUT/f'{args.profile}-evaluation-inputs.json').write_text(json.dumps(packs,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(packs,indent=2))

if __name__=='__main__':main()
