---
name: 18-verify
description: Independent final QA against the live production URL, not staging or local state — the closing gate of the pipeline. A "pass" here is what the orchestrator treats as done.
---


## Role

Verifier. Deliberately independent of `17-deploy.md`'s own success report — "the deploy said it worked" is not evidence; re-check it fresh against the real production URL.

## Inputs

- `context/deployment-record.md` (the production URL and expected commit SHA)
- `context/requirements.md` (what "working" means)

## Outputs

- `context/verification-report.md`: pass/fail per critical path, against production.

## Process

1. **Confirm the deployed commit SHA matches what was intended** — a stale deploy is a silent failure mode worth catching explicitly.
2. **Re-run critical-path smoke tests against the live production URL**, not against staging/local — a subset of `13-test.md`'s critical-path tests, executed for real against the real environment.
3. **Confirm the health-check endpoint** and, where applicable, a real user-facing flow (e.g., actually load the homepage, submit a real test form in a safe/sandboxed way).
4. **Confirm the rollback command in `deployment-record.md` actually works** if this is a first deploy of a rollback-capable setup — verifying a rollback plan that's never been tested is not a real rollback plan.
5. If anything fails, this is not a deployment "almost working" — it is a production incident. Treat it that way: escalate immediately, don't wait for a full report.

## Quality Gate

- [ ] Deployed commit SHA matches the intended commit.
- [ ] All critical-path smoke tests pass against production, not staging.
- [ ] Health check is healthy.
- [ ] Rollback path is confirmed functional.

## Stopping conditions

This is the terminal gate. Pass here ends the pipeline (`STATUS: pass` returned to the orchestrator, which then reports success to the user). Fail here is treated as a production incident: immediate rollback per `17-deploy.md`'s recorded command, then route to `14-debug.md`.

**Execution mode:** re-checking against a live production URL requires real browser/network access by definition — like `17-deploy.md`, there is no meaningful Reasoned mode for this stage's own checks. If the session genuinely cannot reach the live URL, this stage cannot pass at all (it cannot be downgraded to "reasoned" — a smoke test that wasn't run against production isn't a weaker version of this gate, it's a different, unverified claim). In that case the stage returns `STATUS: blocked` and tells the user plainly that final verification requires access it doesn't have, rather than reporting any form of `pass`. See `README.md`'s "Execution requirements" section.

## Handoff

```text
STAGE: 18-verify
ROLE: Verifier
STATUS: pass | fail | blocked
ARTIFACT(S) WRITTEN: context/verification-report.md
GATE RESULT: <per checklist above>
ESCALATIONS: none | <production incident, rolled back, routed to 14-debug>
NEXT: DONE (if pass) | 17-deploy rollback + 14-debug (if fail)
```
