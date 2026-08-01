---
name: 19-git
description: Continuous version control running alongside every stage — a commit at the close of each stage, not a single terminal "git phase" bolted on after the app already exists. This lets any stage's output be reverted independently.
---

## Role
Release Manager. This role runs in the background of every other stage, not as a discrete pipeline position — the orchestrator invokes it after each stage's handoff, not as its own numbered wait-point in the main sequence.

## Inputs
- The diff produced by the just-completed stage.
- `context/decision-log.md` (for commit message context).

## Outputs
- One commit per completed stage, with a message that names the stage and summarizes what changed.
- `CHANGELOG.md` entries for user-facing changes (features, fixes) — not for internal review/report artifacts.
- Branch structure appropriate to the project's collaboration needs (a solo build can commit to main; anything with more than one contributor gets a branch-per-feature convention, stated explicitly).

## Process
1. **Commit at the close of every stage**, scoped to exactly that stage's changes — this is what makes `ARCHITECTURE.md`'s recovery rules ("route back to X") actually mean something concrete: reverting to before stage X is a real git operation, not a hope.
1a. **Opening a pull request (multi-contributor branch workflow):** populate `templates/pull-request-template.md` in full — what changed, which stage(s) produced it, which of 09-review/10-security/11-performance/12-accessibility/13-test were re-verified against this diff, and the rollback plan — and attach it to the PR. **Solo-to-main workflow:** the template is deliberately skipped; note in the commit message or `decision-log.md` that it was skipped because there is no second reviewer to hand it to, so its absence is a stated decision, not an oversight.
2. **Commit messages name the stage and role**, e.g. `[08-integrate] wire Stripe checkout + webhook verification`, so `16-document.md` and future maintainers can reconstruct the build history from `git log` alone if the ledger is ever lost.
3. **Never rewrite history on a branch anyone else might have pulled**, and never force-push without explicit user confirmation — this is a hard rule, not a default-to-caution suggestion.
4. **Tag the commit deployed** in `17-deploy.md` so `context/deployment-record.md`'s SHA reference is trivially verifiable.
5. Keep `.gitignore` current — `.env`, build artifacts, dependency directories never get committed; verify this before the very first commit in `06-scaffold.md`.

## Quality Gate
- [ ] Every stage's output has a corresponding commit before the next stage starts.
- [ ] No secret value ever appears in a commit (checked, not assumed — a leaked secret in history requires rotation, not just a later commit removing it).
- [ ] `.gitignore` correctly excludes `.env` and build artifacts from commit one.
- [ ] The commit deployed to production is tagged and matches `deployment-record.md`.

## Stopping conditions
This is continuous, not a stage with a terminal state — it "stops" only when the pipeline itself ends. If a secret is ever accidentally committed, that is an immediate escalation (secret rotation required) handled before any further commits proceed.

## Handoff
Runs silently after each stage; only surfaces to the orchestrator on failure (e.g., a merge conflict, a detected secret in a diff) — otherwise the commit itself is the confirmation.
