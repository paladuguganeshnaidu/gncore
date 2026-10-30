"""Render one honest comparison graph and one landscape engineering PDF."""
import csv
import json
from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, Preformatted

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'web-results/improvement-cycle-1'
PDF=ROOT/'output/pdf/GNCore-skill-improvement-review.pdf'
INK='#172d40'; MUTED='#526577'; TEAL='#087e75'; ORANGE='#a36020'

def read(path):return json.loads(path.read_text(encoding='utf-8'))
def name(value):return value.replace('-',' ').title().replace('Ai ','AI ').replace('Mlops','MLOps').replace('Nlp','NLP').replace('Ux','UX').replace('Sre','SRE').replace('Devops','DevOps')
def score(case):return f"{case['percent']:.0f}% ({case['passed']}/{case['total']})" if case['complete'] else f"{case['passed']}/{case['total']} + open"

def graph(runs, final):
    labels=['Package tests passed','Declared resources verified','Installed files verified','Generated-code fixtures passed','Browser checks passed','Isolated answers captured*']
    values=[(151,152),(1660,1660),(1690,1690),(160,160),(20,24),(20,120)]
    detail=['151 / 152; 1 skipped','1,660 / 1,660','1,690 / 1,690','160 / 160','20 / 24; 4 unmeasured','20 / 120; not scored']
    fig,ax=plt.subplots(figsize=(19.2,10.8),dpi=100)
    fig.patch.set_facecolor('#f7f9fb');ax.set_facecolor('#f7f9fb')
    fig.subplots_adjust(left=.30,right=.87,top=.73,bottom=.24)
    fig.text(.055,.925,'GNCORE  /  INTERNAL ENGINEERING VALIDATION',fontsize=15,color=TEAL,weight='bold')
    fig.text(.055,.865,'Evidence progress, not product performance',fontsize=29,color=INK,weight='bold')
    fig.text(.055,.811,'Actual local checks | Each row has its own units | No overall quality percentage',fontsize=17,color=MUTED)
    ypos=list(range(6))
    for i,((p,n),y) in enumerate(zip(values,ypos)):
        v=100*p/n
        ax.barh(y,100,height=.52,color='#e4eaf0')
        ax.barh(y,v,height=.52,color=TEAL if i<4 else ORANGE,hatch='///' if i==5 else None)
        ax.text(101.5,y,f'{v:.1f}%',va='center',fontsize=16,color=INK,weight='bold')
        ax.text(2,y-.32,detail[i],va='center',fontsize=11,color=MUTED)
    ax.set(yticks=ypos,yticklabels=labels,xlim=(0,117),xticks=[0,25,50,75,100],ylim=(5.6,-.8))
    ax.tick_params(axis='y',length=0,labelsize=15,pad=14,labelcolor=INK)
    ax.tick_params(axis='x',length=0,labelsize=12,labelcolor=MUTED)
    ax.set_xlabel('Completed or passed / planned items in that row (%)',fontsize=13,color=MUTED,labelpad=12)
    ax.grid(axis='x',color='#e0e7ed',lw=.7);ax.set_axisbelow(True)
    for spine in ax.spines.values():spine.set_visible(False)
    fig.text(.055,.15,'* The fair AI comparison stopped at the account usage limit. A >95% all-domain quality result is not established.',fontsize=15,color=INK)
    fig.text(.055,.105,'Earlier shared-context answer scores are development evidence only; they are withdrawn from quality comparisons.',fontsize=14,color=MUTED)
    fig.text(.055,.06,'The 160 code fixtures test inspected development artifacts; they do not prove which guide caused the result. Narrow UI checks remain open.',fontsize=13,color=MUTED)
    target=OUT/'verified-evidence-1920x1080.png';fig.savefig(target,dpi=100);plt.close(fig)
    (OUT/'verified-evidence-chart.json').write_text(json.dumps([{'label':label,'completed_or_passed':p,'planned':n,'percent':100*p/n} for label,(p,n) in zip(labels,values)],indent=2)+'\n')
    return target,values

def main():
    runs={r['profile']:r for r in read(OUT/'review-results.json')['runs']}
    final=read(OUT/'final-candidate-results.json')
    sizes=read(OUT/'final-entrypoint-sizes.json')
    integrity=read(OUT/'candidate-integrity.json')
    release=read(OUT/'distribution-verification.json')
    sources=read(OUT/'downloaded-reference-guides.json')
    graph_path,values=graph(runs,final)
    PDF.parent.mkdir(parents=True,exist_ok=True)
    styles=getSampleStyleSheet()
    for key in ('BodyText','Normal'):
        styles[key].fontName='Helvetica';styles[key].fontSize=10;styles[key].leading=14;styles[key].textColor=colors.HexColor(INK)
    styles.add(ParagraphStyle(name='TitleGN',fontName='Helvetica-Bold',fontSize=23,leading=28,textColor=colors.HexColor(INK),spaceAfter=10))
    styles.add(ParagraphStyle(name='KickerGN',fontName='Helvetica-Bold',fontSize=9,leading=12,textColor=colors.HexColor(TEAL),spaceAfter=7))
    styles.add(ParagraphStyle(name='SmallGN',fontSize=8,leading=10.5,textColor=colors.HexColor(MUTED)))
    styles.add(ParagraphStyle(name='CellGN',fontSize=8.2,leading=10,textColor=colors.HexColor(INK)))
    styles.add(ParagraphStyle(name='HeadGN',fontName='Helvetica-Bold',fontSize=14,leading=18,spaceBefore=10,spaceAfter=6,textColor=colors.HexColor(INK)))
    story=[]
    def p(text,style='BodyText'):return Paragraph(text,styles[style])
    def title(kicker,text):story.extend([p(kicker,'KickerGN'),p(text,'TitleGN')])
    def body(text):story.extend([p(text),Spacer(1,8)])
    def table(rows,widths,font=8.2,padding=4):
        data=[[p(str(v),'CellGN') for v in row] for row in rows]
        t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e4eeef')),('VALIGN',(0,0),(-1,-1),'TOP'),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f5f7f9')]),('LINEBELOW',(0,0),(-1,0),.6,colors.HexColor('#b8cbd1')),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),padding),('BOTTOMPADDING',(0,0),(-1,-1),padding)]))
        return t
    title('GNCORE / LOCAL REVIEW / 7.0.0rc1','Skill improvement review')
    body('All 30 developer domains were revised and the local package checks passed. A fair AI-quality comparison remains incomplete after an account usage limit. This report separates verified engineering work from unproven performance claims.')
    story.append(Image(str(graph_path),width=745,height=419.06))
    # The figure contains its own complete scope notes; keep the first page sparse.
    story.append(PageBreak())
    title('COMPLETE DOMAIN TABLE','Verified build status; quality target still open')
    body('Every category passed the applicable catalog/merge checks and installation verification. These check files and structure, not AI effectiveness. No domain currently has a completed fair >95% comparative quality measurement in this cycle.')
    catalog=read(ROOT/'catalog/categories.json')['categories']
    evidence={'code-build':'19/19 allocation fixtures','neural-networks':'14/14 math fixtures','testing':'7/7 checker fixtures','web-frontend':'5 UI checks passed; 1 open'}
    rows=[['Domain','Workflows','Bundle checks','Additional executed task evidence*','AI quality >95%']]
    csvrows=[]
    for category in sorted(catalog,key=lambda x:x['id']):
        row=[name(category['id']),str(len(category['workflows'])),'Passed',evidence.get(category['id'],'No domain runtime measurement'),'Unproven']
        rows.append(row);csvrows.append([category['id'],len(category['workflows']),'passed',row[3],'not-established'])
    with (OUT/'verified-domain-table.csv').open('w',encoding='utf-8',newline='') as handle:
        writer=csv.writer(handle);writer.writerow(['domain','workflows','bundle_checks','executed_task_evidence','ai_quality_gt95']);writer.writerows(csvrows)
    story.append(table(rows,[181,65,95,260,128],padding=1.25))
    story.append(Spacer(1,7))
    story.append(p('* Executed examples are synthetic development artifacts, not full real-project evaluations. Each of four development conditions passed the listed code fixtures and five browser checks; four narrow-layout checks remain unmeasured. The fair fresh-context comparison is incomplete.','SmallGN'))
    story.append(PageBreak())
    title('WHAT / WHY / WHERE','A lighter entrypoint, with stronger completion rules')
    body(f"Each domain now has a short task-selection guide, category-specific failure boundaries and a map into a hashed WORKFLOWS.md resource. Main entrypoints decreased from {sizes['before_bytes']:,} to {sizes['after_bytes']:,} bytes ({sizes['reduction_percent']:.1f}% smaller). This measures file bytes only; conditional resources still consume context when read.")
    story.append(table([['Change','Reason','Location'],
      ['Completion boundaries in all 30 domains','Infer essential missing requirements while preserving the requested stack, public API and scope.','catalog/category-completion-checks.json'],
      ['Conditional procedures in all 30 domains','Read the matching workflow and necessary references instead of every procedure by default.','scripts/build_catalog.py; each category/WORKFLOWS.md'],
      ['Ten procedure refinements; eight discovery summaries','Correct actual scope/correctness problems and contradictory discovery text; retain before/after lineage.','workflow-quality-changes.json; migration quality_revisions'],
      ['Three focused completion refinements','Explicit runtime secrets; a runnable, honest documentation example; actual native ABI boundary rules.','focused-guidance-changes.json; focused-review-notes.json']],[195,330,216],padding=6))
    story.append(Spacer(1,8))
    story.append(p('Concrete procedure corrections','HeadGN'))
    corrections=[['Area','Correction'],['Frontend / design','Remove a fixed organic theme; route actual workflow sections; require designer handoff only when applicable.'],['Automation / databases','Honor existing authorization; coordinate old/new writers and resumable reconciliation before contraction.'],['Python / releases','Build the wheel from its sdist; promote the same verified bytes once per intended target.'],['Spatial / neural / native work','Allow suitable geodesic methods; freeze stochastic state for relevant gradient checks; separate checkable pointer bounds from caller provenance obligations.']]
    story.append(table(corrections,[195,546],padding=5))
    body('The merge check retained all 374 workflow IDs: 364 procedures are unchanged and 10 have reviewed revisions. Existing resource declarations and source licenses are preserved. Long files alone are not treated as evidence of quality.')
    story.append(PageBreak())
    title('BUILD / TEST / INSTALL','What was actually executed')
    rows=[['Check','Observed result','Practical limit'],
      ['Final full Python suite','151 passed; 1 skipped','Local Windows/Python 3.14. Symlink creation was unavailable; this is not a full platform/interpreter matrix.'],
      ['Catalog and merge integrity','30 categories; 374 workflows; 1,660 resources verified; 73 helpers parsed','Hash/link/procedure and syntax checks; upstream helpers were not executed.'],
      ['Generated allocation code','16/16 frozen cases + 3/3 exploratory cases, in all four development conditions','Pure synthetic integer allocation; no general code-quality percentage.'],
      ['Generated neural-network math','14/14 cases, in all four conditions','CPU Python loss/gradient fixtures including central differences; no GPU training result.'],
      ['Generated contract checkers','7/7 fixtures, in all four conditions','Correct implementation plus six seeded mutants; not real-project bug-finding recall.'],
      ['Generated offline web pages','5/5 real browser checks in all four conditions','Blank/invalid/valid gating, selected confirmation and keyboard focus. 390px could not be established.'],
      ['Focused documentation example','Copied offline example executed successfully','Acceptance/pending/duplicate/completed assertions. No real HTTP contract verification.'],
      ['Built and installed distributions',f"Wheel built from sdist; Twine checks passed; {release['installed_files']:,} installed files verified",'Isolated installed import, source/resource byte comparison, directory export and portable ZIP; no upload.']]
    story.append(table(rows,[185,265,291],padding=6))
    story.append(Spacer(1,8))
    body('Generated-code tests and browser observations are real, but the development agents were not uniformly isolated from prior chat context. These artifact results do not establish a causal skill benefit. Security findings were static development review only; broad vulnerability detection and production security were not measured.')
    body('The first oracle rejected valid integer subclasses, and the inspector initially rejected benign error formatting. Both harness problems were corrected uniformly; original logs remain available. Neither correction is counted as a GNCore skill gain.')
    story.append(PageBreak())
    title('RESEARCH SOURCES / COMPARISON PENDING','Thirty matched guides from fourteen repositories')
    story.append(p('Pinned source entrypoints were downloaded again and checked against the recorded snapshots after CRLF/LF normalization. This is task-matched comparison, not a ranking of companies, Codex, Plotly, or every available skill. Reference helpers were not executed. Click a source to inspect its exact revision.','SmallGN'))
    story.append(Spacer(1,8))
    rows=[['GNCore domain','Matched repository / entrypoint','Pinned revision']]
    for source in sorted(sources,key=lambda x:x['category']):
        label=source['repo']+' / '+source['entrypoint'].replace('/SKILL.md','').replace('SKILL.md','root')
        rows.append([name(source['category']),f'<link href="{escape(source["url"])}" color="{TEAL}">{escape(label)}</link>',source['revision'][:12]])
    story.append(table(rows,[181,450,110],padding=1.0))
    story.append(Spacer(1,8))
    story.append(p('Original GNCore guidance is MIT-licensed. Retained upstream content keeps its own authorship and license obligations, including share-alike where applicable. Downloading or renaming another author\'s guide does not confer exclusive ownership. Sources without clear redistribution permission remain review inputs, not newly imported GNCore content.','SmallGN'))
    story.append(PageBreak())
    title('INTERPRETATION / REPRODUCTION','What the results establish - and what remains open')
    body('The requested >95% AI-quality target has not been established. Some development agents inherited parent chat history that could expose prior analysis or answers. Their rubric percentages are therefore withdrawn from headline comparisons. The raw answers, reviewer decisions and targeted corrections remain preserved as development evidence, not a fair leaderboard.')
    body('A replacement balanced comparison was frozen with explicit fresh-context agents (fork_turns=none), the same task/schema and dispatch template for each condition, and no further source tuning. The account usage limit stopped that attempt: 20 of 120 planned answers were captured, all from two baseline batches. There is no complete revised/reference/control arm and no valid comparative score. The pending state and saved inputs are recorded in isolated/STATUS.json and input-manifest.json.')
    body('The tasks are known H01-H30 cases, so even a completed replay would be adaptive regression, not new generalization evidence. A fixed served-model ID was not recorded; no repeated-trial uncertainty or external human audit is available. Historical VS Code/Copilot and Antigravity evidence stays separate in web-results/comparison; this cycle did not rerun IDE inference. Earlier natural-language routing remains 18/30. Native, embedded, GPU, deployed-service and full accessibility outcomes remain unmeasured.')
    story.append(p('Reproduce and inspect','HeadGN'))
    commands='python scripts/build_catalog.py --check\npython scripts/check_improvement_candidate.py\npython -m pytest -q\npython scripts/compile_improvement_reviews.py\npython scripts/compile_improvement_followup.py\npython scripts/report_improvement_cycle.py'
    story.append(Preformatted(commands,ParagraphStyle(name='CodeGN',fontName='Courier',fontSize=8,leading=11,textColor=colors.HexColor(INK),backColor=colors.HexColor('#f1f5f7'),borderPadding=7)))
    story.append(Spacer(1,8))
    body('Current evidence: verified-domain-table.csv; verified-evidence-chart.json; candidate-integrity.json; final-tests.txt; per-run executable/browser logs; distribution-verification.json; isolated/STATUS.json. Earlier review-results.json and final-candidate-results.json are explicitly marked development-only. They must not be cited as independent quality results.')
    body('Resume the frozen fresh-context comparison when inference capacity is available; retain any misses. Then use newly authored tasks, repeated model/host runs and blinded independent review. Re-establish 390px rendering and improve the 18/30 natural-language router before broader claims. This is local development validation, not exact-commit remote CI or a published release. GitHub, PyPI and website publication remain held for review and destination approval.')
    manifest='; '.join(f'{key}: {value["sha256"][:20]}...' for key,value in release['artifacts'].items())
    story.append(p('Local artifact fingerprints (full digests in distribution-verification.json): '+escape(manifest),'SmallGN'))
    completion=read(ROOT/'catalog/category-completion-checks.json')
    categories=sorted(completion)
    for offset in range(0,30,8):
        story.append(PageBreak())
        title('DOMAIN REVIEW APPENDIX',f'Completion boundaries - {offset+1} to {min(offset+8,30)}')
        body('These are the reviewed instructions added to the domain guides. They describe required engineering behavior; their presence alone is not a measured runtime outcome. Apply only the checks relevant to the requested task.')
        rows=[['Domain','Added completion boundaries']]
        for category in categories[offset:offset+8]:
            rows.append([name(category),'<br/>'.join(escape(item) for item in completion[category])])
        story.append(table(rows,[181,560],padding=3))
    def footer(canvas,doc):
        canvas.setStrokeColor(colors.HexColor('#d6e0e7'));canvas.line(35,28,807,28)
        canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor(MUTED))
        canvas.drawString(35,17,'GNCore internal engineering validation | Local candidate | Publication held')
        canvas.drawRightString(807,17,str(doc.page))
    doc=SimpleDocTemplate(str(PDF),pagesize=landscape(A4),leftMargin=35,rightMargin=35,topMargin=30,bottomMargin=37,title='GNCore skill improvement review',author='GNCore engineering')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    (OUT/'README.md').write_text('''# Revised skill build: verified work and open comparison

All 30 developer domains were revised, with 374 workflow IDs preserved. The requested greater-than-95% comparative AI-quality result is **not established**.

The complete [landscape PDF](../../output/pdf/GNCore-skill-improvement-review.pdf) contains one [1920x1080 evidence graph](verified-evidence-1920x1080.png), the [30-domain table](verified-domain-table.csv), research sources, implementation changes, actual checks and every domain's completion boundaries.

| Verified local work | Result |
| --- | --- |
| Final Python suite | 151 passed, 1 skipped |
| Catalog audit | 30 categories, 374 workflows, 1,660 resources; no issues |
| Project installation | 1,690 files; no missing/modified/unmanaged files |
| Inspected development code | 160/160 executable fixtures passed across four conditions |
| Offline UI artifacts | 20 browser checks passed; four narrow-layout checks unmeasured |
| Local distributions | Wheel built from sdist; metadata, installed import and source/resource comparisons passed |
| Fair AI comparison | Incomplete: 20 of 120 planned answers captured before account usage limit |

## What changed

- Add relevant completion boundaries in all 30 domains, including compatibility, identity, data leakage, numerical correctness, lifecycle/recovery and honest verification.
- Move detailed procedures to declared, hashed WORKFLOWS.md resources. Main entrypoint bytes decrease 43.2%; no token, cost or latency savings are claimed.
- Refine ten procedures and eight discovery summaries with explicit previous/current lineage. Preserve all existing workflow IDs, resource declarations and license obligations.
- Add focused guidance for runtime secrets, copyable examples under incomplete contracts, and concrete native null/length/error rules.

## Why quality percentages are withheld

Some initial development agents inherited parent chat history, potentially exposing prior analysis or answers. Their numeric rubric results are withdrawn from fair quality comparisons. Raw answers and decisions remain in internal-*-batch-*.json, review-results.json and final-candidate-results.json, all explicitly development-only. Actual generated-code execution and browser observations remain valid within their narrow scopes; they do not establish which guide caused success.

A replacement comparison explicitly used fork_turns=none and the same dispatch template in every condition. The account usage limit stopped it after two baseline batches (20 answers); no balanced comparison is available. See isolated/STATUS.json and isolated/input-manifest.json. No inference retries were attempted after the limit. The frozen inputs support a later continuation without tuning to a target score.

## Evidence and limitations

candidate-integrity.json and workflow-quality-changes.json retain exact merge lineage. focused-guidance-changes.json retains the adaptive text changes. final-tests.txt, final-catalog-audit.json, project-verification.json and distribution-verification.json record executed checks. Per-run executable/browser logs are under runs/. first-candidate-guides/ preserves the guides before focused correction.

Thirty pinned reference guides from fourteen repositories were downloaded and content-checked after CRLF/LF normalization; hashes and exact source links are in downloaded-reference-guides.json. They are research inputs, not exclusively GNCore-owned content. No upstream helper was executed.

The port oracle and artifact inspector required documented corrections; original rejected results remain available. Harness repairs are not skill gains. The known-task replay cannot establish unseen generalization, production reliability or vendor superiority. Historical VS Code/Antigravity results remain separate in ../comparison/; this cycle did not rerun IDE inference. Earlier natural-language routing remains 18/30. GPU, native/embedded runtime, deployed services and full accessibility remain unmeasured.

GitHub, PyPI and website publication are held. Exact-commit remote CI, broader platform/interpreter checks, completed fresh-context evaluation and remaining UI validation are still needed before release claims.
''',encoding='utf-8')
    print(json.dumps({'pdf':str(PDF),'graph':str(graph_path),'scope':'Verified engineering evidence; fair AI comparison incomplete. No greater-than-95% quality claim.'}))

if __name__=='__main__':main()
