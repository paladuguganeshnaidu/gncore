# Architecture

## Pipeline diagram

```text
 00-ORCHESTRATOR (state machine, never does the work itself)
        │
        ▼
 01-THINK ──────────────► clarify.md
        │  gate: zero unresolved ambiguities, ≤1 clarifying question asked
        ▼
 02-RESEARCH ───────────► research-notes.md
        │  gate: every version/library claim has a checked source or is marked "assumed, low-risk"
        ▼
 03-PLAN ───────────────► requirements.md
        │  gate: user has explicitly approved requirements.md
        ▼
 04-ARCHITECT ──────────► architecture.md + ADRs
        │  gate: every major decision has a one-line rationale; no circular dependencies
        ▼
 05-DESIGN ─────────────► design-system.md
        │  gate: design tokens defined for every UI state (default/hover/focus/disabled/error)
        ▼
 06-SCAFFOLD ───────────► project skeleton (files, configs, empty modules)
        │  gate: scaffold builds/installs with zero errors before any feature code is written
        ▼
 07-BUILD ──────────────► feature code + unit tests written alongside it
        │  gate: every requirement in requirements.md maps to at least one built feature
        ▼
 08-INTEGRATE ──────────► auth/db/payments/third-party wiring
        │  gate: every credential is env-var-based, never hardcoded; integration smoke-tested
        ▼
 09-REVIEW (self + code review, by Reviewer role — not the Builder) ─► review-report.md
        │  gate: zero unresolved "must-fix" comments
        ▼
 10-SECURITY ───────────► security-report.md
        │  gate: zero unresolved Critical/High findings
        ▼
 11-PERFORMANCE ────────► performance-report.md
        │  gate: budgets in architecture.md are met or a documented exception exists
        ▼
 12-ACCESSIBILITY ──────► accessibility-report.md
        │  gate: zero WCAG 2.2 AA violations of type "blocker"
        ▼
 13-TEST ───────────────► test-report.md
        │  gate: all critical-path tests pass; coverage floor from architecture.md is met
        ▼
 14-DEBUG (only if 09–13 found unresolved failures) ─► fix diffs + re-run of the failing gate
        │  gate: the specific failing gate now passes; no new regressions introduced
        ▼
 15-REFACTOR (optional, quality-driven, never adds features) ─► refactor-report.md
        │  gate: all tests from 13-TEST still pass after refactor
        ▼
 16-DOCUMENT ───────────► README.md, API docs, ADR index
        │  gate: a new developer could set up the project using only the docs
        ▼
 17-DEPLOY ─────────────► deployment-record.md
        │  gate: build succeeds on the target platform; health check returns 200
        ▼
 18-VERIFY ─────────────► verification-report.md (final QA, production URL)
        │  gate: production smoke test passes; rollback plan confirmed
        ▼
       DONE

 19-GIT runs continuously: one commit at the close of every stage above, not as its own phase.
```

## Stage contract (every skill in `skills/` follows this shape)

Each stage skill file declares:

- **Role** — which named agent (see `agents/AGENTS.md`) owns this stage.
- **Inputs** — exact ledger artifacts it reads from `context/`.
- **Outputs** — exact artifact(s) it writes.
- **Process** — the checklist/workflow.
- **Quality Gate** — a binary pass/fail checklist, written to the shape defined in `templates/quality-gate-checklist.md` (binary criteria, explicit pass/fail-fixable/fail-escalate stopping conditions). This is an editorial rule a contributor edits skill files against, not a template that sits unused — if you add or change a Quality Gate in any `skills/*.md` file, check it against that template's shape before merging. If any gate item fails, the stage is not done.
- **Stopping conditions** — when to stop iterating and either pass the gate or escalate.
- **Handoff** — what it tells the orchestrator and the next stage.

## Orchestrator responsibilities

`00-orchestrator.md` is the only stage that is always loaded. It:

1. Tracks current pipeline position and the state of every ledger artifact in `context/`.
2. Loads exactly one stage skill at a time and feeds it only the ledger sections that stage's contract requires (see `context/CONTEXT-ENGINEERING.md` — no full-history replay).
3. After a stage reports completion, checks that stage's Quality Gate itself before advancing (the orchestrator is the actual gatekeeper — a stage cannot self-certify past its own gate).
4. On gate failure, applies the Recovery Rules below instead of silently proceeding.
5. Surfaces every user-facing decision point in plain language, regardless of how technical the underlying stage was.

## Recovery rules

| Failure at stage | Action |
| --- | --- |
| 01-THINK, 03-PLAN | Ask the user the specific blocking question; do not proceed on an assumption for anything that changes scope, cost, or data handling. |
| 02-RESEARCH | Mark the unverified claim explicitly as an assumption in `requirements.md`/`architecture.md` and flag it for re-check before 10-SECURITY. |
| 04-ARCHITECT, 05-DESIGN | Loop back within the same stage — these are pre-code, so iteration is cheap. Max 3 internal iterations before escalating the tradeoff to the user. |
| 06-SCAFFOLD, 07-BUILD, 08-INTEGRATE | Route to 14-DEBUG with the specific error, not back to the start of the stage. |
| 09-REVIEW, 10-SECURITY, 11-PERFORMANCE, 12-ACCESSIBILITY, 13-TEST | Route the specific failing item(s) to 14-DEBUG. Do not re-run the whole stage — re-run only the failed gate after the fix lands. |
| 14-DEBUG can't reproduce or can't fix after 3 attempts | Escalate to the user with the exact reproduction steps tried and the current hypothesis; do not silently mark it resolved. |
| 17-DEPLOY | Auto-rollback to the last verified deployment record; hand the failure to 14-DEBUG. |
| 18-VERIFY | Treat as a 17-DEPLOY failure — rollback, then debug. |

## Non-linear execution

Stages 10, 11, 12 (security/performance/accessibility) have no data dependency on each other once 09-REVIEW passes — they read the same codebase and none consumes another's output. That means they may be run in **any order** before the pipeline advances to 13-TEST.

Whether they can also be *dispatched concurrently* (as a latency optimization, not a default assumption) depends on a capability the orchestrator must check for, not assert: genuine concurrent execution — independent subagents or independent tool-call streams the runtime actually supports — as opposed to one model instance mentally context-switching between three roles inside a single sequential turn, which is not concurrency and provides no latency benefit. `agents/AGENTS.md` states plainly that role-switching is sequential by default; this section's "may dispatch concurrently" is the one specific exception, and only when that capability is genuinely present. If the orchestrator cannot confirm concurrent execution is actually happening, it defaults to running 10/11/12 sequentially, in any order, and must not tell the user work is happening "in parallel" when it isn't.

Everything else is strictly sequential because each stage's output is the next stage's required input.

## Why 15-REFACTOR is optional and gated last, not continuous

Refactoring before tests exist risks silently changing behavior with nothing to catch it. Refactoring is placed after 13-TEST/14-DEBUG specifically so that "all tests still pass" is a real, previously-established gate, not a new one invented on the spot.
