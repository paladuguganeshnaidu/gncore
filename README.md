# GNCore

GNCore **7.0.0** is a developer-focused release: **30 adaptive skills, 374 workflows, and six capability groups**. One skill guides the host AI through relevant modes, existing project constraints, implementation and verification.

Published versions are listed in the [PyPI release history](https://pypi.org/project/gncore/#history). The release keeps package validation, historical AI trials and current unmeasured behavior distinct; see the [benchmarks](https://gncore.pages.dev/benchmarks/) for source data and methodology.

## Developer coverage

Web frontend/backend, software engineering, UX/design systems, Python, developer tools, documentation, testing, cybersecurity, cloud/DevOps/SRE, release engineering, automation, mobile, games, data engineering/science, databases, machine learning, neural networks, deep learning, computer vision, NLP, MLOps, AI applications, systems programming, embedded systems, performance, observability, technical research and distributed systems.

Phase two retires business/professional packs and consolidates overlapping technical categories. It preserves 319 technical workflows, rewrites 116 formerly shared procedures, adds 55 original procedures and records all 234 retired workflow outcomes. See [the migration guide](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/MIGRATION.md), [full catalog](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/ALL_SKILLS.md) and [merge audit](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/PHASE2_MERGE_AUDIT.json).

## Install

Install the verified production release:

```bash
python -m pip install gncore==7.0.0
```

Or install a source checkout:

```bash
python -m pip install .
gncore list skills
gncore route "Check neural network gradients"
gncore export --specific neural-networks
gncore verify
```

Then use a compatible host agent:

```text
$neural-networks Diagnose gradient flow before scaling training.
$web-frontend Build a clinic booking page using the existing stack, no animation.
$web-backend Add a tenant-scoped idempotent endpoint.
$embedded-systems Verify timer wraparound with host fixtures.
```

Exports contain a standard `.agents/skills/<id>/SKILL.md` and its declared resources/notices. Host discovery and invocation syntax depend on that agent's settings. GNCore does not run a model, install frameworks or grant tool permissions.

The entrypoint selects work and checks completion boundaries. Detailed procedures live in a declared `WORKFLOWS.md` resource; the host reads only the matching section and necessary references. All 374 workflow IDs remain available.

## Inspect, migrate and check

```bash
gncore search "neural network"
gncore show web-frontend
gncore list workflows
gncore list domains
gncore export --all --prune-retired --dry-run
gncore export --all --prune-retired
gncore audit
gncore evaluate --validate
gncore export --all --output gncore-developer-skills.zip
```

Directory installation preflights the entire selection, checks recorded digests, stages and verifies content, and retains a recovery backup. Retirement removes only unchanged inventory-managed folders; custom/untracked content is preserved. See [installation and recovery](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/INSTALLATION.md).

Routing supplies explainable English keyword hints and abstains on ambiguous/unsupported requests. The host AI makes contextual decisions. Frontend-specific `gncore plan` remains available for explicit themes, inferred visual direction and negative constraints.

The [evaluation corpus](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/EVALUATION.md) has 90 concrete scenarios across all 30 categories. Structural checks, human review and unexecuted external checks remain separate. The bundled neural-network probe verifies analytic gradients and tiny synthetic XOR learning on CPU; it does not establish production model quality.

## Develop and prepare release artifacts

The [comparative pilot](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/web-results/comparison/EXECUTIVE-REPORT.md) records original VS Code and Antigravity answers across all 30 categories, alongside pinned published references. Landscape plots show passed checks and missing measurements; they do not certify universal efficiency or security. See the [technical report](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/web-results/comparison/TECHNICAL-REPORT.md) for raw evidence, scoring and limitations.

The [subsequent improvement cycle](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/web-results/improvement-cycle-1/README.md) records all-domain completion rules, ten reviewed procedure refinements and three focused corrections. Initial shared-context answer scores are withdrawn from fair comparisons; the replacement fresh-context evaluation stopped at an account usage limit. The [landscape review](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/output/pdf/GNCore-skill-improvement-review.pdf) includes the complete domain table, verified-evidence graph, sources and remaining gaps. A greater-than-95% AI-quality result is not established.

```bash
python -m pip install -e ".[test,skills]" build twine
python scripts/build_catalog.py --check
python scripts/build_evaluations.py --check
python -m pytest -q
python scripts/generate_skill_catalog.py
python scripts/build_website.py
python -m build --sdist --wheel --outdir .work/phase2/release
python -m twine check .work/phase2/release/*.whl .work/phase2/release/*.tar.gz
```

Versioned authoring inputs in `catalog/` and retained source files support offline rebuilds; no `.work` cache or fresh source download is required. The generated website uses the same catalog. The publication build is promoted only after the package version and artifact hashes are publicly verified.

## Ownership

Original GNCore code and guidance are MIT-licensed under [LICENSE](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/LICENSE). Retained third-party guides, helpers and adaptations keep their supplied notices, authorship and applicable licenses, including share-alike obligations. They are not exclusively GNCore-owned. Aggregate skill expressions and per-source notices travel with exports; see [ownership](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/OWNERSHIP.md).

See [historical phase-two release preparation](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/PHASE2_RELEASE.md) and [verification evidence](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/PHASE2_VERIFICATION.md) for exact scope and publication state.

The current production promotion plan is documented in [RELEASE_7_0_0.md](https://github.com/paladuguganeshnaidu/gncore/blob/v7.0.0/docs/RELEASE_7_0_0.md).
