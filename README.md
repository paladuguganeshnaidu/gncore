# GNCore

A production-grade autonomous software delivery framework for Claude. Given a plain-language idea, it plans, architects, designs, builds, integrates, reviews (security / performance / accessibility), tests, debugs, refactors, documents, deploys, and verifies a real website or web app — with explicit quality gates between every stage.

This is a ground-up redesign of the `website-builder-skills` baseline (see `AUDIT.md` for the full critique). The baseline was a solid 8-phase linear script. This framework is a **verified pipeline**: every stage has a contract (inputs, outputs, stopping conditions, quality gate) and nothing advances on an unmet gate. See `AUDIT.md` for the reasoning behind every structural change.

## What changed, and why

| Baseline gap | Fix in this framework |
| --- | --- |
| No requirements-clarification loop before planning — ambiguity got silently resolved by guessing | New `01-think.md` stage: forces explicit assumption-surfacing and a single clarifying-question budget before any doc is written |
| No research stage — library/pattern choices came from training-data priors, which go stale | New `02-research.md`: web-verifies framework versions, library choices, and platform constraints before they're locked into the architecture |
| "Design" conflated visual design with technical architecture in one skill | Split into `04-architect.md` (system/tech decisions) and `05-design.md` (visual/UX design system) — different failure modes, different reviewers |
| Security review ran once, at the end, disconnected from what was built | `10-security.md` runs as a gate immediately after `08-integrate.md` and again before `18-verify.md`; security constraints are also injected into `06-scaffold.md` and `07-build.md` up front, not bolted on after |
| No performance or accessibility review at all | New `11-performance.md`, `12-accessibility.md` as first-class gated stages |
| No testing stage — "fix-it" only reacted to bugs already in production | New `13-test.md` runs before debugging; `14-debug.md` now consumes failing tests instead of vibes |
| No explicit stopping conditions or pass/fail gates — a skill could "finish" on vibes | Every skill in `skills/` has a `## Quality Gate` section with binary pass/fail criteria the orchestrator checks before advancing |
| No context/memory system — long builds re-explain everything each turn | New `context/CONTEXT-ENGINEERING.md`: a living project ledger (decisions, style, dependencies) that every stage reads/updates instead of re-deriving |
| No multi-agent role definitions — one voice did everything, which hides review-blindness (the builder can't credibly review its own security) | New `agents/AGENTS.md`: named roles with decision boundaries and a handoff contract; the orchestrator assigns each stage to a role and the role's output is judged against that role's mandate, not the builder's |
| Inconsistent packaging across variants (READMEs, license, CI differ between the three source zips) | Single canonical structure, one README, one CI-ready layout |
| Redundant stages in "elite" wishlists (self-review + review + bug-hunt + final-QA all overlap) | Consolidated into `09-review.md` (pre-merge self+code review), `13-test.md`/`14-debug.md` (correctness), `18-verify.md` (post-deploy final QA) — three distinct checkpoints, not five overlapping ones |

## Pipeline

```text
THINK → RESEARCH → PLAN → ARCHITECT → DESIGN → SCAFFOLD → BUILD → INTEGRATE
   → REVIEW → SECURITY → PERFORMANCE → ACCESSIBILITY → TEST → DEBUG → REFACTOR
   → DOCUMENT → DEPLOY → VERIFY
```

GIT (`19-git.md`) is not a phase — it runs continuously (a commit at the close of every stage). See `ARCHITECTURE.md` for the full diagram, gate criteria, and rollback rules.

## Directory structure

```text
website-builder-elite/
├── README.md                 ← you are here
├── ARCHITECTURE.md           ← pipeline diagram, stage contracts, quality gates
├── AUDIT.md                  ← deep audit of the baseline, per-skill scores, rationale
├── MIGRATION.md              ← how to move an in-flight baseline project onto this framework
├── SECURITY.md               ← reporting policy for defects in the framework's own prompts (not generated-app security — that's skills/10-security.md)
├── skills/                   ← the 19 pipeline skills, numbered in execution order
│   ├── 00-orchestrator.md
│   ├── 01-think.md
│   ├── 02-research.md
│   ├── 03-plan.md
│   ├── 04-architect.md
│   ├── 05-design.md
│   ├── 06-scaffold.md
│   ├── 07-build.md
│   ├── 08-integrate.md
│   ├── 09-review.md
│   ├── 10-security.md
│   ├── 11-performance.md
│   ├── 12-accessibility.md
│   ├── 13-test.md
│   ├── 14-debug.md
│   ├── 15-refactor.md
│   ├── 16-document.md
│   ├── 17-deploy.md
│   ├── 18-verify.md
│   └── 19-git.md
├── agents/
│   └── AGENTS.md              ← 18 named roles, decision boundaries, handoff format
├── context/
│   ├── CONTEXT-ENGINEERING.md ← the living project ledger and retrieval rules
│   └── pattern-library.md     ← durable, framework-agnostic decision structure read by 04-architect and 05-design (never a source of specific package names)
├── templates/
│   ├── requirements-template.md
│   ├── architecture-decision-record.md
│   ├── quality-gate-checklist.md
│   └── pull-request-template.md
├── scripts/
│   └── validate_consistency.py ← the CI consistency checker, see "Consistency CI" below
└── .github/workflows/ci.yml   ← runs the validator + markdownlint on every push/PR
```

## Consistency CI

`.github/workflows/ci.yml` runs on every push and PR and executes `scripts/validate_consistency.py`, a real script (not a described-but-unbuilt process) that checks: every skill's frontmatter `name:` matches its filename, every `NEXT:` handoff target resolves to a real stage file (or a documented exception), every backtick-quoted `*.md` filename referenced in `README.md`/`ARCHITECTURE.md`/`agents/AGENTS.md` actually exists, every numeric claim about a countable table (like "N named roles") matches the table's real row count, and every file in `templates/` is referenced by name somewhere in `skills/`. This is what would have caught the role-count mismatch and the dangling `SECURITY.md` reference automatically instead of relying on a manual audit to find them — see `CHANGELOG.md` for that history. A markdownlint pass runs alongside it for basic formatting hygiene (config in `.markdownlint.yml`).

## How to use this framework

1. Load `skills/00-orchestrator.md`. It is the only entry point — never load a stage skill directly except when resuming mid-pipeline or explicitly asked to run one stage in isolation.
2. The orchestrator drives the state machine in `ARCHITECTURE.md`, loading one stage skill at a time, checking that stage's Quality Gate before advancing, and writing/reading `context/` artifacts between stages.
3. Every stage produces one artifact (a document, a diff, a report) that the next stage consumes. Nothing is implicit.
4. If a Quality Gate fails, the orchestrator does not advance — it routes back to the owning stage (or to `14-debug.md`) with the specific failure, per the recovery rules in `ARCHITECTURE.md`.

## Execution requirements

Several gates in this framework are phrased as achieved facts — "prove the scaffold builds," "all tests pass," "confirm the health check returns 200" — that are only meaningfully binary if the session actually has the capability to check them. Stages **06** (scaffold), **07** (build), **09** (partial — the correctness-tracing part of review benefits from execution but doesn't strictly require it), **10** (partial — dependency-CVE lookups benefit from live access), **11** (performance), **13** (test), **16** (document), **17** (deploy), and **18** (verify) all contain at least one gate item like this.

This framework supports two explicit modes, and every affected stage's Quality Gate, Stopping conditions, and Handoff block name which one it ran in:

- **Verified mode** — the session has real code-execution, browser, and (for 17/18) deployment-credential access. Gates are checked by actually running the command, test, or request. This is the mode the gate text in each skill file is written to assume by default.
- **Reasoned mode** — chat-only, no execution access. The model performs the equivalent analysis without running anything: a static review of config files for `06-scaffold.md`, a static trace-through of logic for `13-test.md`, a manual walkthrough of setup steps for `16-document.md`, and so on. In this mode, the handoff block's `STATUS` line must read `pass (reasoned, not executed)` — **never** a bare `pass`, since a bare `pass` implies Verified mode and would misrepresent what was actually checked. The orchestrator surfaces this distinction to the user in plain language at the next real decision point — for example, before `17-deploy`: "I haven't been able to actually run the test suite in this session — here's what I traced through, but you should run it yourself before this ships."

Reasoned-mode results are not treated as equivalent to Verified-mode results everywhere: `17-deploy.md` specifically requires an explicit, logged user acknowledgment before deploying on a Reasoned-mode `10-security.md` or `13-test.md` result, because deploying on an untested claim is a materially higher-risk action than deploying on an actually-verified one. See that skill file for the exact rule.

## Public CLI

The supported user workflow is intentionally small:

```powershell
pip install gncore
mkdir myproject
cd myproject
gncore init
gncore run
```

`gncore init` creates `.gncore/`, writes `prompt.md`, writes configuration, and auto-detects an available provider. `gncore run` validates the project and then executes the workflow automatically. If execution stops partway through, `gncore resume` continues from the saved state.

Other public commands:

| Command | Purpose |
| --- | --- |
| `gncore doctor` | Validate the project, config, provider availability, Git, and secure credential storage |
| `gncore provider list` | Show discovered providers and their availability |
| `gncore provider use <name>` | Select a provider and persist it in the project config |
| `gncore provider detect` | Re-detect the best available provider and save it |
| `gncore provider health [name]` | Check provider health for the selected provider or a named one |
| `gncore config show` | Print the current project config |
| `gncore config set --provider <name>` | Update the selected provider |
| `gncore config validate` | Validate the on-disk project config |
| `gncore auth login <provider>` | Store a provider token securely in the platform credential store |
| `gncore auth logout <provider>` | Remove the stored provider token |
| `gncore auth status <provider>` | Check whether a token is available |
| `gncore version` | Print the installed gncore version |
| `gncore update` | Upgrade gncore with pip |

Examples:

```powershell
gncore provider list
gncore provider use mock
gncore auth login openai-api --token %OPENAI_API_KEY%
gncore doctor
```

Stages remain internal implementation details. Users should work through `init`, `run`, and `resume` rather than invoking stage numbers directly during normal usage.

## Design principles this framework holds itself to

- **A gate is binary.** "Looks good" is not a gate. Every gate in this repo is phrased as a checklist item that resolves to pass/fail, because ambiguous gates are the #1 way agent pipelines silently ship broken work.
- **No stage reviews its own output as the final word.** The role that builds is never the role whose sign-off is the gate (see `agents/AGENTS.md`).
- **Context is retrieved, not replayed.** Stages read only the ledger sections relevant to them, not the full conversation history — see `context/CONTEXT-ENGINEERING.md`.
- **Fewer, sharper stages beat many overlapping ones.** We rejected several stages from typical "elite framework" wishlists (separate "bug-hunt" and "final-QA" stages, a standalone "monitor" stage) because their responsibilities are fully covered by `14-debug.md` and `18-verify.md` respectively; adding them back would only add token cost and ambiguous ownership, not capability.
- **Security, performance, and accessibility are gates, not chapters.** They block deployment exactly like a failing test does.
