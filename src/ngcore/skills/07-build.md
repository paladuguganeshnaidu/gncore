---
name: 07-build
description: Implements every feature from requirements.md against architecture.md and design-system.md, writing unit tests alongside each feature rather than deferring all testing to a later stage.
---


## Role

Backend Engineer (server-side features) / Frontend Engineer (client-side features).

## Inputs

- `context/requirements.md`
- `context/architecture.md`
- `context/design-system.md`
- `context/style-guide.md`

## Outputs

- Feature code, organized per `architecture.md`'s module boundaries.
- Unit tests alongside each feature (not deferred to `13-test.md` — that stage owns integration/e2e and the overall test *strategy*, but unit tests for logic are written here, next to the logic, while context is freshest).
- Updates to `context/style-guide.md` if a new convention is established (append, don't silently diverge).

## Process

1. **Build directly against `requirements.md`'s feature list, one feature at a time.** Track coverage: every `must` and `should` feature needs a corresponding implementation before this stage is done; `could` features are explicitly optional and should be flagged if skipped.
2. **Reference design tokens and components from `design-system.md`**, never hardcode a color/spacing/font value that already has a token.
3. **Follow `style-guide.md`'s established conventions.** If none exist yet (first feature), establish one and write it there.
4. **Write a unit test alongside any non-trivial logic** (business rules, data transforms, validation) — not for trivial glue code.
5. **Never invent scope.** If something feels missing, it's either in `requirements.md`'s non-goals (don't build it) or it's a genuine gap — flag it to the orchestrator rather than silently adding it.
6. **Handle errors and edge cases explicitly** — empty states, loading states, failure states — matching the states `design-system.md` already defined for each component.
7. Commit at logical feature boundaries (see `19-git.md`), not one giant commit at the end.

## Quality Gate

- [ ] Every `must` and `should` feature in `requirements.md` maps to implemented code.
- [ ] Every non-trivial logic path has a unit test, and it passes.
- [ ] No hardcoded design values where a token exists.
- [ ] No feature exists that isn't traceable to `requirements.md` (no silent scope addition).
- [ ] Empty/loading/error states are implemented for every component that defines them in `design-system.md`.

## Stopping conditions

This stage is done when the feature list is fully covered (or explicitly descoped with the user's sign-off) and the build/lint/type-check/unit-test commands from `06-scaffold.md` all pass. Any failure routes to `14-debug.md` for that specific feature rather than blocking the whole stage indefinitely.

**Execution mode:** with real shell access, "all pass" means those commands were actually run against the new code (Verified mode). Without it, this stage runs in Reasoned mode: a manual trace-through of each new unit test against the logic it covers, explicitly flagged as not executed. See `README.md`'s "Execution requirements" section.

## Handoff

```text
STAGE: 07-build
ROLE: Backend Engineer / Frontend Engineer
STATUS: pass | pass (reasoned, not executed)
ARTIFACT(S) WRITTEN: feature code, unit tests, style-guide.md updates
GATE RESULT: <per checklist above, with explicit feature-coverage list>
ESCALATIONS: none | <requirements gap found>
NEXT: 08-integrate
```
