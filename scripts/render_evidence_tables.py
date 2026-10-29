"""Render Full HD evidence tables from saved pilot results; perform no inference."""
from __future__ import annotations
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Rectangle, FancyBboxPatch

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "web-results/comparison"
OUT = EVIDENCE / "tables"
WIDTH, HEIGHT = 1920, 1080
INK, MUTED = "#14263b", "#546477"
TEAL, NAVY = "#007b70", "#122d47"
PALE, LINE, AMBER = "#edf7f4", "#dce4eb", "#92551c"
PROFILES = ("gncore-before", "reference", "gncore-after")
HOSTS = ("vscode", "antigravity")
LABELS = ("Original", "Reference", "Revised trial")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text(ax, x, y, value, size=20, color=INK, weight="normal", align="left"):
    return ax.text(x, y, value, fontsize=size * .72, color=color,
                   weight=weight, ha=align, va="top", linespacing=1.35)


def rect(ax, x, y, w, h, color, radius=0):
    patch = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                           facecolor=color, edgecolor="none") if radius else Rectangle((x, y), w, h, facecolor=color, edgecolor="none")
    ax.add_patch(patch)


def canvas():
    fig = plt.figure(figsize=(19.2, 10.8), dpi=100, facecolor="#f7f9fb")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set(xlim=(0, WIDTH), ylim=(HEIGHT, 0))
    ax.axis("off")
    return fig, ax


def pct(p, n):
    return f"{100*p/n:.1f}%" if n else "Not measured"


def counted(p, n):
    return f"{pct(p,n)}  ({p}/{n})"


def save(fig, name):
    for suffix, dpi in (("full-hd", 100), ("4k", 200)):
        fig.savefig(OUT / f"{name}-{suffix}.png", dpi=dpi, facecolor=fig.get_facecolor())
    fig.savefig(OUT / f"{name}.svg", facecolor=fig.get_facecolor())
    plt.close(fig)


def name(category):
    names = {"ai-engineering": "AI engineering", "cloud-devops-sre": "Cloud / DevOps / SRE",
             "natural-language-processing": "Natural language processing", "mlops": "MLOps",
             "design-ux": "Design / UX"}
    return names.get(category, category.replace("-", " ").capitalize())


def reference_name(repo):
    return {"anthropics/skills": "Anthropic", "vercel-labs/agent-skills": "Vercel",
            "microsoft/skills": "Microsoft", "google/skills": "Google",
            "huggingface/skills": "Hugging Face", "trailofbits/skills": "Trail of Bits",
            "obra/superpowers": "Superpowers", "affaan-m/ecc": "ECC",
            "K-Dense-AI/scientific-agent-skills": "K-Dense scientific",
            "supabase/agent-skills": "Supabase", "cloudflare/skills": "Cloudflare",
            "temporalio/skill-temporal-developer": "Temporal",
            "beriberikix/zephyr-agent-skills": "Zephyr agent skills",
            "minhhoit/gamedev-agent-skills": "Game-dev agent skills"}[repo]


def header(ax, title, subtitle):
    rect(ax, 0, 0, WIDTH, 10, TEAL)
    text(ax, 38, 29, "GNCORE  /  RECORDED COMPARISON", 18, TEAL, "bold")
    text(ax, 1880, 29, "29 OCTOBER 2026  |  LOCAL CANDIDATE", 16, MUTED, align="right")
    text(ax, 38, 65, title, 39, INK, "bold")
    text(ax, 38, 119, subtitle, 20, MUTED)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for path in ("C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/segoeuib.ttf"):
        if Path(path).exists():
            font_manager.fontManager.addfont(path)
    plt.rcParams["font.family"] = "Segoe UI" if Path("C:/Windows/Fonts/segoeui.ttf").exists() else "DejaVu Sans"
    data = read(EVIDENCE / "review-results.json")
    sources = {x["category"]: x for x in read(EVIDENCE / "source-snapshots.json")}
    runs = {(r["host"], r["profile"]): r for r in data["runs"] if r["split"] == "holdout"}
    assert set(runs) == {(h,p) for h in HOSTS for p in PROFILES}
    cases = {key: {c["category"]: c for c in value["cases"]} for key, value in runs.items()}
    assert all(len(c)==30 for c in cases.values())

    totals = {}
    for key, by_category in cases.items():
        selected = [c for c in by_category.values() if c["category"] != "web-frontend"]
        assert len(selected)==29 and all(c["complete"] for c in selected)
        totals[key] = (sum(c["passed"] for c in selected), sum(c["total"] for c in selected))

    fig, ax = canvas()
    header(ax, "How GNCore compares: measured results, visible limits",
           "Same holdout tasks within each IDE. Percentages mean checks passed, not universal efficiency or security.")
    for x, host, label in ((38,"vscode","ORIGINAL VS CODE / COPILOT"), (972,"antigravity","ANTIGRAVITY IDE")):
        rect(ax, x, 165, 910, 115, NAVY, 12)
        text(ax, x+22, 180, label, 17, "#c4d6e4", "bold")
        p,n=totals[host,"gncore-after"]
        rp,rn=totals[host,"reference"]
        text(ax, x+22, 210, pct(p,n), 39, "#ffffff", "bold")
        text(ax, x+190, 215, f"Revised trial {p}/{n}   |   matched references {pct(rp,rn)} ({rp}/{rn})", 22, "#e0edf4")
    text(ax, 40, 298, "Published reference = a category-matched guide from 14 pinned repositories, not a score for an entire company.", 19, MUTED)

    edges = [38, 520, 747, 974, 1201, 1428, 1655, 1882]
    rect(ax, 38, 333, 1844, 43, NAVY)
    text(ax, 53, 344, "MEASUREMENT", 18, "white", "bold")
    text(ax, (520+1201)/2, 344, "VS CODE / COPILOT", 18, "white", "bold", "center")
    text(ax, (1201+1882)/2, 344, "ANTIGRAVITY", 18, "white", "bold", "center")
    rect(ax, 38, 376, 1844, 35, "#e7edf3")
    for i in range(6):
        text(ax, (edges[i+1]+edges[i+2])/2, 384, LABELS[i%3], 17, INK, "bold", "center")

    metric_rows = [
        ("Task decisions: 29 non-UI categories", "decisions"),
        ("Security: seeded defects identified", "security-found"),
        ("Security: proposed repairs accepted*", "security-repairs"),
        ("Security: safe cases wrongly flagged (lower is better)", "security-fp"),
        ("Allocation code: 16 frozen tests", "allocation"),
        ("Allocation code: 3 later regression tests", "allocation-extra"),
        ("Neural-network code: numerical tests", "numeric"),
        ("Test quality: correct + six faulty implementations", "tests"),
        ("Held-out UI / time-cost efficiency", "unmeasured"),
    ]
    metric_export=[]
    for row,(label,kind) in enumerate(metric_rows):
        y=411+row*42
        rect(ax,38,y,1844,42,"white" if row%2==0 else "#f0f4f7")
        text(ax,53,y+12,label,17 if len(label)>50 else 19,INK,"bold" if row==0 else "normal")
        for i,(host,profile) in enumerate((h,p) for h in HOSTS for p in PROFILES):
            case=cases[host,profile]
            p=n=None
            if kind=="decisions":p,n=totals[host,profile]
            elif kind.startswith("security"):
                s=case["cybersecurity"]["security"]
                p,n={"security-found":(s["found"],s["seeded"]),"security-repairs":(s["repairs_passed"],s["repairs_total"]),"security-fp":(s["safe_controls_flagged"],s["safe_controls"])}[kind]
            elif kind=="allocation-extra":
                v=read(EVIDENCE/"runs"/runs[host,profile]["run"]/"H04-exploratory.json");p,n=v["passed"],v["total"]
            elif kind in {"allocation","numeric","tests"}:
                v=case[{"allocation":"code-build","numeric":"neural-networks","tests":"testing"}[kind]]["execution"]
                assert not v["error"];p,n=v["passed"],v["total"]
            value="Not measured" if n is None else counted(p,n)
            color=MUTED if n is None or kind=="security-fp" else AMBER if p<n else TEAL
            text(ax,(edges[i+1]+edges[i+2])/2,y+12,value,18,color,"bold" if row==0 else "normal","center")
            metric_export.append({"metric":kind,"host":host,"profile":profile,"passed_or_flagged":p,"total":n,"display":value})

    text(ax, 40, 803, "VERIFIED GNCORE FEATURES  /  These are implementation facts; competitor feature absence was not audited.", 17, TEAL, "bold")
    for x,title,body in [(38,"ONE INVOCATION PER DOMAIN","30 categories / 374 workflows\nTask-specific modes and inferred UI direction"),
                         (662,"PORTABLE, REVIEWABLE EXPORTS","No mandatory runtime dependencies\nHashes, recovery journals and source notices"),
                         (1286,"EVIDENCE INCLUDED","Raw answers, failures and executable fixtures\n1,660 installed files verified")]:
        rect(ax,x,832,596,96,PALE,10)
        text(ax,x+16,846,title,18,TEAL,"bold")
        text(ax,x+16,874,body,18,INK)
    rect(ax,38,944,1844,45,"#fff3df",8)
    text(ax,54,955,"Plotly-related skills and standalone Codex skills: NOT MEASURED. No direct superiority claim is supported.",21,AMBER,"bold")
    text(ax,40,1002,"* Security repairs were manually reviewed; exploits were not executed. All rows use the initial revised trial, not the final follow-up.",17,MUTED)
    text(ax,40,1027,"Single unblinded pilot; host/model/context effects are uncontrolled. Final allocation follow-ups pass 16/16 + 3/3 in both IDEs.",17,MUTED)
    text(ax,40,1052,"Source: web-results/comparison/review-results.json + raw test logs. VS Code/Copilot testing is not a Codex-skill benchmark.",16,MUTED)
    save(fig,"gncore-executive-comparison")

    fig,ax=canvas()
    header(ax,"All 30 categories: GNCore and matched published references",
           "Recorded holdout task-check percentages, with raw counts. Original = frozen GNCore; Revised = initial revised trial.")
    edges=[38,344,700,897,1094,1291,1488,1685,1882]
    rect(ax,38,166,1844,40,NAVY)
    text(ax,52,177,"GNCORE CATEGORY",18,"white","bold")
    text(ax,358,177,"MATCHED REFERENCE SOURCE",18,"white","bold")
    text(ax,(700+1291)/2,177,"VS CODE / COPILOT",18,"white","bold","center")
    text(ax,(1291+1882)/2,177,"ANTIGRAVITY",18,"white","bold","center")
    rect(ax,38,206,1844,35,"#e7edf3")
    text(ax,52,215,"One distinct task per category",16,MUTED)
    text(ax,358,215,"Different guide for each row",16,MUTED)
    for i in range(6):text(ax,(edges[i+2]+edges[i+3])/2,215,LABELS[i%3],17,INK,"bold","center")
    category_export=[]
    for row,category in enumerate(sorted(sources)):
        y=241+row*24
        rect(ax,38,y,1844,24,"white" if row%2==0 else "#edf2f6")
        text(ax,52,y+4,name(category),18)
        text(ax,358,y+4,reference_name(sources[category]["repo"]),18,MUTED)
        record={"category":category,"reference_repository":sources[category]["repo"],"reference_url":sources[category]["url"]}
        for i,(host,profile) in enumerate((h,p) for h in HOSTS for p in PROFILES):
            c=cases[host,profile][category]
            value=counted(c["passed"],c["total"]) if c["complete"] else "Not measured"
            color=MUTED if not c["complete"] else TEAL if c["passed"]==c["total"] else INK
            text(ax,(edges[i+2]+edges[i+3])/2,y+4,value,17,color,align="center")
            record[host+"_"+profile]=value
        category_export.append(record)
    text(ax,40,980,"Not measured: web-frontend needs rendered holdout checks; its one static check is not shown as a complete score.",18,MUTED)
    text(ax,40,1006,"Six checks per task; H14 has five applicable checks in every arm. Published sources span 14 repositories; this is not a publisher-wide ranking.",17,MUTED)
    text(ax,40,1032,"Manual, unblinded, single-task pilot. No repeated trials or no-added-skill controls. Plotly / standalone Codex collections were not tested.",17,MUTED)
    text(ax,40,1056,"Final code-build, performance and frontend entrypoints have separate adaptive evidence; these scores retain the original trial's failures.",16,MUTED)
    save(fig,"gncore-all-category-comparison")

    for filename,rows in (("metric-table.csv",metric_export),("all-category-table.csv",category_export)):
        with (OUT/filename).open("w",encoding="utf-8",newline="") as stream:
            writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    manifest={"generated_from":{"review_results_sha256":digest(EVIDENCE/"review-results.json"),"source_snapshot_sha256":digest(EVIDENCE/"source-snapshots.json")},
              "full_hd_pixels":[1920,1080],"master_pixels":[3840,2160],"holdout_categories":30,
              "fully_measured_non_ui_categories":29,"reference_repositories":len({x["repo"] for x in sources.values()}),
              "unmeasured_comparators":["Plotly-related skills (unspecified collection)","Standalone Codex skill collection"],
              "inference_runs_performed":0,"outputs":{p.name:digest(p) for p in sorted(OUT.glob("*.png"))}}
    (OUT/"image-provenance.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(manifest,indent=2))


if __name__=="__main__":main()
