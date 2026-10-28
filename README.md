# GNCore

GNCore 6 organizes **553 workflows into 60 adaptive category skills**. Install a category once, describe the result you want, and a compatible AI agent uses that skill to select the relevant workflows, constraints, and verification steps.

For example, invoke `$web-frontend` with an idea for a site. It can choose a suitable visual direction when no theme is named, honor an explicit theme, preserve an existing brand, and guide implementation through responsive behavior, accessibility, interaction states, and verification. The same category-first pattern covers backend services, coding, business work, research, documents, data, and the other categories.

## Install this source version

From a checkout of this branch:

```bash
python -m pip install .
gncore export --specific web-frontend
```

Or install directly from the pushed development branch:

```bash
python -m pip install "git+https://github.com/paladuguganeshnaidu/gncore.git@codex/adaptive-category-skills"
```

Export writes standard `.agents/skills/<category>/SKILL.md` folders in your project, including the supporting references, tools, assets, and license notices declared by the category. Compatible agents discover the entrypoints according to their own skill settings; GNCore does not launch a model or bypass host settings.

## Use an adaptive category

```text
$web-frontend Build a booking website for a small clinic.
$web-frontend Build a maximalist music festival landing page.
$web-backend Implement an authenticated booking API using this project's stack.
$code-build Diagnose and fix the failing checkout tests.
$finance-accounting Reconcile these figures and explain the variance.
$presentations-powerpoint Create a board presentation from this report.
```

The skill selects relevant work instead of requiring a separate skill invocation for each subtask. Its core selection and workflow procedures are merged into one `SKILL.md`; substantial technical references and executable helpers remain supporting files, loaded only when relevant.

## Discover, inspect, and export

```bash
gncore list skills
gncore list categories
gncore list domains
gncore list workflows
gncore search "machine learning training"
gncore show web-frontend
gncore export --skills web-frontend web-backend code-build
gncore export --all
gncore export --all --dry-run
gncore verify
gncore export --all --output gncore-categories.zip
```

`gncore list skills` lists 60 primary entrypoints. `list workflows` lists all 553 retained workflow IDs and their category destinations. The 30 professional domain packs each retain their ten workflows inside one category skill. Existing workflow IDs remain CLI/API lookup aliases; exporting aliases from one category produces one merged folder.

The optional planning aid gives a deterministic frontend starting direction without calling a model:

```bash
gncore plan "A premium hotel website, no animation"
gncore plan "An analytics dashboard" --theme minimalism
```

The host AI makes the contextual design decisions and performs the work. The planning aid is a useful local check, not a guarantee of aesthetic quality.

Directory exports now preflight the whole selection, stage and verify content, and retain a recoverable backup. Customized and unmanaged files are preserved. `gncore verify` compares installed files with their recorded hashes. For exact known older exports, `python scripts/install_categories.py --migrate-managed` retires only byte-identical legacy folders. See [installation and recovery](docs/INSTALLATION.md).

The [offline evaluation pilot](docs/EVALUATION.md) includes 36 scenarios across 12 categories:

```bash
gncore evaluate --validate
gncore evaluate --list
```

Its runner separates structural artifact checks from pending human review and unexecuted tool checks; it does not certify the quality of an AI output.

## Python API

```python
from gncore import get_skill, list_categories, list_workflows, search_skills

frontend = get_skill("web-frontend")
same_category = get_skill("web-front-minimalism")
assert frontend == same_category
print(len(list_categories()))   # 60
print(len(list_workflows()))    # 553
print([s.metadata.skill_id for s in search_skills("fastapi")])
```

Browse the [complete catalog](docs/ALL_SKILLS.md), [source research](docs/SOURCE_RESEARCH.md), [frontend guide](docs/FRONTEND_SKILLS.md), [backend guide](docs/BACKEND_SKILLS.md), [migration notes](MIGRATION.md), and [API documentation](docs/API.md).

The [upgrade plan](docs/UPGRADE_PLAN.md) tracks the implemented reliability foundation and the remaining category, routing, and source-maintenance work.

## Quality and development

```bash
python -m pip install -e ".[test,skills]" build twine
python -m pytest -q
python scripts/generate_skill_catalog.py
python -m build
python -m twine check dist/*
```

Tests cover workflow preservation, aliases, category selection, explicit themes and constraints, portable resources, licensing metadata, and exports. Source compilation and package smoke tests cover GNCore's own runtime; supporting upstream tools can have independent runtime requirements. Automated checks do not certify every possible AI output. See [verification scope](VERIFIED_MODE.md).

## Ownership and licenses

GNCore's independently authored code and guidance are MIT-licensed under [LICENSE](LICENSE). Third-party guides, helpers, assets, and adaptations retain their original authorship and supplied terms, including Apache, Creative Commons attribution, and share-alike obligations. They are not relicensed as exclusively GNCore-owned. Each category declares its aggregate licenses and includes source provenance and notices. See [ownership and attribution](docs/OWNERSHIP.md).

Version 6.0.0 is prepared in this source branch. Pushing the branch does not publish a PyPI release; publishing requires a reviewed release tag and successful publishing workflow.
