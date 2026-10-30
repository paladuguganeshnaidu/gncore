"""Measure all GNCore categories without claiming agent-output quality.

Run with an installed GNCore candidate or PYTHONPATH=src. Matplotlib is an
optional reporting dependency; raw results are written before plotting.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
from importlib.resources import files
import json
from pathlib import Path
import platform
import statistics
import sys
import time
from datetime import datetime, timezone

import gncore
from gncore.evaluation import load_corpus
from gncore.routing import route_task
from gncore.skills.bundles import packaged_resources
from gncore.skills.unified import unified_manifest

ROOT = Path(__file__).resolve().parents[1]


def measure(operation, repeats):
    operation()  # Exclude one warm-up; retain every timed sample.
    values = []
    for _ in range(repeats):
        start = time.perf_counter_ns()
        operation()
        values.append((time.perf_counter_ns() - start) / 1e6)
    ordered = sorted(values)
    return {"samples_ms": values, "median_ms": statistics.median(values),
            "p95_ms": ordered[max(0, int(.95 * len(values) + .999999) - 1)]}


def benchmark(output, repeats, installed_directory=None):
    from gncore.installation import verify_installation
    corpus = load_corpus()
    installed_directory = Path(installed_directory or ROOT / '.agents/skills').resolve()
    output.mkdir(parents=True, exist_ok=True)
    rows, routes = [], []
    for entry in unified_manifest():
        name = entry["id"]
        document = gncore.render_skill(gncore.get_skill(name)).encode("utf-8")
        resources = packaged_resources(name)
        hashes_ok = all(hashlib.sha256(content).hexdigest() == entry["resource_sha256"][path]
                        for path, content in resources.items())
        packaged_document = files("gncore.skills").joinpath("unified_data", name, "SKILL.md").read_bytes()
        entrypoint_ok = hashlib.sha256(packaged_document).hexdigest() == entry["entrypoint_sha256"]
        installed_document = (installed_directory / name / "SKILL.md").read_bytes()
        cases = [c for c in corpus["cases"] if c["category"] == name]
        for case in cases:
            result = route_task(case["prompt"])
            routes.append({"case_id": case["id"], "category": name, "kind": case["kind"],
                           "prompt": case["prompt"], "selected": result["skill_id"],
                           "status": result["status"], "category_match": result["skill_id"] == name,
                           "expected_workflows": case["workflows"],
                           "suggested_workflows": result["workflows"],
                           "expected_workflow_hit": bool(set(case["workflows"]) & set(result["workflows"]))})
        rendering = measure(lambda: gncore.render_skill(gncore.get_skill(name)), repeats)
        # This explicit selection tests dispatch overhead, not automatic selection accuracy.
        routing = measure(lambda: route_task(cases[0]["prompt"], skill_id=name), repeats)
        reading = measure(lambda: packaged_resources(name), min(repeats, 5))
        row = {"category": name, "workflows": len(entry["workflows"]),
               "resources": len(resources), "entrypoint_bytes": len(document),
               "resource_bytes": sum(map(len, resources.values())), "hashes_ok": hashes_ok,
               "entrypoint_ok": entrypoint_ok, "render_matches_installation": document == installed_document,
               "cases_defined": len(cases),
               "render": rendering, "explicit_route": routing, "resource_read": reading}
        rows.append(row)
        print(f"Measured {name}: {row['workflows']} workflows", flush=True)
    probe_path = ROOT / "src/gncore/skills/unified_data/neural-networks/scripts/gradient_probe.py"
    spec = importlib.util.spec_from_file_location("gradient_probe", probe_path)
    probe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(probe)
    neural = probe.train()
    parameters, curve = probe.initial_parameters(), []
    for step in range(2501):
        loss, gradient, _ = probe.loss_and_gradient(parameters)
        if step % 25 == 0:
            curve.append({"step": step, "loss": loss})
        if step < 2500:
            parameters = [p - .7*g for p, g in zip(parameters, gradient)]
    report = {"schema_version": 1, "version": gncore.__version__,
              "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
              "source_sha256": {str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
                                for path in [Path(__file__), ROOT / "src/gncore/routing.py", ROOT / "src/gncore/evaluation_cases.json", ROOT / "src/gncore/skills/unified_data/manifest.json"]},
              "environment": {"python": platform.python_version(), "system": platform.system(),
                              "architecture": platform.machine(), "processor": platform.processor()},
              "methodology": {"warmups": 1, "repeats": repeats, "resource_read_repeats": min(repeats, 5),
                              "timer": "perf_counter_ns", "latency_scope": "Warm in-process CPU and local filesystem; filesystem caches uncontrolled; no IDE or model inference latency.",
                              "routing_scope": "90 authored scenarios, no held-out set. Category labels are scenario context, not an independent oracle for underspecified/boundary requests.",
                              "quality_scope": "Integrity and deterministic routing only. No complete agent-generated artifact quality scores or creator comparisons."},
              "categories": rows, "scenario_routes": routes, "neural_probe": neural,
              "neural_learning_curve": curve,
              "installed_inventory": verify_installation(installed_directory)}
    (output / "benchmarks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    fields = ["category", "workflows", "resources", "entrypoint_bytes", "resource_bytes", "hashes_ok", "entrypoint_ok", "cases_defined", "render_median_ms", "route_median_ms", "resource_read_median_ms"]
    with (output / "categories.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            flat = {k: row[k] for k in fields if k in row}
            flat.update(render_median_ms=row["render"]["median_ms"], route_median_ms=row["explicit_route"]["median_ms"], resource_read_median_ms=row["resource_read"]["median_ms"])
            writer.writerow(flat)
    assert all(r["hashes_ok"] and r["entrypoint_ok"] and r["render_matches_installation"] for r in rows)
    assert report["installed_inventory"]["ok"] and neural["passed"]
    return report


def charts(report, output):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MaxNLocator
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "axes.spines.left": False, "axes.edgecolor": "#d9deeb",
                         "text.color": "#18213a", "axes.labelcolor": "#46516b",
                         "xtick.color": "#59647c", "ytick.color": "#46516b",
                         "figure.facecolor": "#f8f9fc", "axes.facecolor": "#f8f9fc",
                         "svg.fonttype": "none", "savefig.facecolor": "#f8f9fc"})
    target = output / "charts"
    target.mkdir(exist_ok=True)
    def save(fig, name, footnote):
        fig.get_layout_engine().set(rect=(0, .07, 1, .93))
        fig.text(.03, .015, footnote, fontsize=8, color="#64708b")
        fig.savefig(target / (name + ".png"), dpi=180, bbox_inches="tight")
        fig.savefig(target / (name + ".svg"), bbox_inches="tight")
        plt.close(fig)
    rows = sorted(report["categories"], key=lambda r: (r["workflows"], r["category"]))
    labels = [r["category"] for r in rows]
    fig, axes = plt.subplots(1, 2, figsize=(13, 11), layout="constrained")
    fig.suptitle("GNCore · all 30 developer categories", fontsize=20, fontweight="bold", x=.03, ha="left")
    for ax, key, color, title in [(axes[0], "workflows", "#7257d9", "Active workflows"), (axes[1], "resources", "#229c8b", "Verified supporting files")]:
        ax.barh(labels, [r[key] for r in rows], color=color, height=.65)
        ax.set_title(title, loc="left", fontsize=13, pad=18)
        ax.grid(axis="x", alpha=.18)
        ax.set_axisbelow(True)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.bar_label(ax.containers[0], padding=4, fontsize=8)
        ax.margins(x=.15)
    axes[1].tick_params(labelleft=False)
    save(fig, "category-coverage", "374 workflows · 1,630 resources · counts describe breadth, not output quality. Source: benchmarks.json")
    fig, axes = plt.subplots(1, 2, figsize=(13, 11), layout="constrained")
    fig.suptitle("Local dispatch and rendering", fontsize=20, fontweight="bold", x=.03, ha="left")
    for ax, key, color, title in [(axes[0], "render", "#7257d9", "Skill rendering · milliseconds"), (axes[1], "explicit_route", "#229c8b", "Explicit routing · milliseconds")]:
        medians = [r[key]["median_ms"] for r in rows]
        ax.barh(labels, medians, color=color, height=.6, label="Median")
        ax.scatter([r[key]["p95_ms"] for r in rows], labels, color="#e29539", s=18, zorder=3, label="p95")
        ax.set_title(title, loc="left", fontsize=13, pad=18)
        ax.set_xscale("log")
        ax.grid(axis="x", alpha=.18)
        ax.set_axisbelow(True)
        ax.legend(frameon=False, loc="lower right")
    axes[1].tick_params(labelleft=False)
    save(fig, "local-latency", f"Warm process · {report['methodology']['repeats']} samples/category · log scale · includes no model inference or IDE latency.")
    cases = report["scenario_routes"]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), layout="constrained")
    fig.suptitle("Routing observations and neural mechanics", fontsize=18, fontweight="bold", x=.03, ha="left")
    kinds = ["normal", "underspecified", "boundary"]
    statuses = ["suggested", "ambiguous", "needs-context"]
    left = [0]*3
    for status, color in zip(statuses, ["#7257d9", "#e8b45d", "#a7b1c6"]):
        values = [sum(c["kind"] == k and c["status"] == status for c in cases) for k in kinds]
        axes[0].barh(kinds, values, left=left, color=color, label=status, height=.55)
        left = [a+b for a,b in zip(left, values)]
    axes[0].set_title("Automatic router · 90 authored scenarios", loc="left", pad=16)
    axes[0].set_xlabel("Cases (routing status, not pass/fail)")
    axes[0].legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0, -.32), ncol=3)
    curve = report["neural_learning_curve"]
    axes[1].plot([c["step"] for c in curve], [c["loss"] for c in curve], color="#229c8b", lw=2.5)
    axes[1].set_yscale("log")
    axes[1].set_title("Synthetic XOR · CPU · seed 17", loc="left", pad=16)
    axes[1].set_xlabel("SGD steps")
    axes[1].set_ylabel("Binary cross-entropy loss")
    axes[1].grid(alpha=.2)
    save(fig, "routing-and-neural-probe", "Scenario routing is not an agent-quality benchmark. XOR is a tiny synthetic mechanics check; no GPU/model claim.")
    from matplotlib.colors import ListedColormap
    from matplotlib.patches import Patch
    kinds = ["normal", "underspecified", "boundary"]
    names = sorted(r["category"] for r in rows)
    cells = []
    for name in names:
        selected = [next(c for c in cases if c["category"] == name and c["kind"] == kind) for kind in kinds]
        cells.append([0 if c["selected"] is None else 1 if c["category_match"] else 2 for c in selected])
    fig, ax = plt.subplots(figsize=(8, 12), layout="constrained")
    fig.suptitle("Automatic routing · every category", fontsize=18, fontweight="bold", x=.03, ha="left")
    palette = ["#dfe4ef", "#229c8b", "#e8b45d"]
    ax.imshow(cells, cmap=ListedColormap(palette), vmin=0, vmax=2, aspect="auto")
    ax.set_xticks(range(3), kinds)
    ax.set_yticks(range(len(names)), names)
    ax.tick_params(length=0, pad=9)
    ax.set_xticks([.5, 1.5], minor=True)
    ax.set_yticks([i+.5 for i in range(len(names)-1)], minor=True)
    ax.grid(which="minor", color="#f8f9fc", linewidth=3)
    ax.tick_params(which="minor", length=0)
    ax.legend(handles=[Patch(color=palette[0], label="Unresolved"), Patch(color=palette[1], label="Scenario category"), Patch(color=palette[2], label="Another category")], frameon=False, ncol=3, fontsize=8, loc="lower center", bbox_to_anchor=(.5, -.075))
    save(fig, "category-routing", "Three authored prompts/category · routing labels are observations; underspecified/boundary cases have no universal oracle.")
    report["plotting"] = {"matplotlib": matplotlib.__version__, "outputs": sorted(p.name for p in target.iterdir())}
    (output / "benchmarks.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "web-results")
    parser.add_argument("--repeats", type=int, default=30)
    parser.add_argument("--plot-only", action="store_true")
    parser.add_argument("--installed-directory", type=Path, help="Explicit verified installation; defaults to this project's .agents/skills")
    args = parser.parse_args()
    if not 5 <= args.repeats <= 1000:
        parser.error("repeats must be between 5 and 1000")
    report = json.loads((args.output / "benchmarks.json").read_text(encoding="utf-8")) if args.plot_only else benchmark(args.output, args.repeats, args.installed_directory)
    charts(report, args.output)
    print(f"Saved measured results and charts to {args.output}")


if __name__ == "__main__":
    main()
