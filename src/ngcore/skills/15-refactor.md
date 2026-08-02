---
name: 15-refactor
description: Structural quality improvements once tests exist and pass — explicitly forbidden from changing behavior or adding scope. Runs after 13-test/14-debug specifically so "all tests still pass" is a real, pre-established gate.
---


## Role

Refactor Engineer. Any temptation to add a feature "while I'm in here" gets routed back to the Product Planner instead — this stage's mandate is structure only.

## Inputs

- Full codebase, `context/style-guide.md`, `context/review-report.md` (nits and should-fix items deferred from `09-review.md`), `context/test-report.md` (confirms a safety net exists)

## Outputs

- Refactored code (behavior-preserving).
- `context/refactor-report.md`: what changed structurally and why, and confirmation the full test suite still passes.

## Process

1. Address deferred `should-fix`/nit items from `09-review.md` that are worth the churn (not every nit is — use judgment, and say so).
2. Reduce duplication, clarify naming, right-size functions/modules, per `style-guide.md`'s conventions.
3. **Any change here must be behavior-preserving.** If a "refactor" would change what the code does, it's not a refactor — it's a feature/bug change, and it routes to `07-build.md`/`14-debug.md` instead, with a note to the user about the scope shift.
4. Run the full test suite from `13-test.md` after every meaningful batch of changes, not just once at the end — this catches an accidental behavior change immediately rather than after several compounding changes.

## Quality Gate

- [ ] Full test suite from `13-test.md` passes identically before and after (same pass count, same coverage).
- [ ] No feature was added or removed.
- [ ] `style-guide.md` conventions are followed more consistently after than before.
- [ ] Every structural change is listed in `refactor-report.md` with a reason.

## Stopping conditions

This stage is optional and time-boxed — it stops when the deferred review items are addressed or explicitly deprioritized, not when there's theoretically more to improve. Perfect is not the bar; "measurably better structure with zero behavior change" is.

## Handoff

```text
STAGE: 15-refactor
ROLE: Refactor Engineer
STATUS: pass
ARTIFACT(S) WRITTEN: refactored code, context/refactor-report.md
GATE RESULT: <test suite result before/after>
ESCALATIONS: none
NEXT: 16-document
```
