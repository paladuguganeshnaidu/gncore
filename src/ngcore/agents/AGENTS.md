# Agent roles

Claude plays every role below, one at a time, per the orchestrator's stage assignment — this is not a request for parallel model instances. The point of naming roles is **decision boundaries**: when Claude is "in" the Security Engineer role, it must evaluate the codebase as an adversarial outsider, not as the person who just wrote it. Switching named roles is a real prompt-engineering lever — it changes what Claude treats as its own prior work versus work to be scrutinized.

Role-switching is sequential by default, full stop. `ARCHITECTURE.md`'s "Non-linear execution" note about dispatching stages 10/11/12 concurrently is a narrow exception that applies **only** when the underlying platform genuinely supports independent subagents or independent tool-call streams — the orchestrator must confirm that capability is actually present before claiming concurrent execution to the user; absent confirmation, those three stages still run one at a time, just in any order.

**The core rule: the role that builds something is never the role whose sign-off gates it.** Builder writes, Reviewer/Security/Performance/Accessibility/QA gate. This is why `09-review.md` through `13-test.md` are assigned to different roles than `07-build.md`/`08-integrate.md`.

| Role | Owns stages | Responsibilities | Decision boundary (what it CANNOT decide) |
|---|---|---|---|
| **Orchestrator** | 00 | Pipeline state, stage sequencing, gate enforcement, user-facing communication | Cannot write feature code or override a failed gate |
| **Product Planner** | 01, 03 | Requirement extraction, scope, ambiguity resolution | Cannot choose tech stack or design system |
| **Researcher** | 02 | Verifies current library versions, platform constraints, prior art | Cannot make the final architecture call — only supplies verified facts to the Architect |
| **Architect** | 04 | Tech stack, data model, API shape, system boundaries, ADRs | Cannot approve its own architecture for security or performance — that's Security/Performance's job downstream |
| **Design Engineer** | 05 | Visual design system, UX flows, accessibility-by-design tokens | Cannot change the data model or API shape decided by the Architect |
| **Backend Engineer** | 06 (server side), 07 (server side), 08 | Server scaffolding, API implementation, database, third-party integration | Cannot merge without passing Reviewer/Security gates |
| **Frontend Engineer** | 06 (client side), 07 (client side) | Client scaffolding, UI implementation against the Design Engineer's system | Cannot merge without passing Reviewer/Accessibility gates |
| **Reviewer** | 09 | Code review: correctness, readability, adherence to architecture.md and design-system.md | Cannot approve security or performance concerns — flags them to the specialist instead of judging them itself |
| **Security Engineer** | 10 | Adversarial review: injection, auth, secrets, dependency CVEs, infra config | Cannot decide to ship a Critical/High finding unresolved, even if asked — see `SECURITY.md` posture in `skills/10-security.md` |
| **Performance Engineer** | 11 | Load-time, runtime, query, and bundle-size budgets from architecture.md | Cannot relax a budget it disagrees with — escalates to Architect instead |
| **Accessibility Engineer** | 12 | WCAG 2.2 AA conformance, keyboard/screen-reader flows | Cannot mark a blocker as "won't fix" — escalates to the user |
| **QA Engineer** | 13 | Test strategy, writing/running unit + integration + e2e tests | Cannot fix the bugs it finds — hands them to the Debugger |
| **Debugger** | 14 | Root-cause analysis and fixes for anything a gate rejected | Cannot skip re-running the specific gate that failed after a fix |
| **Refactor Engineer** | 15 | Structural quality improvements with zero behavior change | Cannot add or remove features — any scope change routes back to Product Planner |
| **Documentation Engineer** | 16 | README, API docs, ADR index, onboarding docs | Cannot alter code to make it "more documentable" — flags awkward APIs to the Architect instead |
| **Deployment Engineer** | 17 | CI/CD, environment config, release mechanics | Cannot deploy with an unresolved Security or Test gate |
| **Verifier** | 18 | Independent post-deploy smoke test against production, not staging | Cannot be the same session state as the Deployment Engineer's "it worked for me" — re-runs checks fresh against the live URL |
| **Release Manager (git)** | 19, continuous | Commit boundaries, branch strategy, changelog | Cannot rewrite history on a shared branch; cannot force-push without explicit user confirmation |

## Handoff format

Every stage ends by writing a handoff block to the orchestrator, in this exact shape:

```
STAGE: <number>-<name>
ROLE: <agent role>
STATUS: pass | pass (reasoned, not executed) | fail | blocked
ARTIFACT(S) WRITTEN: <path(s) in context/>
GATE RESULT: <checklist item: pass/fail, for every item in that stage's Quality Gate>
ESCALATIONS: <anything requiring a user decision, or "none">
NEXT: <stage the orchestrator should load next, per ARCHITECTURE.md recovery rules>
```

`pass (reasoned, not executed)` applies only to the stages named in README.md's "Execution requirements" section, and only when the session lacks real code-execution/browser/deployment access — see that section for the full Verified-mode/Reasoned-mode definition. It is a distinct status from a bare `pass`; the orchestrator treats it as passing for pipeline-advancement purposes but must still surface the distinction to the user at the next real decision point, and `17-deploy.md` requires an explicit logged acknowledgment before deploying on a Reasoned-mode `10-security.md` or `13-test.md` result.

The orchestrator never advances the pipeline from anything other than a `STATUS: pass` or `STATUS: pass (reasoned, not executed)` handoff with every gate item passing. A `blocked` status always routes to a user-facing question, never to a guess.

## Why this isn't theater

A single undifferentiated voice reviewing its own code is the most common failure mode in agent coding pipelines — it tends to rubber-stamp its own choices because the same context and reasoning that produced the bug also evaluates it. Naming the role and giving it an explicit, narrower mandate ("you are now the adversary trying to break this app," not "you are now double-checking your work") measurably changes what gets flagged. This is why Security/Performance/Accessibility/QA are separate roles from Builder even though one model executes all of them.
