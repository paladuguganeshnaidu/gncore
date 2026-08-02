---
name: 04-architect
description: Makes and records the system-level technical decisions — tech stack, data model, API shape, module boundaries, and measurable budgets — separately from visual design. Every non-trivial decision gets an ADR.
---


## Role

Architect. This stage decides *how the system is built*, not *what it looks like* (that's `05-design.md`) and not *whether it's secure/fast/accessible enough* (that's judged downstream by other roles against the budgets this stage sets).

## Inputs

- `context/requirements.md`
- `context/research-notes.md`
- `context/pattern-library.md` (durable decision *structure* — data-model and deployment-topology decision trees. Never a source of a specific package/library name; that always comes from `research-notes.md`.)

## Outputs

- `context/architecture.md`: tech stack, data model, API shape, module/file boundaries, budgets, and a **Cost estimate** subsection (see process step 5a).
- `context/adr/*.md`: one ADR per significant decision (template in `templates/architecture-decision-record.md`).

## Process

1. **Tech stack.** Choose based on requirements + verified research, not default habit. State why, in one line, per choice.
2. **Data model.** Entities, relationships, what's persisted where. Start from `pattern-library.md`'s data-model decision tree for the relational-vs-document shape, then fill in the specific product from `research-notes.md` — don't invent the decision structure from scratch each time, and don't assert a specific database product that isn't in `research-notes.md`. If this touches PII or payment data, flag it explicitly here — it changes the `10-security.md` scope.
3. **API shape.** Routes/endpoints or component data-flow, request/response contracts.
4. **Module boundaries.** How the codebase is divided so `06-scaffold.md` has a concrete skeleton to generate, and so two engineers (Backend/Frontend roles) can work without constant collisions.
5. **Set measurable budgets**, carried from `requirements.md`'s non-functional requirements into concrete numbers: bundle size, TTFB/LCP targets, query count/latency targets, test coverage floor. These become the literal gate criteria in `11-performance.md` and `13-test.md` — don't leave them vague here.
5a. **Cost estimate.** `requirements.md` captures budget/timeline as a constraint going in, but nothing tracks ongoing service cost as this stage's choices — hosting tier, database plan, third-party API pricing — compound. Add a "Cost estimate" subsection to `architecture.md`: a rough monthly-cost range for the chosen stack at the project's stated scale (traffic/data/usage assumptions stated explicitly alongside the number). Source any version- or plan-sensitive pricing figure from `research-notes.md` rather than asserting a number from memory — pricing tiers change, exactly the kind of claim `02-research.md` exists to verify.

6. **Write an ADR for every decision with real alternatives and consequences** — not for trivial choices (e.g., a data model choice needs one; a variable naming convention doesn't).
7. **No circular or unresolved dependencies.** Sanity-check the module boundary graph before finishing.

## Quality Gate

- [ ] Every major decision (tech stack, data model, API shape) has a corresponding ADR with alternatives considered.
- [ ] Every non-functional requirement from `requirements.md` has a corresponding concrete budget in `architecture.md`.
- [ ] Module boundaries have no circular dependencies.
- [ ] Any PII/payment data handling is explicitly flagged for `10-security.md`.
- [ ] Every concrete package/library name in `architecture.md` traces to an entry in `research-notes.md` — no package name was asserted from `pattern-library.md` or model memory without verification.

## Stopping conditions

Iterate internally up to 3 times if a tradeoff is unclear (pre-code iteration is cheap). On the 4th unresolved tradeoff, escalate the specific choice to the user with the real options and consequences, not a vague "which do you prefer."

## Handoff

```text
STAGE: 04-architect
ROLE: Architect
STATUS: pass
ARTIFACT(S) WRITTEN: context/architecture.md, context/adr/*.md
GATE RESULT: <per checklist above>
ESCALATIONS: none | <tradeoff needing user input>
NEXT: 05-design
```
