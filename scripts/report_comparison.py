"""Render evidence-backed landscape scorecards and two audience reports."""
from __future__ import annotations
import csv
import hashlib
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "web-results/comparison"
PLOTS = OUT / "charts"
LABELS = {"gncore-before": "GNCore before", "reference": "Published reference", "gncore-after": "Revised GNCore trial"}
COLORS = {"gncore-before": "#708297", "reference": "#c08345", "gncore-after": "#157a70"}
ORDER = list(LABELS)

def pct(passed, total):
    return 100*passed/total if total else None

def score(case):
    return pct(case["passed"], case["total"]) if case["complete"] else None

def simple_name(name):
    return name.replace("-", " ").title().replace("Ai ", "AI ").replace("Mlops", "MLOps").replace("Nlp", "NLP")

def metric(case, kind):
    record = case.get(kind)
    if not record or record.get("error") or not record.get("total"):
        return None
    return record["passed"], record["total"]

def panel(ax, title, values, subtitle):
    ax.set_title(title, loc="left", fontsize=12, fontweight="bold", pad=17)
    ax.text(0, 1.035, subtitle, transform=ax.transAxes, fontsize=8, color="#5e6a78")
    for i, profile in enumerate(ORDER):
        value = values.get(profile)
        if value is None:
            ax.barh(i, 100, color="#eef0f2", height=.54)
            ax.text(2, i, "Not measured", va="center", fontsize=9, color="#73808e")
        else:
            p, n = value
            v = pct(p,n)
            ax.barh(i, v, color=COLORS[profile], height=.54)
            ax.text(min(v+2,101), i, f"{v:.0f}%  ({p}/{n})", va="center", fontsize=9)
    ax.axvline(95, color="#9b4557", lw=1, ls=(0,(3,3)), zorder=0)
    ax.set(yticks=range(3), yticklabels=[LABELS[p] for p in ORDER], xlim=(0,135), xticks=[0,50,100])
    ax.invert_yaxis()
    ax.grid(axis="x",color="#e9edf1",linewidth=.6)
    ax.set_axisbelow(True)
    ax.tick_params(axis="both", length=0, labelsize=8)
    for spine in ax.spines.values():spine.set_visible(False)

def sheet(data, host, split):
    runs = {r["profile"]:r for r in data["runs"] if r["host"]==host and r["split"]==split}
    cats = sorted({c["category"] for r in data["runs"] for c in r["cases"]})
    cases = {p:{c["category"]:c for c in r["cases"]} for p,r in runs.items()}
    fig=plt.figure(figsize=(16.54,11.69),facecolor="#fcfcfa")
    fig.text(.045,.959,"GNCORE  /  PRACTICAL SKILL COMPARISON",fontsize=10,color="#157a70",weight="bold")
    fig.text(.045,.923,f"What passed, and what still needs work",fontsize=25,weight="bold",color="#192a3b")
    host_label="Original Microsoft VS Code / Copilot Auto" if host=="vscode" else "Antigravity IDE / Gemini 3.8 Flash High"
    fig.text(.045,.895,f"{host_label}  |  {split.title()} tasks  |  30 developer categories",fontsize=11,color="#5e6a78")
    fig.text(.045,.873,"References: 14 pinned repositories, including Anthropic, Microsoft, Google, Hugging Face, Vercel and domain specialists.",fontsize=9,color="#5e6a78")
    grid=fig.add_gridspec(3,3,left=.10,right=.97,bottom=.12,top=.84,width_ratios=[1,1,1.43],wspace=.54,hspace=.66)
    panels=[("Defects correctly identified", "cybersecurity", "security", "Six seeded issues; manual review"),
            ("Code repair: frozen tests", "code-build", "execution", "Additional exploratory regressions are separate"),
            ("Numerical correctness", "neural-networks", "execution", "Loss, gradients, stability and validation"),
            ("Tests that catch bugs", "testing", "execution", "Correct implementation plus six mutants"),
            ("Web interface behavior", "web-frontend", "browser", "Form flow, focus and 390px layout"),
            ("Other task checks", None, "decisions", "29 non-UI categories; applicable reviewed criteria")]
    for index,(title,cat,kind,subtitle) in enumerate(panels):
        values={}
        for profile,by_cat in cases.items():
            if kind=="security":
                s=by_cat[cat].get("security")
                values[profile]=(s["found"],s["seeded"]) if s else None
            elif kind=="decisions":
                complete=[c for c in by_cat.values() if c["category"]!="web-frontend" and c["complete"]]
                # UI has its own panel; require all29 other categories in every arm.
                values[profile]=(sum(c["passed"] for c in complete),sum(c["total"] for c in complete)) if len(complete)==29 else None
            else:values[profile]=metric(by_cat[cat],kind)
        panel(fig.add_subplot(grid[index//2,index%2]),title,values,subtitle)
    ax=fig.add_subplot(grid[:,2])
    matrix=np.full((len(cats),3),np.nan)
    for i,cat in enumerate(cats):
        for j,p in enumerate(ORDER):
            if p in cases and cat in cases[p]:
                value=score(cases[p][cat])
                if value is not None:matrix[i,j]=value
    cmap=plt.get_cmap("YlGnBu").copy();cmap.set_bad("#e5e9ed")
    ax.imshow(matrix,aspect="auto",vmin=0,vmax=100,cmap=cmap)
    ax.set_title("All categories: task checks passed",loc="left",fontsize=12,weight="bold",pad=20)
    ax.set(yticks=range(len(cats)),yticklabels=[simple_name(c) for c in cats],xticks=range(3),xticklabels=["Before","Reference","Revised trial"])
    ax.tick_params(length=0,labelsize=8)
    ax.xaxis.tick_top()
    for i,cat in enumerate(cats):
        for j,p in enumerate(ORDER):
            value=matrix[i,j]
            cell=cases.get(p,{}).get(cat)
            label="N/A" if np.isnan(value) else f"{value:.0f}%  {cell['passed']}/{cell['total']}"
            ax.text(j,i,label,ha="center",va="center",fontsize=7.7,color="#fff" if not np.isnan(value) and value>70 else "#223344")
    for spine in ax.spines.values():spine.set_visible(False)
    fig.text(.045,.066,"Read the percentages as passed checks, not a universal efficiency or security rating. 95% dashed line = goal only.",fontsize=10,weight="bold",color="#24384b")
    fig.text(.045,.043,"Pilot: one task per category per split and condition; no repeated trials or significance claim. References vary by category. Gray = not measured.",fontsize=9,color="#5e6a78")
    fig.text(.045,.025,"Manual review is unblinded. Models/IDE context can affect results. Raw answers, criteria, source revisions and logs accompany this report. 29 October 2026.",fontsize=8,color="#5e6a78")
    name=f"{host}-{split}-landscape"
    for ext in ("png","svg","pdf"):
        fig.savefig(PLOTS/f"{name}.{ext}",dpi=180,facecolor=fig.get_facecolor())
    plt.close(fig)
    return name

def doc_pdf(path, title, paragraphs, images=(), technical=False):
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name="ReportBody",fontName="Helvetica",fontSize=10,leading=14,spaceAfter=8,textColor=colors.HexColor("#26394b")))
    styles.add(ParagraphStyle(name="SmallReport",fontName="Helvetica",fontSize=8,leading=11,spaceAfter=6))
    story=[Paragraph(escape(title),styles["Title"]),Spacer(1,12)]
    for heading,text in paragraphs:
        parts=text.split("\n\n")
        story.append(KeepTogether([Paragraph(escape(heading),styles["Heading2"]),Paragraph(escape(parts[0]),styles["ReportBody"])]))
        for para in parts[1:]:
            story.append(Paragraph(escape(para),styles["ReportBody"]))
    for name in images:
        story.extend([PageBreak(),Paragraph(name.replace("-"," ").title(),styles["Heading1"]),Image(str(PLOTS/f"{name}.png"),width=680,height=480)])
    def footer(canvas,document):
        canvas.saveState();canvas.setFont("Helvetica",8);canvas.setFillColor(colors.HexColor("#667789"));canvas.drawString(42,22,"GNCore / comparative pilot / publication held");canvas.drawRightString(800,22,str(document.page));canvas.restoreState()
    SimpleDocTemplate(str(path),pagesize=landscape(A4),rightMargin=42,leftMargin=42,topMargin=36,bottomMargin=34).build(story,onFirstPage=footer,onLaterPages=footer)

def main():
    PLOTS.mkdir(parents=True,exist_ok=True)
    data=json.loads((OUT/"review-results.json").read_text(encoding="utf-8"))
    sheets=[sheet(data,h,s) for s in ("holdout","development") for h in ("vscode","antigravity")]
    rows=[]
    for run in data["runs"]:
        for c in run["cases"]:
            rows.append({"host":run["host"],"profile":run["profile"],"split":run["split"],"category":c["category"],"passed":c["passed"],"total":c["total"],"complete":c["complete"],"percent":score(c)})
    with (OUT/"category-scores.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    failures=[{"run":r["run"],"category":c["category"],"criterion":ch["id"],"requirement":ch["requirement"],"evidence":ch["evidence"]}
              for r in data["runs"] for c in r["cases"] for ch in c["checks"] if ch["status"]=="fail"]
    with (OUT/"failed-checks.csv").open("w",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=["run","category","criterion","requirement","evidence"]);writer.writeheader();writer.writerows(failures)
    adaptive=json.loads((ROOT/"benchmarks/comparison/adaptive-followup-decisions.json").read_text(encoding="utf-8"))
    adaptive_lines=[]
    for run,notes in adaptive["reviews"].items():
        folder=OUT/"runs"/run
        for suffix,label in [("H04-tests.json","frozen allocation tests"),("H04-exploratory.json","exploratory allocation tests")]:
            result=json.loads((folder/suffix).read_text(encoding="utf-8"))
            host_name="VS Code" if run.startswith("vscode") else "Antigravity"
            adaptive_lines.append(f"{host_name}: {result['passed']}/{result['total']} {label} passed.")
        adaptive_lines.append(f"{host_name}: arithmetic is correct. The performance answer still omits throughput coverage. Browser behavior remains unmeasured.")
    summaries=[]
    for r in data["runs"]:
        complete=[c for c in r["cases"] if c["complete"]]
        p=sum(c["passed"] for c in complete);n=sum(c["total"] for c in complete)
        host_name="VS Code" if r["host"]=="vscode" else "Antigravity"
        summaries.append(f"{host_name}, {LABELS[r['profile']]}, {r['split']} tasks: {p}/{n} checks passed ({pct(p,n):.1f}%); {len(complete)}/30 categories fully measured.")
    exploratory=[]
    for path in sorted((OUT/"runs").glob("*/H04-exploratory.json")):
        record=json.loads(path.read_text(encoding="utf-8"))
        exploratory.append(f"{path.parent.name}: {record['passed']}/{record['total']} added allocation cases passed.")
    intro=[("What this tells you","This is a practical pilot of GNCore and a published reference for each of its 30 developer categories. Original Microsoft VS Code and Antigravity were tested separately. The charts show real saved answers, executed code tests and browser observations; a missing measurement stays gray. Development and holdout tasks are different and must not be subtracted to claim an improvement."),
           ("How to read a percentage","A result of 5/6 (83%) means five of six specific checks passed on one task. It does not mean the skill is 83% intelligent, an application is 83% secure, or that future tasks have an 83% success probability. The 95% line is an improvement target, never a value filled into the data."),
           ("Results currently supported","All 30 categories have saved answers in both IDEs. The main comparison uses the same holdout tasks for original GNCore, published references and the revised trial. Twenty-nine categories are fully reviewed; the web interface category still needs rendered checks. The four landscape sheets show every category, raw counts and percentages.\n\nDevelopment tasks were used to find weaknesses; holdout tasks were reserved for the next evaluation. The final three-case follow-up uses already known tasks and is reported separately."),
           ("Did the revised trial do better?","On the same holdout tasks, the 29 fully reviewed non-UI categories passed164/173 checks (94.8%) before and168/173 (97.1%) in the revised VS Code trial; the published references passed158/173 (91.3%). Antigravity passed140/173 (80.9%) before and147/173 (85.0%) in the revised trial; references passed132/173 (76.3%). These are single unblinded pilot observations, not statistically established gains or a universal ranking. Many individual categories remain below95%, and the initial revised trial is not the final three-entrypoint follow-up."),
           ("What changed","All 30 GNCore entrypoints gained original, domain-specific failure-prevention guidance. The work addresses recoverable retries, safe migration boundaries, model/data correctness, reproducible builds and visible UI focus. Existing workflows and upstream license notices remain intact. A text change is an implemented improvement to guidance; only a comparable held-out result can support an outcome-improvement claim."),
           ("A passing test suite still missed a bug","VS Code's initial revised allocation code passed all16 frozen cases but failed three added mixed-remainder cases. The original answer and failures are retained. These exploratory tests were added after inspecting the bug and are reported separately, not disguised as predeclared coverage. This is why100% on a small fixture cannot certify general correctness.\n\n"+"\n\n".join(exploratory)),
           ("What remains uncertain","There is one task variant per category and no repeated-trial estimate. Manual scoring is unblinded. The whole-library batch can create cross-task context and retrieval effects. Copilot Auto can choose models; these results cannot isolate a skill's causal effect from model knowledge. Final code-build, performance and frontend guidance changed after the first revised trial and receive a separate adaptive follow-up. The frontend style section was restored after a generation regression. These known-task follow-ups are not spliced into the original holdout scores. Browser use became disabled after the development tests; missing holdout UI evidence remains gray. This is not a broad ranking of publishers or a security certification. Visual beauty was not assigned a fabricated percentage."),
           ("Final guidance: separate follow-up","\n\n".join(adaptive_lines)+"\n\nBoth final allocation answers pass the added regressions, and both arithmetic answers give22.4 and28ms correctly. A known-task follow-up cannot establish generalization. The original VS Code baseline also exposed an extreme-logit neural-network failure (13/14 tests); initial revised and reference answers passed14/14 on that fixture. Earlier failures remain in the evidence."),
           ("Package and installation checks","The complete Python3.12 package suite passed148 tests with one skip when temporary test files were outside the sync folder. A run inside the synced repository passed147, failed one and skipped one after Windows access-denied journal replacement. Both logs remain. Bounded atomic replacement retries and permanent-failure preservation tests were added; the competing process was not identified. This does not prove every synced-folder installation succeeds."),
           ("Release decision","Keep release publication on hold while reviewing the evidence and remaining failures. Prepare and verify package and website artifacts before asking the owner for GitHub, PyPI and website publication approval.")]
    technical=intro+[("Experimental design","The frozen before revision is cd77d82. Sixty synthetic tasks and six checks per task were frozen before instruction improvements: 30 development and 30 holdout cases. Published guides cover 30 mappings from 14 repositories. Exact commits, entrypoint/support hashes, root and skill-specific license metadata are in source-snapshots.json. References were not relicensed as GNCore, and imported helpers were not executed."),
            ("Measurement and grading","Raw copied IDE responses are preserved, schema-validated and expanded into standalone generated artifacts. Eligible pure Python functions are inspected, checked with a narrow AST allowlist and run under an isolated child process with a five-second compute limit and separate Windows startup allowance. This is not a general security sandbox. Security findings and repairs are manually reviewed against seeded snippets; safe-control false positives are separate. The generated HTML is exercised in the real in-app browser at a 390px viewport, including invalid input, enabling, confirmation and visible radio focus."),
            ("Scoring details","Six frozen criteria per case are reviewed with explicit evidence. Two conditional development criteria are inapplicable in every arm: mutation retry identity for a read-only feed and dataset splitting for a hand-token-alignment example. The stale-writer holdout has no remote operation, so its unknown-remote-outcome check is also inapplicable in every arm. These exclusions are stated in the compiler. Percentages use applicable checks, with raw denominators visible. Missing or incomplete runs are not zero and are not silently averaged into a passing score. Functional tests, security recall, false positives and manual decisions remain different metrics. Overall raw-check totals weight each check equally; category rows expose the denominator differences."),
            ("Reproduction","Run scripts/compile_comparison_reviews.py, then scripts/report_comparison.py in an environment with Matplotlib, NumPy and ReportLab. Grading fixtures and immutable tasks are under benchmarks/comparison. Use scripts/import_comparison_response.py for a newly captured response, then scripts/grade_comparison_artifacts.py for inspected eligible artifacts. IDE inference itself requires the recorded fresh-session protocol and account/model availability; rerunning a reporting script does not reproduce the inference."),
            ("Limitations and threats to validity","The references are task-relevant examples rather than every publisher's best possible configuration. Some are narrower than the category. Offline guide-conditioned tasks do not exercise cloud deployment, hardware, GPU training, full tool integrations or complete project workflows. All 30 tasks share one conversation per condition, so they are not independent per-skill trials. Output budgets and varied document sizes can affect coverage. No no-added-skill control or repeated trials should be claimed unless a corresponding saved run exists. Small percentage differences are not evidence of statistical superiority."),
            ("Source map","\n\n".join(f"{x['category']}: {x['repo']} / {x['entrypoint']} / {x.get('revision','see source-snapshots.json')} / {x['url']}" for x in json.loads((OUT/"source-snapshots.json").read_text(encoding="utf-8"))))]
    for name,title,paras in [("EXECUTIVE-REPORT","GNCore: practical results explained",intro),("TECHNICAL-REPORT","GNCore: experiment, evidence and limits",technical)]:
        text="# "+title+"\n\n"+"\n\n".join("## "+h+"\n\n"+t for h,t in paras)+"\n"
        text=re.sub(r'(?<![<(])https://[^\s<>]+',lambda m:'<'+m[0]+'>',text)
        (OUT/f"{name}.md").write_text(text,encoding="utf-8",newline="\n")
        doc_pdf(OUT/f"{name}.pdf",title,paras,images=sheets if name.startswith("EXEC") else (),technical=name.startswith("TECH"))
    index={"generated_from":hashlib.sha256((OUT/"review-results.json").read_bytes()).hexdigest(),"scorecards":sheets,"plotted_values":"category-scores.csv and review-results.json","claims":"pilot task-check percentages only"}
    (OUT/"report-manifest.json").write_text(json.dumps(index,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(index,indent=2))

if __name__=="__main__":main()
