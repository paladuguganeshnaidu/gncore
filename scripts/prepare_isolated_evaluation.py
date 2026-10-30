"""Freeze a single balanced fresh-context validation after development corrections."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'.work/improvement-cycle-1'
OUT=ROOT/'web-results/improvement-cycle-1/isolated'

def main():
    OUT.mkdir(exist_ok=True)
    dest=WORK/'isolated';dest.mkdir(exist_ok=True)
    records=[]
    for profile in ('baseline','reference','candidate','control'):
        for i in (1,2,3):
            data=json.loads((WORK/f'{profile}-batch-{i}.json').read_text())
            data['run_id']=f'isolated-{profile}-batch-{i}'
            data['scope']='One fresh-context known-task validation. Frozen final candidate; no target-score resampling.'
            for case in data['cases']:
                if case['guidance_file']:
                    case['guidance_sha256']=hashlib.sha256(Path(case['guidance_file']).read_bytes()).hexdigest()
            path=dest/f'{profile}-batch-{i}.json'
            path.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
            records.append({'profile':profile,'batch':i,'pack_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'cases':[c['id'] for c in data['cases']]})
    (OUT/'input-manifest.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()
