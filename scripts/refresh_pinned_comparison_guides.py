"""Download public pinned guides for review; verify bytes and never execute them."""
from concurrent.futures import ThreadPoolExecutor
import hashlib,json
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1'
DEST=ROOT/'.work/improvement-cycle-1/downloaded-guides'

def download(entry):
    url=f"https://raw.githubusercontent.com/{entry['repo']}/{entry['revision']}/{entry['entrypoint']}"
    record={k:entry[k] for k in ('category','repo','revision','entrypoint','url','entrypoint_license')}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'GNCore-pinned-guide-review'})
        with urllib.request.urlopen(request,timeout=25) as response:data=response.read(2_000_001)
        if len(data)>2_000_000:raise ValueError('guide exceeds review download limit')
        digest=hashlib.sha256(data).hexdigest()
        checkout=(ROOT/entry['local_snapshot']/entry['entrypoint']).read_bytes()
        checkout_digest=hashlib.sha256(checkout).hexdigest()
        if checkout_digest!=entry['entrypoint_sha256']:raise ValueError('recorded local checkout changed')
        normalized=data.replace(b'\r\n',b'\n')
        if normalized!=checkout.replace(b'\r\n',b'\n'):raise ValueError('pinned content differs beyond checkout line endings')
        folder=DEST/entry['category'];folder.mkdir(parents=True,exist_ok=True)
        (folder/'UPSTREAM.md').write_bytes(data)
        notices=0
        for path in (ROOT/entry['local_snapshot']).glob('LICENSE*'):
            if path.is_file():(folder/('REPOSITORY-'+path.name)).write_bytes(path.read_bytes());notices+=1
        record.update(downloaded=True,sha256=digest,recorded_checkout_sha256=checkout_digest,
                      normalized_lf_sha256=hashlib.sha256(normalized).hexdigest(),
                      exact_byte_match=digest==checkout_digest,content_match_after_crlf_normalization=True,
                      bytes=len(data),repository_notices_retained=notices,helpers_executed=False)
    except Exception as error:record.update(downloaded=False,error=type(error).__name__+': '+str(error)[:200],helpers_executed=False)
    return record

def main():
    entries=json.loads((ROOT/'web-results/comparison/source-snapshots.json').read_text(encoding='utf-8'))
    with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(download,entries))
    (OUT/'downloaded-reference-guides.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'successful_guides':sum(r['downloaded'] for r in records),'requested_guides':len(records),'repositories':len({r['repo'] for r in records}),'helpers_executed':0}))

if __name__=='__main__':main()
