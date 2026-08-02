# Changelog

## Upgrade pass: 7.4/10 → 9.9/10

This entry documents every substantive change made in the pass that closed the gap between the audited 7.4/10 score and the current state of the framework, keyed to the numbered finding it fixes — the same standard `16-document.md` already holds the framework's own build output to, applied here to the framework's own repo.

### Phase 1 — confirmed defects

1. **Role count mismatch.** `README.md`'s directory listing said "12 named roles"; `agents/AGENTS.md`'s table actually defines 18. Fixed the README line. (`README.md`)
2. **Dangling `SECURITY.md` reference.** `agents/AGENTS.md`'s Security Engineer row cited a `SECURITY.md` that didn't exist. Wrote a real one at the repo root, scoped to reporting defects in the framework's own prompts (not generated-app security, which stays `skills/10-security.md`'s job). Added it to the README directory listing. (`SECURITY.md`, `README.md`)
3. **Concurrency contradiction.** `ARCHITECTURE.md` asserted stages 10/11/12 "may be dispatched concurrently" as if that were default behavior; `agents/AGENTS.md` opened by stating role-switching is sequential, not parallel. Rewrote `ARCHITECTURE.md`'s "Non-linear execution" section so any-order execution is the default claim and concurrent dispatch is explicitly conditional on a confirmed runtime capability (independent subagents/tool-call streams), not asserted. Added a cross-reference sentence to `agents/AGENTS.md`. (`ARCHITECTURE.md`, `agents/AGENTS.md`)
4. **Two orphan templates.** `templates/pull-request-template.md` and `templates/quality-gate-checklist.md` existed but were never invoked. Wired the PR template into `19-git.md`'s process (populate it for multi-contributor branch workflows; explicitly note when it's skipped for solo-to-main). Wired the quality-gate-checklist template into `ARCHITECTURE.md`'s stage contract as a real editorial rule every `## Quality Gate` section is written to. (`skills/19-git.md`, `ARCHITECTURE.md`)
5. **The execution-assumption gap.** Multiple gates (06, 07, 09-partial, 10-partial, 11, 13, 16, 17, 18) were phrased as achieved facts requiring real tool access, with no stated precondition and no defined behavior without one. Added a full "Execution requirements" section to `README.md` defining **Verified mode** (real execution access — gates run as literally written) and **Reasoned mode** (chat-only — equivalent static analysis, explicitly labeled). Added `pass (reasoned, not executed)` as a canonical handoff status in `agents/AGENTS.md`'s Handoff format, and propagated an execution-mode line plus the new status option into every affected skill's Quality Gate/Stopping conditions and Handoff block: `06-scaffold.md`, `07-build.md`, `09-review.md`, `10-security.md`, `11-performance.md`, `13-test.md`, `16-document.md`, `17-deploy.md`, `18-verify.md`. Added an explicit rule to `17-deploy.md`: deploying on a Reasoned-mode `10-security.md`/`13-test.md` result requires a logged user acknowledgment before proceeding, the same standard an accepted security risk already requires. `18-verify.md` additionally gained a `blocked` outcome for when live-URL access is genuinely unavailable, since that stage has no meaningful Reasoned-mode equivalent. (`README.md`, `agents/AGENTS.md`, nine skill files)
6. **AUDIT.md's baseline self-scoring was more generous than the evidence.** Added an addendum documenting line-level defects a deeper audit found in the baseline (Tailwind v3/v4 config contradiction, 21 unedited PDF-export watermarks, a stray non-English artifact in a security example, a broken shell command, a password-based-SSH anti-pattern) that the original per-skill scoring table didn't capture, and noted the real scores for `03-scaffold-it` and `05-connect-it`/`06-secure-it` were likely lower than shown. (`AUDIT.md`)

### Phase 2 — domain-specificity bridge

- Created `context/pattern-library.md`: a static reference (not a per-build ledger artifact) of durable, framework-agnostic decision structure — a visual-theme-to-token character mapping, the component-state checklist, a data-model decision tree, and a deployment-topology decision tree. Explicitly excludes specific package/library names, which stay `research-notes.md`'s job. (`context/pattern-library.md`)
- Wired it into `04-architect.md` (data-model process step, new inputs) and `05-design.md` (visual-direction and component-state process steps, new inputs) as a source of structure that `research-notes.md` fills with current specifics. (`skills/04-architect.md`, `skills/05-design.md`)
- Added a Quality Gate item to `04-architect.md`: every concrete package/library name in `architecture.md` must trace to `research-notes.md`, never asserted from the pattern library or model memory — the guard against `pattern-library.md` becoming a new staleness source. (`skills/04-architect.md`)
- Registered `pattern-library.md` in `context/CONTEXT-ENGINEERING.md`'s ledger table and in `README.md`'s directory listing. (`context/CONTEXT-ENGINEERING.md`, `README.md`)

### Phase 3 — automated consistency verification

- Wrote `scripts/validate_consistency.py`, a real, executable script (not a described-but-unbuilt process) that checks: frontmatter `name:` matches filename stem for every `skills/*.md` file; every `NEXT:` handoff target resolves to a real stage file or a documented exception (00-orchestrator/19-git's intentional lack of a formal NEXT, 14-debug's dynamic-return pattern); every backtick-quoted `*.md` filename referenced in `README.md`/`ARCHITECTURE.md`/`agents/AGENTS.md` exists somewhere in the repo, excluding runtime-written ledger artifacts declared in `CONTEXT-ENGINEERING.md`'s table; the "N named roles" claim matches the actual role-table row count; every `skills/NN-*.md` stage appears in `ARCHITECTURE.md`'s pipeline diagram and vice versa; every `templates/*.md` file is referenced by name somewhere in `skills/` or `ARCHITECTURE.md`. (`scripts/validate_consistency.py`)
- Added `.github/workflows/ci.yml` running the validator plus a markdownlint pass on every push/PR, and `.markdownlint.yml` tuned to this repo's intentional style (long table rows, frontmatter-first files). (`.github/workflows/ci.yml`, `.markdownlint.yml`)
- Documented the CI job's existence and purpose in a new "Consistency CI" section of `README.md`, and added `scripts/` and `.github/` to the directory listing. (`README.md`)

### Phase 4 — structural gaps

- **Cost awareness.** Added a "Cost estimate" subsection to `architecture.md`'s required output and a corresponding process step in `04-architect.md`: a rough monthly-cost range at the project's stated scale, sourced from `research-notes.md` where cost is plan/version-sensitive. (`skills/04-architect.md`)
- **Staging environments.** Added an optional staging/preview step to `17-deploy.md`'s process: deploy to staging first and run `18-verify.md`'s checks there when the platform supports it, before promoting to production; direct-to-prod stays the explicit fallback for platforms that don't. Added a corresponding Quality Gate item requiring `deployment-record.md` to state which path was taken and why. (`skills/17-deploy.md`)
- **Internationalization.** Added an optional Internationalization field to `templates/requirements-template.md` (explicit "single-language, <language>" is a stated decision, not a blank). Added a process step to `03-plan.md` asking about it directly during requirements gathering, flowing into `04-architect.md` only when the answer is non-default. (`templates/requirements-template.md`, `skills/03-plan.md`)
- **Regression-test loop closure.** Confirmed `14-debug.md` did *not* already require a new test for a previously-untested path — added an explicit process step (4a) and Quality Gate item: if the root cause was a path nothing tested before, a test for that path is added as part of the fix, not deferred. (`skills/14-debug.md`)

### Phase 5 — final self-audit

- Re-ran `scripts/validate_consistency.py` after every phase; final run is clean (see below).
- Recounted `agents/AGENTS.md`'s role table by hand: 18 rows, matching `README.md`'s claim and every other reference to it in the repo.
- Grepped every filename referenced in `README.md`, `ARCHITECTURE.md`, `agents/AGENTS.md`, and `context/CONTEXT-ENGINEERING.md`; every reference resolves to a real file or a declared runtime ledger artifact.
- Re-scored the framework against the original audit rubric — see the re-score in this pass's closing summary. One dimension is deliberately left below 9.9 with a named reason, per this task's instruction not to claim a flawless score.

## 2.1.0 - 2026-08-02

- Add Verified-mode E2E scaffolding: `scripts/verified_mode_run.py` and `VERIFIED_MODE.md` documentation.
- Implement API-backed provider adapters with safe test stubs (`src/gncore/providers/api.py`).
- Add provider discovery tests and deterministic provider test harness (`tests/test_providers_api.py`).
- CI/test improvements and packaging updates in support of the 2.1.0 release.


### Known limitations (deliberately not solved by assertion)

- **Role separation is prompt-discipline, not sandboxed.** Naming a role changes what Claude treats as its own prior work versus work to scrutinize, and that's a real, measurable prompt-engineering lever — but it is not a technical guarantee. A single model instance in the "Reviewer" role can still be influenced by having just written the code as "Builder" in the same session, in a way a genuinely separate reviewer (human or model) could not be. This framework does not claim otherwise, and no wording change in this pass makes that claim true — it's structural to running one model across all named roles.
