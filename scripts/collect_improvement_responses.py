"""Validate raw adaptive responses and extract generated artifacts without running them."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--profile',required=True,choices=['baseline','reference','candidate','control'])
    args=parser.parse_args()
    answers=[];inputs=[]
    for i in range(1,4):
        source=OUT/f'internal-{args.profile}-batch-{i}.json'
        pack=ROOT/f'.work/improvement-cycle-1/{args.profile}-batch-{i}.json'
        raw=json.loads(source.read_text(encoding='utf-8'))
        task=json.loads(pack.read_text(encoding='utf-8'))
        assert raw['benchmark_run']==task['run_id'],source
        values=raw['answers'];expected={x['id'] for x in task['cases']}
        assert len(values)==len(expected)==10 and {x['id'] for x in values}==expected,source
        for answer in values:
            assert isinstance(answer['answer'],str) and answer['answer'].strip()
            assert answer['artifact_code'] is None or isinstance(answer['artifact_code'],str)
            assert isinstance(answer['findings'],list) and isinstance(answer['verification'],str)
        answers.extend(values)
        inputs.append({'file':source.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(source.read_bytes()).hexdigest()})
    assert len({x['id'] for x in answers})==30
    folder=OUT/'runs'/args.profile;folder.mkdir(parents=True,exist_ok=True)
    (folder/'response.json').write_text(json.dumps({'benchmark_run':'internal-'+args.profile,'answers':sorted(answers,key=lambda x:x['id'])},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    for answer in answers:
        if answer['id'] in {'H04','H22','H28','H30'}:
            assert answer['artifact_code'],answer['id']
            suffix='.html' if answer['id']=='H30' else '.py'
            (folder/(answer['id']+suffix)).write_text(answer['artifact_code'],encoding='utf-8',newline='\n')
    record={'profile':args.profile,'answers':30,'raw_inputs':inputs,'scope':'Adaptive replay; separate internal agent block, not historical IDE inference.'}
    (folder/'capture.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
