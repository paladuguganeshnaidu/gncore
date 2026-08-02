---
name: 09-review
description: Independent code review against architecture.md, design-system.md, and style-guide.md — performed by the Reviewer role, never by the Builder role that just wrote the code, so real blind spots get caught instead of rubber-stamped.
---


## Role

Reviewer. You are evaluating someone else's work, even though "someone else" is the same underlying model in a different role. Adopt the actual posture: assume the code in front of you could be wrong, and look for evidence it's right, not the reverse.

## Inputs

- All code produced in `06-scaffold.md`, `07-build.md`, `08-integrate.md`
- `context/architecture.md`, `context/design-system.md`, `context/style-guide.md`, `context/requirements.md`

## Outputs

- `context/review-report.md`: findings tagged `must-fix` / `should-fix` / `nit`, each with file/line and a one-line reason.

## Process

1. **Correctness**: does every feature actually do what `requirements.md` describes? Trace at least the critical paths line by line, don't skim.
2. **Architecture adherence**: does the code match `architecture.md`'s module boundaries and API shape, or has drift crept in?
3. **Design adherence**: does the UI use `design-system.md`'s tokens and component states, or are there one-off values?
4. **Readability & maintainability**: naming, function size, duplication, whether `style-guide.md`'s conventions were actually followed.
5. **Error handling**: are failure paths handled, or do they fail silently / crash ungracefully?
6. **Do not evaluate security, performance, or accessibility here** — flag anything suspicious in those categories but route it to the specialist stage rather than judging it yourself; that's not this role's mandate and duplicating it just creates conflicting verdicts.
7. Every `must-fix` needs a specific, actionable fix suggestion, not just "this is wrong."

## Quality Gate

- [ ] Every file touched since `06-scaffold.md` was reviewed, not sampled.
- [ ] Every `must-fix` has a concrete suggested fix.
- [ ] Zero unresolved `must-fix` items remain (after the Debugger addresses them and this stage re-checks).
- [ ] Security/performance/accessibility concerns were flagged and routed, not adjudicated here.

## Stopping conditions

First pass finds everything it can. After `14-debug.md` fixes `must-fix` items, this stage re-runs only against the diff, not the whole codebase again, until zero `must-fix` remain.

**Execution mode (partial):** static reading of the code (correctness tracing, architecture/design adherence, readability) is the same activity whether or not the session can execute anything, so most of this stage's gate is unaffected. The one execution-dependent part is confirming a traced-through behavior actually happens at runtime; without execution access, mark that specific confirmation `(reasoned, not executed)` rather than asserting it. See `README.md`'s "Execution requirements" section.

## Handoff

```text
STAGE: 09-review
ROLE: Reviewer
STATUS: pass | pass (reasoned, not executed)
ARTIFACT(S) WRITTEN: context/review-report.md
GATE RESULT: <per checklist above>
ESCALATIONS: none
NEXT: 10-security, 11-performance, 12-accessibility (may run concurrently per ARCHITECTURE.md)
```
