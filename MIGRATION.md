# Migration guide: baseline `website-builder-skills` → `website-builder-elite`

## If you have no in-flight project
Just start using `skills/00-orchestrator.md`. There's nothing to migrate.

## If you have an in-flight project built with the baseline framework

The baseline's phases map onto this framework's stages roughly as follows. Use this to figure out where to re-enter the pipeline — you do not need to restart from `01-think`.

| Baseline phase | Roughly maps to | What to do |
|---|---|---|
| Phase 1 (dream-it, Requirements Document) | `01-think` + `03-plan` | Copy the existing Requirements Document into `context/requirements.md`, reformatted to `templates/requirements-template.md`. Add explicit non-functional requirements (performance/accessibility/security/coverage) — the baseline doc almost certainly doesn't have concrete numbers for these; set them now, don't skip it. |
| Phase 2 (design-it, Technical Specification) | `04-architect` + `05-design` | Split the old Technical Specification: tech stack/data model/API shape → `context/architecture.md` (write ADRs retroactively for the decisions that mattered); visual/UX content → `context/design-system.md`. This split is the most valuable single migration step — do it even if you do nothing else. |
| Phase 3 (build-it, Codebase) | `06-scaffold` + `07-build` | If the codebase already exists, treat it as already scaffolded/built. Immediately run `09-review.md` against it before doing anything else — the baseline had no independent review step, so this is very likely the first real review the code has had. |
| Phase 4 (connect-it) | `08-integrate` | Audit against this stage's Quality Gate directly — specifically, grep for hardcoded credentials, since the baseline's env-var discipline was good but not gate-enforced. |
| Phase 5 (secure-it, Security Report) | `10-security` | Re-run in full. The baseline's security pass happened once, after connect-it, with no re-check after any later change — treat any existing security report as stale unless it postdates the current code exactly. |
| — (no baseline equivalent) | `11-performance`, `12-accessibility`, `13-test` | Run these from scratch — the baseline never covered them. Expect to find real gaps; that's the point of adding them. |
| Phase 6 (launch-it) | `17-deploy` | Re-run only if `10-security` and `13-test` weren't both passing at the original deploy time (very likely true, since neither performance/accessibility/test gates existed in the baseline). |
| Phase 7 (fix-it) | `14-debug` | Same taxonomy, now explicitly consuming a specific failing gate instead of an ad-hoc bug report — no change needed to how you invoke it, just feed it a specific `*-report.md` finding where one exists. |
| Phase 8 (refactor, implied but not a real baseline stage) | `15-refactor` | Only run this after `13-test.md` has been established for the first time — refactoring before any test coverage exists is unsafe regardless of which framework you're using. |
| 09-git-it | `19-git` | Going forward, commit at stage boundaries instead of in one batch. No need to rewrite existing history. |
| 10-readme-it | `16-document` | Re-run once `context/architecture.md` and `context/adr/*.md` exist, so the ADR index has real content. |

## The one thing to do even if you migrate nothing else

Split any existing "design/spec" document into `architecture.md` (system decisions) and `design-system.md` (visual/UX decisions), and run `10-security.md`, `11-performance.md`, `12-accessibility.md`, and `13-test.md` against the existing codebase once, cold. In every baseline build these four stages either ran once-and-stale or never ran at all — this is where migration effort pays off fastest.
