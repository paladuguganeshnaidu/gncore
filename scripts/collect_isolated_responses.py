"""Collect only schema-valid fresh-context responses and preserve their hashes."""
import argparse,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1/isolated'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--profile',required=True,choices=['baseline','reference','candidate','control']);args=parser.parse_args()
    answers=[];inputs=[]
    for i in (1,2,3):
        path=OUT/f'{args.profile}-batch-{i}.json'
        raw=json.loads(path.read_text(encoding='utf-8'))
        pack=json.loads((ROOT/f'.work/improvement-cycle-1/isolated/{args.profile}-batch-{i}.json').read_text(encoding='utf-8'))
        assert raw['benchmark_run']==pack['run_id']
        assert len(raw['answers'])==10 and {a['id'] for a in raw['answers']}=={c['id'] for c in pack['cases']}
        for answer in raw['answers']:
            assert isinstance(answer['answer'],str) and answer['answer'].strip()
            assert isinstance(answer['verification'],str) and isinstance(answer['findings'],list)
        inputs.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        answers.extend(raw['answers'])
    folder=OUT/'runs'/args.profile;folder.mkdir(parents=True,exist_ok=True)
    (folder/'response.json').write_text(json.dumps({'benchmark_run':'isolated-'+args.profile,'answers':sorted(answers,key=lambda a:a['id'])},indent=2)+'\n',encoding='utf-8')
    for answer in answers:
        if answer['id'] in {'H04','H22','H28','H30'}:
            assert answer['artifact_code']
            (folder/(answer['id']+('.html' if answer['id']=='H30' else '.py'))).write_text(answer['artifact_code'],encoding='utf-8')
    (folder/'capture.json').write_text(json.dumps({'inputs':inputs,'fork_turns':'none','scope':'Fresh-context known-task validation, one balanced pass.'},indent=2)+'\n',encoding='utf-8')
    print(args.profile+':30captured')

if __name__=='__main__':main()
