"""Mask condition identity for the separate fresh-context rubric review."""
import hashlib,json,random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1/isolated'
WORK=ROOT/'.work/improvement-cycle-1/isolated'

def read(p):return json.loads(p.read_text(encoding='utf-8'))

def main():
    rng=random.Random(70931)
    profiles=['baseline','reference','candidate','control']
    rubrics={x['id']:x for x in read(ROOT/'benchmarks/comparison/rubrics.json')}
    answers={p:{a['id']:a for a in read(OUT/'runs'/p/'response.json')['answers']} for p in profiles}
    mapping={};manifest=[]
    for batch in (1,2,3):
        pack=read(WORK/f'candidate-batch-{batch}.json')
        items=[]
        for case in pack['cases']:
            order=list(profiles);rng.shuffle(order)
            for profile in order:
                response_id=f'R{len(mapping)+1:03d}'
                mapping[response_id]={'profile':profile,'case_id':case['id']}
                answer=answers[profile][case['id']]
                folder=OUT/'runs'/profile
                execution=folder/(case['id']+'-tests.json')
                browser=folder/(case['id']+'-browser.json')
                items.append({'response_id':response_id,'case_id':case['id'],'prompt':case['prompt'],
                              'checks':rubrics[case['id']]['checks'],'answer':answer,
                              'execution':read(execution) if execution.exists() else None,
                              'browser':read(browser) if browser.exists() else None})
        path=WORK/f'masked-review-{batch}.json'
        path.write_text(json.dumps({'items':items,'scope':'Condition-masked review. H14c4 is not-applicable; H30c6 is not-measured when390px unavailable. No other automatic exceptions.'},indent=2)+'\n',encoding='utf-8')
        manifest.append({'batch':batch,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'responses':len(items)})
    (WORK/'masked-mapping.json').write_text(json.dumps(mapping,indent=2)+'\n',encoding='utf-8')
    (OUT/'masked-review-inputs.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
