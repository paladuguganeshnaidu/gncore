"""Export exact Full HD/4K comparison tables from saved, reviewed evidence."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'web-results/comparison'
OUT = EVIDENCE / 'comparison-images'
WIDTH, HEIGHT, DPI = 1920, 1080, 100
INK, MUTED = '#172d40', '#526577'
TEAL, GOLD, LINE = '#087e75', '#9a641e', '#dce4ea'
PROFILES = ['gncore-before', 'reference', 'gncore-after']
HOSTS = ['vscode', 'antigravity']
RUNS = {}
SOURCES = {}


def text(ax, x, y, value, size=15, color=INK, weight='normal', align='left'):
    return ax.text(x, y, value, fontsize=size * 72 / DPI, color=color,
                   fontweight=weight, va='center', ha=align, family='DejaVu Sans')


def rect(ax, x, y, w, h, color, edge=None):
    ax.add_patch(Rectangle((x, y), w, h, facecolor=color,
                           edgecolor=edge or color, linewidth=.6))


def canvas(kicker, title, subtitle):
    fig = plt.figure(figsize=(WIDTH / DPI, HEIGHT / DPI), dpi=DPI, facecolor='#f5f7fa')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set(xlim=(0, WIDTH), ylim=(HEIGHT, 0))
    ax.axis('off')
    rect(ax, 0, 0, WIDTH, 7, TEAL)
    text(ax, 40, 32, kicker, 13, TEAL, 'bold')
    text(ax, 40, 72, title, 33, weight='bold')
    text(ax, 40, 106, subtitle, 16, MUTED)
    return fig, ax


def summary(host, profile):
    cases = [c for c in RUNS[(host, profile)]['cases'] if c['complete'] and c['category'] != 'web-frontend']
    assert len(cases) == 29
    return sum(c['passed'] for c in cases), sum(c['total'] for c in cases)


def percentage(p, n, decimals=1):
    return f'{100*p/n:.{decimals}f}% ({p}/{n})'


def case(host, profile, category):
    return next(c for c in RUNS[(host, profile)]['cases'] if c['category'] == category)


def case_label(c):
    return percentage(c['passed'], c['total']) if c['complete'] else 'NOT MEASURED'


def guide_name(category):
    source = SOURCES[category]
    owner = {'anthropics': 'Anthropic', 'microsoft': 'Microsoft', 'google': 'Google',
             'huggingface': 'Hugging Face', 'vercel-labs': 'Vercel', 'trailofbits': 'Trail of Bits',
             'obra': 'Superpowers', 'K-Dense-AI': 'K-Dense', 'affaan-m': 'ECC',
             'supabase': 'Supabase', 'cloudflare': 'Cloudflare',
             'temporalio': 'Temporal', 'beriberikix': 'Zephyr specialist',
             'minhhoit': 'Game-dev specialist'}[source['repo'].split('/')[0]]
    parent = Path(source['entrypoint']).parent.name
    if category == 'automation': parent = 'temporal developer'
    return owner + ' / ' + parent


def columns(ax, widths, y, height, titles, fills=None, size=14, bold=False):
    x = 40
    for i, (width, title) in enumerate(zip(widths, titles)):
        color = fills[i] if fills else '#ffffff'
        rect(ax, x, y, width, height, color)
        first = i == 0 or i == len(titles)-1
        text(ax, x+10 if first else x+width/2, y+height/2, title, size,
             '#ffffff' if color == INK else INK, 'bold' if bold else 'normal',
             'left' if first else 'center')
        x += width
    ax.plot([40, 1880], [y+height, y+height], color=LINE, lw=.45)


def footnotes(ax, lines, start=966):
    for i, line in enumerate(lines):
        text(ax, 40, start+i*22, line, 13.2, MUTED)


def save(fig, name):
    result=[]
    for suffix, dpi in [('full-hd', 100), ('4k', 200)]:
        path=OUT/f'{name}-{suffix}.png'
        fig.savefig(path, dpi=dpi, facecolor=fig.get_facecolor(),
                    metadata={'Title': name, 'Description': 'Evidence-backed GNCore pilot; not a universal efficiency rating.',
                              'Source': 'web-results/comparison/review-results.json'})
        result.append({'file':path.relative_to(ROOT).as_posix(), 'width':1920 if dpi==100 else 3840,
                       'height':1080 if dpi==100 else 2160,
                       'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    fig.savefig(OUT/f'{name}.svg',facecolor=fig.get_facecolor())
    plt.close(fig)
    return result


def category_table():
    fig, ax = canvas('GNCORE  /  COMPLETE CATEGORY COMPARISON  /  29 OCTOBER 2026',
                     'All 30 categories. Exact checks. Visible limits.',
                     'Same held-out tasks in each IDE. Published references vary by category; this is a pilot, not a publisher ranking.')
    for x, host, label in [(40, 'vscode', 'ORIGINAL VS CODE / COPILOT AUTO'),
                           (970, 'antigravity', 'ANTIGRAVITY / GEMINI 3.8 FLASH HIGH')]:
        rect(ax, x, 128, 910, 65, '#e9f3f1')
        before=summary(host,'gncore-before');ref=summary(host,'reference');after=summary(host,'gncore-after')
        text(ax,x+15,145,label+'  |  29 fully reviewed non-UI categories',12.4,TEAL,'bold')
        text(ax,x+15,173,f'Before {percentage(*before)}   Reference {percentage(*ref)}   Revised* {percentage(*after)}',18.2,weight='bold')
    widths=[310,180,180,180,180,180,180,450]
    assert sum(widths)==1840
    rect(ax,40,205,1840,23,INK)
    text(ax,620,217,'VS CODE',13,'white','bold','center')
    text(ax,1160,217,'ANTIGRAVITY',13,'white','bold','center')
    text(ax,1660,217,'PINNED REFERENCE GUIDE',13,'white','bold','center')
    columns(ax,widths,228,28,['Developer category','Before','Reference','Revised trial*','Before','Reference','Revised trial*','Source used for that category'],[INK]*8,13,True)
    rows=[]
    for i,category in enumerate(sorted(SOURCES)):
        name=category.replace('-', ' ').capitalize()
        names={'ai-engineering':'AI engineering','mlops':'MLOps','natural-language-processing':'Natural language processing',
               'cloud-devops-sre':'Cloud / DevOps / SRE','design-ux':'Design / UX'}
        values=[case_label(case(h,p,category)) for h in HOSTS for p in PROFILES]
        columns(ax,widths,256+i*19.4,19.4,[names.get(category,name),*values,guide_name(category)],
                ['#ffffff' if i%2==0 else '#edf1f5']+['#ffffff','#fff4e6','#e4f3ef']*2+['#ffffff' if i%2==0 else '#edf1f5'],12.8)
        rows.append({'category':category,**{h+'_'+p:case_label(case(h,p,category)) for h in HOSTS for p in PROFILES},
                     'reference_repository':SOURCES[category]['repo'],'reference_entrypoint':SOURCES[category]['entrypoint'],
                     'reference_revision':SOURCES[category]['revision'],'reference_url':SOURCES[category]['url']})
    rect(ax,40,856,1840,92,'#e8edf3')
    for x, title, line1, line2 in [
        (56,'GNCORE: VERIFIED CAPABILITIES','30 adaptive entrypoints / 374 workflows','Single category invocation; relevant workflows'),
        (520,'PORTABILITY','Offline exports; no required runtime deps','Host agent supplies the model and permissions'),
        (984,'INTEGRITY & PROVENANCE','1,660 installed files / 1,630 resources checked','Preserved source notices and recovery journals'),
        (1448,'EVIDENCE, NOT ASSURANCES','306 saved task answers across two IDEs','Package suite: 148 passed / 1 skipped')]:
        text(ax,x,876,title,12,TEAL,'bold');text(ax,x,904,line1,13.7,weight='bold');text(ax,x,928,line2,12.7,MUTED)
    footnotes(ax,[
        '* Revised = initial revised trial, not the final three-guide follow-up. Three later entrypoints were tested separately on known tasks.',
        'Percentages = applicable manual task checks passed. One task per category per condition; one unblinded reviewer; no repeated-trial or no-skill control.',
        'NOT MEASURED = incomplete rendered UI evidence; it is not 0%. Plotly-specific skills and the standalone OpenAI/Codex skill catalog were NOT benchmarked.',
        'No universal speed, cost, security or visual-design efficiency claim. Source: review-results.json / source-snapshots.json in web-results/comparison.',
        'All original failures are retained. A synced-folder Windows journal failure remains documented; the full suite passed outside the sync folder.'
    ])
    return save(fig,'gncore-complete-comparison-table'),rows


def overview_table():
    fig,ax=canvas('GNCORE  /  EXECUTIVE COMPARISON  /  SAVED EVIDENCE',
                  'What GNCore does differently - and what the tests show',
                  'Compare outcomes within the same IDE. References = 30 task-relevant guides from 14 pinned repositories, not one rival application.')
    widths=[310,180,180,180,180,180,180,450]
    rect(ax,40,128,1840,25,INK)
    text(ax,620,141,'ORIGINAL VS CODE / COPILOT AUTO',14,'white','bold','center')
    text(ax,1160,141,'ANTIGRAVITY / GEMINI',14,'white','bold','center')
    columns(ax,widths,153,33,['Measured item','Before','Reference','Revised trial*','Before','Reference','Revised trial*','Meaning / limitation'],[INK]*8,13,True)
    metrics=[]
    def six(fn):return [fn(h,p) for h in HOSTS for p in PROFILES]
    def exec_score(h,p,cat):
        r=case(h,p,cat)['execution'];return percentage(r['passed'],r['total'])
    def exploratory(h,p):
        r=json.loads((EVIDENCE/'runs'/f'{h}-{p}-holdout'/'H04-exploratory.json').read_text(encoding='utf-8'))
        return percentage(r['passed'],r['total'])
    metrics.append(('Engineering task checks',six(lambda h,p:percentage(*summary(h,p))),'Manual review; 29 complete non-UI categories'))
    metrics.append(('Seeded security issues found',six(lambda h,p:percentage(case(h,p,'cybersecurity')['security']['found'],6)),'Six synthetic defects; exploits not executed'))
    metrics.append(('Safe security controls flagged',six(lambda h,p:str(case(h,p,'cybersecurity')['security']['safe_controls_flagged'])+'/4 flagged'),'Lower is better; not an application-wide audit'))
    metrics.append(('Allocation: frozen code tests',six(lambda h,p:exec_score(h,p,'code-build')),'Small fixture missed a real ordering defect'))
    metrics.append(('Allocation: added regressions',six(exploratory),'Exploratory tests added after inspecting a failure'))
    metrics.append(('Neural-network numeric tests',six(lambda h,p:exec_score(h,p,'neural-networks')),'Loss, gradients, extreme values and validation'))
    metrics.append(('Test checker / mutant fixtures',six(lambda h,p:exec_score(h,p,'testing')),'Accept correct code; reject six buggy versions'))
    metrics.append(('Held-out rendered UI behavior',['NOT MEASURED']*6,'Browser access unavailable for these pages'))
    metrics.append(('Speed / cost efficiency',['NOT ESTABLISHED']*6,'No controlled repeated cost/latency experiment'))
    for i,(name,values,meaning) in enumerate(metrics):
        columns(ax,widths,186+i*35,35,[name,*values,meaning],
                ['#ffffff' if i%2==0 else '#edf1f5']+['#ffffff','#fff4e6','#e4f3ef']*2+['#ffffff'],13.2)
    text(ax,40,534,'HOW THE PRODUCT IS PACKAGED',19,weight='bold')
    product_widths=[400,620,820]
    columns(ax,product_widths,554,30,['Capability','GNCore: implemented and verified','What can fairly be concluded'],[INK]*3,14,True)
    products=[
        ('One domain invocation','30 entrypoints selecting among 374 workflows','A simpler entry format; not proof that rivals lack routing.'),
        ('Short or underspecified briefs','Visual direction and domain failure guidance','Guidance exists; every output still needs verification.'),
        ('Portable use','Offline skill ZIP, wheel/sdist; zero required runtime deps','Host discovery, tools and model remain separate.'),
        ('Managed updates and provenance','File digests, staging/recovery, retained source notices','Recovery is tested; one synced-folder Windows failure remains.'),
        ('Reviewable evidence','300 full-run answers + 6 adaptive follow-up answers','A transparent pilot; not an independent or statistical ranking.')]
    for i,row in enumerate(products):columns(ax,product_widths,584+i*33,33,row,['#ffffff' if i%2==0 else '#edf1f5']*3,14)
    rect(ax,40,769,1840,91,'#e9f3f1')
    text(ax,56,791,'FINAL FOLLOW-UP - KEPT SEPARATE',13,TEAL,'bold')
    text(ax,56,820,'Both IDEs: final allocation code passes 16/16 frozen + 3/3 added cases; both arithmetic answers are correct.',19,weight='bold')
    text(ax,56,843,'Known-task follow-up, not unseen evaluation. Throughput coverage is still incomplete; final UI rendering remains unmeasured.',14,MUTED)
    rect(ax,40,878,1840,64,'#fff1dd')
    text(ax,56,900,'OPENAI / CODEX SKILL CATALOG: NOT BENCHMARKED    |    PLOTLY-SPECIFIC SKILLS: NOT BENCHMARKED',17,GOLD,'bold')
    text(ax,56,925,'No invented scores or feature superiority claims are assigned to these untested comparisons. The tested reference library is mapped by category.',14,MUTED)
    footnotes(ax,[
        '* Initial revised trial. Three entrypoints changed later. Published-reference conditions use different guides by category; raw source revisions are retained.',
        'One unblinded reviewer; one batch conversation per condition; no repeated-trial/no-skill estimate. Host/model/context and order can affect outcomes.',
        'Percentages are passed fixture/task checks, not universal intelligence, speed, security, visual quality or future success probabilities.',
        'Evidence: web-results/comparison/review-results.json, runs/, source-snapshots.json and release-verification.json. Publication remains held.'
    ],974)
    return save(fig,'gncore-executive-comparison-table')


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    raw=EVIDENCE/'review-results.json'
    data=json.loads(raw.read_text(encoding='utf-8'))
    RUNS.update({(r['host'],r['profile']):r for r in data['runs'] if r['split']=='holdout'})
    SOURCES.update({s['category']:s for s in json.loads((EVIDENCE/'source-snapshots.json').read_text(encoding='utf-8'))})
    assert len(RUNS)==6 and len(SOURCES)==30
    files,rows=category_table()
    files.extend(overview_table())
    with (OUT/'complete-comparison-table.csv').open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    manifest={'schema_version':1,'date':'2026-10-29','review_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),
              'files':files,'categories':30,'comparison_repositories':14,
              'metrics':'Saved task checks and fixture results only; not universal efficiency',
              'untested_comparisons':['Standalone OpenAI/Codex skill catalog','Plotly-specific skills'],
              'candidate':'Initial revised trial; final three-entrypoint adaptive follow-up separately labeled',
              'sources':['review-results.json','source-snapshots.json','runs/*/H04-exploratory.json','release-verification.json'],
              'feature_claims':'GNCore implementation facts, not assertions that competitors lack these capabilities'}
    (OUT/'image-provenance.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(manifest,indent=2))


if __name__=='__main__':main()
