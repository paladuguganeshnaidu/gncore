"""Keep the first comparison intact and derive a labeled adaptive final view."""
import copy
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1'

def read(p):return json.loads(p.read_text(encoding='utf-8'))

def main():
    first=next(r for r in read(OUT/'review-results.json')['runs'] if r['profile']=='candidate')
    answers=read(OUT/'internal-focused-pass-1.json')
    notes=read(ROOT/'benchmarks/improvement-cycle-1/focused-review-notes.json')
    assert {a['id'] for a in answers['answers']}==set(notes['reviews'])=={'H03','H15','H27'}
    final=copy.deepcopy(first)
    final['profile']='candidate-focused'
    for case in final['cases']:
        if case['id'] not in notes['reviews']:continue
        note=notes['reviews'][case['id']]
        for criterion in case['checks']:
            criterion['status']='fail' if criterion['id'] in note['fail'] else 'pass'
            criterion['evidence']=note['fail'].get(criterion['id'],note['basis'])
        case['passed']=sum(c['status']=='pass' for c in case['checks'])
        case['percent']=100*case['passed']/case['total']
        case['review_note']=note['basis']
        case['phase']='adaptive-focused-pass-1'
    final['passed']=sum(c['passed'] for c in final['cases'])
    final['percent']=100*final['passed']/final['total']
    final['scope']=notes['scope']
    final['valid_for_fair_comparison']=False
    final['context_warning']='DEVELOPMENT ONLY: inherited parent context may reveal earlier analysis. This adaptive aggregate is withdrawn from headline quality claims; see isolated/STATUS.json.'
    final['first_candidate_response_sha256']=first['response_sha256']
    final['focused_response_sha256']=hashlib.sha256((OUT/'internal-focused-pass-1.json').read_bytes()).hexdigest()
    final['changed_case_ids']=['H03','H15','H27']
    final['remaining_unmeasured']=['H30c6:390px viewport did not apply; full frontend target not established.']
    (OUT/'final-candidate-results.json').write_text(json.dumps(final,indent=2)+'\n',encoding='utf-8')
    sizes=[]
    for old in read(OUT/'entrypoint-size-comparison.json'):
        path=ROOT/'src/gncore/skills/unified_data'/old['category']/'SKILL.md'
        sizes.append({'category':old['category'],'before_bytes':old['before_bytes'],'final_bytes':path.stat().st_size,
                      'final_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    before=sum(r['before_bytes'] for r in sizes);after=sum(r['final_bytes'] for r in sizes)
    (OUT/'final-entrypoint-sizes.json').write_text(json.dumps({'before_bytes':before,'after_bytes':after,
            'reduction_percent':100*(before-after)/before,'categories':sizes,
            'scope':'Unconditional source entrypoint bytes; supporting workflows are read conditionally. No token/cost/latency measurement.'},indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':final['passed'],'total':final['total'],'percent':final['percent'],'fully_measured_categories':sum(c['complete'] for c in final['cases']), 'entrypoint_byte_reduction_percent':100*(before-after)/before}))

if __name__=='__main__':main()
