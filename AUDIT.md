# Audit: baseline `website-builder-skills` → `website-builder-elite`

Three near-identical builds of the same 11-file framework were supplied (sonnet4.6, kimi, sonnet5 variants). They converge on the same 8-phase design, so this audit treats them as one baseline and notes where the packaging diverged.

## Cross-cutting findings

**Strengths**
- Checklist-driven, imperative prompt style ("Mark PASS or FAIL. Do not skip lines.") — this is good prompt engineering and is preserved in this framework's gate design.
- Plain-language framing for non-technical users is a real product decision worth keeping, not a weakness — this framework keeps it in `00-orchestrator.md` and `01-think.md`.
- `03-scaffold-it`, `04-build-it`, `05-connect-it` are already close to production quality in their checklists (dependency pinning, file structure conventions, env var handling).

**Structural weaknesses (the reason this is a redesign, not a patch)**
1. **Linear script, not a pipeline.** Phases hand off with "user approves" as the only gate. There is no binary, checkable stopping condition anywhere in the baseline — approval is vibes, not verification.
2. **No requirements-clarification budget.** `01-dream-it` asks open questions but nothing bounds ambiguity resolution, so downstream stages inherit unstated assumptions silently.
3. **No research stage.** Framework/library choices in `02-design-it` and `03-scaffold-it` are asserted from the model's priors with no verification step, which is a hallucination risk for anything version-specific (deprecated APIs, renamed packages, changed defaults).
4. **Design conflates two different disciplines.** `02-design-it` (554 lines) does both visual/UX design tokens *and* technical architecture (framework choice, data model, API shape) in one pass. These need different review lenses and different failure modes — a wrong color palette and a wrong database schema are not the same category of risk.
5. **Security runs once, late, and alone.** `06-secure-it` is thorough *within itself* (reconnaissance → line-by-line checklist → injection/XSS/auth checks) but only executes after the entire app is built and connected, meaning insecure patterns baked into scaffolding (`03-scaffold-it`) or integration (`05-connect-it`) get expensive late fixes instead of being prevented.
6. **No performance or accessibility review exists at all.** Zero stages check for either. For "production-grade" output this is a hard gap, not a nice-to-have.
7. **No testing stage.** `08-fix-it` (481 lines) is a strong *reactive* debugger, but nothing produces the failing signal it consumes — there's no unit/integration/e2e stage that would catch regressions before a human notices broken behavior in production.
8. **No context/memory system.** Each skill's "Input" section just says "codebase from skills 01-04," implying the full history is replayed into context every stage. On a real multi-day build this is both a token-cost problem and a staleness problem (the ledger of *decisions made* is never distinguished from the *code itself*).
9. **Single undifferentiated voice.** One persona plans, builds, and reviews. A reviewer that is the same voice as the builder is structurally unable to catch the builder's own blind spots — this is the classic self-review failure mode in agentic pipelines.
10. **Packaging inconsistency across the three variants.** The kimi variant's README is 41 lines with no CI/license/contributing scaffolding; the sonnet4.6 variant has full repo scaffolding (`.github/`, `CHANGELOG.md`, `SECURITY.md`) but is missing `09-git-it`/`10-readme-it`; the sonnet5 variant has all 11 skills but minimal repo scaffolding. None of the three is a complete, self-consistent deliverable on its own.
11. **`git-it` and `readme-it` are terminal add-ons.** Version control should be continuous (a commit boundary per stage, so any stage can be reverted independently), not a single "phase 9" checkpoint after the app already exists.

## Per-skill scores (baseline, 1–10)

Scored on: Architecture, Reasoning, Prompt Design, Reliability, Scalability, Maintainability, Output Quality, Extensibility, Production Readiness.

| Skill | Arch | Reason | Prompt | Reliab | Scale | Maint | Output | Extend | Prod-Ready | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 00-orchestrator | 5 | 5 | 6 | 5 | 4 | 6 | 6 | 4 | 5 | Clear phase list, but "approval" is the only gate; no recovery/rollback logic |
| 01-dream-it | 6 | 6 | 7 | 6 | 6 | 7 | 7 | 6 | 6 | Good extraction checklist; no ambiguity/clarification budget |
| 02-design-it | 6 | 5 | 6 | 5 | 5 | 5 | 7 | 4 | 5 | Strong content, wrong scope — mixes UX and architecture |
| 03-scaffold-it | 8 | 7 | 8 | 7 | 7 | 7 | 8 | 6 | 7 | Best file in the baseline; convention-driven and specific |
| 04-build-it | 7 | 6 | 7 | 6 | 6 | 6 | 7 | 5 | 6 | Solid, but no test-writing responsibility paired with it |
| 05-connect-it | 7 | 6 | 7 | 6 | 6 | 6 | 7 | 5 | 6 | Good credential/env handling; no security gate before going live |
| 06-secure-it | 8 | 7 | 8 | 6 | 6 | 6 | 8 | 5 | 6 | Excellent checklist depth; wrong position in pipeline (too late, runs once) |
| 07-launch-it | 6 | 5 | 6 | 5 | 5 | 5 | 6 | 4 | 5 | Deploy mechanics fine; no post-deploy verification stage follows it |
| 08-fix-it | 7 | 7 | 7 | 6 | 6 | 6 | 7 | 5 | 6 | Good root-cause taxonomy; purely reactive, no test signal to consume |
| 09-git-it | 6 | 5 | 6 | 5 | 5 | 6 | 6 | 5 | 5 | Fine mechanics; wrongly scoped as single terminal phase |
| 10-readme-it | 6 | 5 | 6 | 5 | 5 | 6 | 6 | 4 | 5 | Fine mechanics; should run continuously alongside build, not at the end |
| **Average** | **6.5** | **5.8** | **6.7** | **5.6** | **5.5** | **6.0** | **6.9** | **4.9** | **5.6** | |

Read the pattern: **Output quality and prompt design are decent (~6.7–6.9) but Extensibility and Scalability lag (~4.9–5.5)** — the individual checklists are well-written, but the system they're wired into doesn't scale to a real multi-day, multi-reviewer build. That's exactly what this redesign targets: the *pipeline*, not the *prose*.

## What was kept

- The imperative, no-filler checklist voice.
- The plain-language user-facing framing in the orchestrator.
- The core competencies of scaffold/build/integrate/secure/fix — rewritten and re-scoped, not discarded, since the underlying checklists were the strongest part of the baseline.

## Addendum: the baseline scoring above was more generous than the evidence supports

A later, deeper line-level pass over the baseline found concrete defects that the per-skill scoring table did not capture: a Tailwind v3/v4 config contradiction within `03-scaffold-it` itself, 21 unedited PDF-export watermarks left across two of the baseline's own files, a stray non-English artifact inside a security code example, a broken shell command in the git skill, and a password-based-SSH anti-pattern surfaced in the deploy skill. None of these were weighted into the `Arch`/`Reliab`/`Output` columns above.

This doesn't change this redesign's structural conclusions — the pipeline-vs-script, single-voice, no-context-system, and no-testing-stage findings above are independent of these line-level defects and were correct regardless. But an audit that cites itself as the justification for a ground-up rewrite should be accurate about what it actually found, and it wasn't fully accurate here: the real per-file scores for `03-scaffold-it` and `05-connect-it`/`06-secure-it` were likely lower than the table shows — those three files are exactly the ones praised most highly above ("best file in the baseline," "excellent checklist depth"), and a config contradiction, a broken command, and an anti-pattern sitting inside files scored 7–8 is a real scoring miss, not a rounding error. Treat the numbers above as directionally correct but overstated on those three rows specifically.

## What was replaced

- The phase-approval gate model → binary Quality Gates per stage (`ARCHITECTURE.md`).
- The single-voice model → named agent roles with decision boundaries (`agents/AGENTS.md`).
- The "replay everything" context model → a ledger-based context system (`context/CONTEXT-ENGINEERING.md`).
- The single late security pass → security gates injected at scaffold, integrate, and pre-deploy.
- The absence of testing/performance/accessibility → three new first-class gated stages.
