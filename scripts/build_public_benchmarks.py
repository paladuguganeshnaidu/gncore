"""Render public, source-backed GNCore charts without inventing quality scores."""
from __future__ import annotations
import argparse,csv,hashlib,json,shutil,subprocess,sys
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/public-benchmarks';OUT.mkdir(parents=True,exist_ok=True)
PAPER='#f8f7f3';INK='#171827';PURPLE='#7b68c6';LILAC='#d1c4ff';LIME='#b9ed70';MUTED='#666575';LINE='#dddcd7'
ORDER=['gncore-before','reference','gncore-after']
LABELS={'gncore-before':'GNCore baseline','reference':'Published references','gncore-after':'GNCore revised trial'}
COLORS=[LILAC,'#777b87',PURPLE]
HOSTS={'vscode':'VS Code / Copilot Auto','antigravity':'Antigravity'}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'text.color':INK,'axes.labelcolor':MUTED,
 'xtick.color':MUTED,'ytick.color':MUTED,'axes.facecolor':PAPER,'figure.facecolor':PAPER,'svg.fonttype':'path','svg.hashsalt':'gncore-public-v1'})

def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def pct(p,n):return 100*p/n if n else None
def name(s):return s.replace('-',' ').title().replace('Ai ','AI ').replace('Mlops','MLOps')
def axis(ax):
    for spine in ax.spines.values():spine.set_visible(False)
    ax.tick_params(length=0,pad=8);ax.set_axisbelow(True);ax.grid(axis='y',color=LINE,lw=.7)
def title(fig,kicker,heading,sub):
    fig.text(.065,.95,'GNCORE  /  '+kicker,fontsize=10,color=PURPLE,weight='bold')
    fig.text(.065,.885,heading,fontsize=25,weight='bold')
    fig.text(.065,.835,sub,fontsize=10.5,color=MUTED)
def footer(fig,text):fig.text(.065,.055,text,fontsize=9,color=MUTED)
def save(fig,slug,pdf):
    fig.savefig(OUT/(slug+'.svg'),metadata={'Date':None})
    fig.savefig(OUT/(slug+'.png'),dpi=150)
    fig.savefig(OUT/(slug+'.pdf'),metadata={'CreationDate':None,'ModDate':None})
    pdf.savefig(fig);plt.close(fig)

def build_data():
    source='web-results/comparison/review-results.json';review=load(source)
    runs=[r for r in review['runs'] if r['split']=='holdout']
    lookup={(r['host'],r['profile']):r for r in runs}
    assert len(lookup)==6
    totals=[];categories=[];tasks=[];security=[]
    for host in HOSTS:
        for profile in ORDER:
            run=lookup[host,profile]
            complete=[c for c in run['cases'] if c['complete'] and c['category']!='web-frontend']
            assert len(complete)==29
            p=sum(c['passed'] for c in complete);n=sum(c['total'] for c in complete)
            assert n==173
            totals.append({'host':host,'profile':profile,'passed':p,'total':n,'percent':pct(p,n),'categories':29,'run':run['run']})
            for c in run['cases']:
                categories.append({'host':host,'profile':profile,'category':c['category'],'passed':c['passed'],'total':c['total'],'complete':c['complete'],'percent':pct(c['passed'],c['total']) if c['complete'] else None})
                if c['category'] in ('code-build','neural-networks','testing'):
                    e=c['execution'];assert not e.get('error')
                    tasks.append({'host':host,'profile':profile,'category':c['category'],'passed':e['passed'],'total':e['total'],'percent':pct(e['passed'],e['total']),'evidence':e['evidence']})
                if c['category']=='cybersecurity':security.append({'host':host,'profile':profile,**c['security']})
    assert next(t for t in totals if t['host']=='vscode' and t['profile']=='gncore-after')['passed']==168
    # A historical router corpus is descriptive, not a held-out accuracy estimate.
    local_path='web-results/production-release/local/benchmarks.json'
    if not (ROOT/local_path).is_file():local_path='web-results/benchmarks.json'
    local=load(local_path);routing=[]
    for kind in ('normal','underspecified','boundary'):
        rows=[r for r in local['scenario_routes'] if r['kind']==kind]
        routing.append({'kind':kind,'matched':sum(r['category_match'] for r in rows),'total':len(rows),
                        'needs_context':sum(r['status']=='needs-context' for r in rows),'percent':pct(sum(r['category_match'] for r in rows),len(rows))})
    baseline='62c4c99ef08b83cff415c01d6841a8e8b4a9e2da'
    manifest=load('src/gncore/skills/unified_data/manifest.json');footprint=[]
    for entry in manifest:
        rel=f"src/gncore/skills/unified_data/{entry['id']}/SKILL.md"
        before=subprocess.run(['git','show',baseline+':'+rel],cwd=ROOT,capture_output=True,check=True).stdout
        now=(ROOT/rel).read_bytes()
        footprint.append({'category':entry['id'],'before_bytes':len(before.replace(b'\r\n',b'\n')),'current_bytes':len(now.replace(b'\r\n',b'\n'))})
    source_paths=[source,local_path,'src/gncore/skills/unified_data/manifest.json','web-results/comparison/source-snapshots.json']
    tests_path=ROOT/'web-results/production-release/local-tests.txt';tests=None
    if tests_path.exists():
        import re
        m=re.search(r'(\d+) passed(?:, (\d+) skipped)?',tests_path.read_text(encoding='utf-8',errors='replace'))
        failed=re.search(r'(\d+) failed',tests_path.read_text(encoding='utf-8',errors='replace'))
        if m:tests={'passed':int(m[1]),'skipped':int(m[2] or 0),'failed':int(failed[1]) if failed else 0,'source':'web-results/production-release/local-tests.txt'}
    data={'schema_version':1,'current_version':manifest[0]['version'],'pilot_label':'Historical IDE pilot, 29 October 2026',
        'pilot_scope':'Same holdout tasks; 29 fully reviewed non-UI categories; one unblinded trial per host/condition. Prior trial guides, not a fresh evaluation of the current release.',
        'limitations':['Manual unblinded review; one task per category and no repeated trials.','Copilot Auto is not a fixed model; library-wide batches can share context.','No no-skill control; no causal or publisher-wide superiority conclusion.','Web frontend holdout browser checks remain unmeasured.','Adaptive follow-ups and withdrawn development quality scores are excluded from the comparison.'],
        'totals':totals,'categories':categories,'execution':tasks,'security':security,'routing':routing,'footprint':footprint,
        'entrypoint_baseline_commit':baseline,'local_version':local['version'],'local_recorded_at_utc':local['recorded_at_utc'],
        'latency':[{k:c[k] for k in ('category','render','explicit_route','resource_read')} for c in local['categories']],
        'catalog':{'categories':len(manifest),'workflows':sum(len(e['workflows']) for e in manifest),'resources':sum(len(e['resources']) for e in manifest)},
        'package_tests':tests,'sources':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in source_paths}}
    return data

def render(data):
    with PdfPages(OUT/'GNCore-benchmark-report.pdf',metadata={'Title':'GNCore benchmark evidence','CreationDate':None,'ModDate':None}) as pdf:
        fig,axs=plt.subplots(1,2,figsize=(12.8,7.2));fig.subplots_adjust(left=.08,right=.96,bottom=.21,top=.72,wspace=.3)
        title(fig,'HISTORICAL IDE PILOT','Same tasks. Results you can inspect.','Passed review criteria / 173 applicable checks per condition. 29 non-UI categories.')
        for ax,(host,label) in zip(axs,HOSTS.items()):
            rows=[next(t for t in data['totals'] if t['host']==host and t['profile']==p) for p in ORDER]
            bars=ax.bar(range(3),[r['percent'] for r in rows],color=COLORS,width=.58,zorder=3)
            for b,r in zip(bars,rows):ax.text(b.get_x()+b.get_width()/2,r['percent']+3,f"{r['percent']:.1f}%\n{r['passed']}/{r['total']}",ha='center',fontsize=11,weight='bold')
            ax.set(ylim=(0,115),yticks=[0,25,50,75,100],xticks=range(3),xticklabels=['GNCore\nbaseline','Published\nreferences','GNCore\nrevised trial'],ylabel='Checks passed (%)');ax.set_title(label,loc='left',pad=24,fontsize=14,weight='bold');axis(ax)
        footer(fig,'29 Oct 2026 · Single unblinded pilot · Prior guides, not current-release accuracy · UI unmeasured · No universal ranking')
        save(fig,'ide-pilot',pdf)

        cats=sorted({r['category'] for r in data['categories']});matrix=np.full((30,6),np.nan);texts={}
        for i,c in enumerate(cats):
            for j,(host,profile) in enumerate((h,p) for h in HOSTS for p in ORDER):
                r=next(r for r in data['categories'] if r['category']==c and r['host']==host and r['profile']==profile)
                if r['complete']:matrix[i,j]=r['percent'];texts[i,j]=f"{r['passed']}/{r['total']}  ·  {r['percent']:.0f}%"
        fig,ax=plt.subplots(figsize=(16,11.2));fig.subplots_adjust(left=.25,right=.95,bottom=.13,top=.76)
        title(fig,'EVERY DEVELOPER DOMAIN','All 30 categories, including open measurements.','Historical holdout review. Each cell shows passed / applicable checks and the percentage.')
        cm=LinearSegmentedColormap.from_list('gncore',[PAPER,LILAC,PURPLE]);cm.set_bad('#e5e4e0');ax.imshow(matrix,aspect='auto',vmin=0,vmax=100,cmap=cm)
        ax.set(yticks=range(30),yticklabels=[name(c) for c in cats],xticks=range(6),xticklabels=['VS Code\nBaseline','VS Code\nReference','VS Code\nRevised','Antigravity\nBaseline','Antigravity\nReference','Antigravity\nRevised']);ax.xaxis.tick_top();ax.tick_params(length=0,labelsize=10,pad=12)
        for i in range(30):
            for j in range(6):ax.text(j,i,texts.get((i,j),'Unmeasured'),ha='center',va='center',fontsize=9,color='white' if matrix[i,j]>85 else INK)
        for s in ax.spines.values():s.set_visible(False)
        footer(fig,'Open measurements remain gray. Small denominators and one task per category do not establish future success rates.')
        save(fig,'all-categories',pdf)

        fig,axs=plt.subplots(2,3,figsize=(12.8,8.3));fig.subplots_adjust(left=.08,right=.97,bottom=.17,top=.73,wspace=.33,hspace=.8)
        title(fig,'EXECUTED CODE','Focused checks for generated implementations.','Historical pilot artifacts. Frozen test outcomes are separate from manual review scores.')
        for row,(host,hostlabel) in enumerate(HOSTS.items()):
            for col,(cat,label) in enumerate([('code-build','Allocation · 16 cases'),('neural-networks','Loss & gradients · 14 cases'),('testing','Implementation + 6 mutants')]):
                ax=axs[row,col];rs=[next(r for r in data['execution'] if r['host']==host and r['profile']==p and r['category']==cat) for p in ORDER]
                bars=ax.bar(range(3),[r['percent'] for r in rs],color=COLORS,width=.6)
                for b,r in zip(bars,rs):ax.text(b.get_x()+b.get_width()/2,r['percent']+4,f"{r['passed']}/{r['total']}",ha='center',fontsize=10)
                ax.set(ylim=(0,120),yticks=[0,50,100],xticks=range(3),xticklabels=['Base','Ref','Revised']);ax.set_title(hostlabel.split(' / ')[0]+'\n'+label,loc='left',fontsize=11);axis(ax)
        footer(fig,'All three arms tied on several fixtures. The revised VS Code allocation later failed 3/3 exploratory cases; follow-up repairs are separate.')
        save(fig,'code-checks',pdf)

        fig,axs=plt.subplots(1,2,figsize=(12.8,7.2));fig.subplots_adjust(left=.08,right=.96,bottom=.23,top=.71,wspace=.3)
        title(fig,'SECURITY FIXTURE','Six seeded findings. Four safe controls.','Manual review of a supplied fixture; exploits were not executed. All three conditions tied.')
        for ax,(host,label) in zip(axs,HOSTS.items()):
            rs=[next(r for r in data['security'] if r['host']==host and r['profile']==p) for p in ORDER]
            for j,r in enumerate(rs):
                assert r['found']==6 and r['safe_controls_flagged']==0
                ax.bar(j,r['found'],width=.58,color=COLORS[j]);ax.text(j,6.2,'6/6 found\n0/4 safe flagged',ha='center',fontsize=10)
            ax.set(ylim=(0,8),yticks=[0,2,4,6],xticks=range(3),xticklabels=['Baseline','Reference','Revised'],ylabel='Seeded findings identified');ax.set_title(label,loc='left',fontsize=14);axis(ax)
        footer(fig,'A bounded fixture result, not a production security rating. Source findings, repair checks and safe-control counts remain inspectable.')
        save(fig,'security-fixture',pdf)

        fig,axs=plt.subplots(1,2,figsize=(12.8,7.2));fig.subplots_adjust(left=.09,right=.95,bottom=.24,top=.71,wspace=.4)
        title(fig,'ROUTING CORPUS','Routing is measured separately from skill quality.','Authored diagnostic prompts. These are in-corpus observations, not a held-out comparison.')
        normal=next(r for r in data['routing'] if r['kind']=='normal');ax=axs[0]
        ax.barh([0],[normal['matched']],color=PURPLE,height=.4);ax.barh([0],[normal['total']-normal['matched']],left=[normal['matched']],color=LINE,height=.4)
        ax.text(0,.55,f"{normal['matched']}/{normal['total']}  ·  {normal['percent']:.0f}%",fontsize=28,weight='bold');ax.set(xlim=(0,30),ylim=(-.6,1),yticks=[],xticks=[0,10,20,30],xlabel='Normal prompts matching the authored category');axis(ax)
        ax=axs[1];rs=data['routing'];ax.bar(range(3),[r['needs_context'] for r in rs],color=[LILAC,PURPLE,LIME],width=.6)
        for i,r in enumerate(rs):ax.text(i,r['needs_context']+.6,f"{r['needs_context']}/{r['total']}",ha='center')
        ax.set(ylim=(0,32),yticks=[0,10,20,30],xticks=range(3),xticklabels=['Normal','Underspecified','Boundary'],ylabel='Requests for more context');axis(ax)
        footer(fig,'Context requests can be appropriate for vague prompts. This chart does not count every abstention as an error or claim 90–97% routing.')
        save(fig,'routing-corpus',pdf)

        fig,ax=plt.subplots(figsize=(12.8,7.2));fig.subplots_adjust(left=.1,right=.94,bottom=.22,top=.72)
        title(fig,'ENTRYPOINT SIZE','Focused entrypoints. Detailed procedures on demand.','Distribution of UTF-8 SKILL.md bytes across all 30 categories; supporting resources remain available.')
        for key,label,color in [('before_bytes','Earlier guides',MUTED),('current_bytes','Current release',PURPLE)]:
            values=sorted(r[key]/1024 for r in data['footprint']);ax.step(values,np.arange(1,31)/30*100,where='post',label=label,color=color,lw=2.5)
        ax.set(xlabel='Entry instruction size (KiB)',ylabel='Categories at or below this size (%)',ylim=(0,105),yticks=[0,25,50,75,100]);axis(ax);ax.legend(frameon=False,loc='lower right')
        footer(fig,'Measured bytes, not tokens, inference speed or cost. Baseline source revision: 62c4c99. All workflow IDs are retained.')
        save(fig,'entrypoint-footprint',pdf)

        fig,ax=plt.subplots(figsize=(12.8,7.2));fig.subplots_adjust(left=.1,right=.94,bottom=.23,top=.72)
        title(fig,'LOCAL LIBRARY OPERATIONS','Warm local timing, with its scope visible.','Cumulative distribution of recorded samples. CPU + filesystem only; excludes IDE and model inference.')
        for key,label,color in [('render','Render guide',PURPLE),('explicit_route','Explicit route',MUTED),('resource_read','Read resources','#62942d')]:
            values=sorted(v for c in data['latency'] for v in c[key]['samples_ms'])
            ax.step(values,np.arange(1,len(values)+1)/len(values)*100,where='post',label=f'{label} (n={len(values)})',lw=2,color=color)
        ax.set(xscale='log',xlabel='Wall-clock milliseconds · logarithmic scale',ylabel='Samples completed at or below this time (%)',ylim=(0,105),yticks=[0,25,50,75,100]);axis(ax);ax.legend(frameon=False,loc='lower right')
        footer(fig,'Recorded '+data['local_recorded_at_utc'][:10]+' · '+data['local_version']+' · warmups and uncontrolled filesystem caches · no cross-provider speed claim')
        save(fig,'local-latency',pdf)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--data-only',action='store_true');args=parser.parse_args()
    data=build_data()
    if not args.data_only:render(data)
    (OUT/'benchmark-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    rows=data['categories']
    with (OUT/'category-results.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    (OUT/'README.md').write_text('# GNCore public benchmark figures\n\nRegenerate with `python scripts/build_public_benchmarks.py`. Charts use original measurements, the GNCore palette, denominators and explicit scope. Data sources and SHA-256 digests are in benchmark-data.json.\n\nThe IDE results are the historical 29 October pilot, not a fresh evaluation of 7.0.0. Withdrawn development quality scores and adaptive follow-ups are not mixed into that comparison. The public charts do not establish causal gains, universal security or a ranking of AI vendors. Source-specific attribution remains in the linked snapshots.\n',encoding='utf-8')
    web=ROOT/'web/benchmarks';web.mkdir(exist_ok=True)
    for p in OUT.iterdir():
        if p.suffix in ('.svg','.pdf','.json','.csv'):shutil.copyfile(p,web/p.name)
    shutil.copyfile(ROOT/'web-results/comparison/source-snapshots.json',web/'source-snapshots.json')
    print(json.dumps({'charts':7,'categories':30,'pilot_conditions':6,'output':str(OUT)}))

if __name__=='__main__':main()
