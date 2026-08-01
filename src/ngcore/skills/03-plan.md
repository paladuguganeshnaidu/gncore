---
name: 03-plan
description: Produces the approved requirements document — the single source of truth every later gate checks against. Uses templates/requirements-template.md.
---

## Role
Product Planner (main pass).

## Inputs
- `context/clarify.md`
- `context/research-notes.md`

## Outputs
- `context/requirements.md` (use `templates/requirements-template.md` as the shape)

## Process
1. Translate `clarify.md`'s resolved picture into: purpose, audience, a prioritized feature list (must/should/could), explicit non-goals, non-functional requirements (performance budget, accessibility target, security posture, test coverage floor), internationalization needs, and constraints.
2. **Set real non-functional requirements, don't leave them as boilerplate.** If the user hasn't specified a performance/accessibility/security bar, propose a sensible default for the project type and say so plainly (e.g., "I'll target WCAG 2.2 AA and a sub-2.5s load time unless you'd rather I optimize for something else") — this is what makes `11-performance.md` and `12-accessibility.md` checkable later instead of vague.
2a. **Ask about internationalization explicitly, don't assume single-language.** If the user hasn't said, ask directly whether multiple languages/locales are needed; if the answer is no, record "single-language, <language>" in `requirements.md`'s Internationalization field per `templates/requirements-template.md` rather than leaving it blank. Only carry this into `04-architect.md` (locale routing, content structure, RTL support, etc.) when the answer is non-default — a single-language project shouldn't gain i18n architecture it doesn't need.
3. **Write explicit non-goals.** This is what prevents scope creep from being silently reintroduced in `07-build.md`.
4. Present the document to the user in plain language: what it does, who it's for, what's in v1, what's explicitly not in v1.
5. Get explicit approval. "Looks fine" counts; silence does not.

## Quality Gate
- [ ] `requirements.md` exists and follows the template.
- [ ] Every non-functional requirement (perf/a11y/security/coverage) has a concrete, checkable value — not "should be fast" but a number or standard.
- [ ] Non-goals are explicit, not implied.
- [ ] The user has explicitly approved the document (checkbox in the template is checked).

## Stopping conditions
Stop iterating once the user approves. If the user requests a change, apply it and re-present the diff (not the whole document again) for a fast re-approval.

## Handoff
```
STAGE: 03-plan
ROLE: Product Planner
STATUS: pass
ARTIFACT(S) WRITTEN: context/requirements.md
GATE RESULT: <per checklist above>
ESCALATIONS: none
NEXT: 04-architect
```
