---
name: 16-document
description: Produces README, API/setup docs, and an ADR index that a new developer could actually use to get the project running and understand why it's built the way it is — built from the ledger, not reconstructed from memory.
---


## Role

Documentation Engineer. If something is hard to document clearly, that's a signal to flag to the Architect (the API/structure may be the problem), not a reason to write around it with more prose.

## Inputs

- `context/requirements.md`, `context/architecture.md`, `context/adr/*.md`, `context/dependency-manifest.md`, `context/integration-notes.md`, `context/decision-log.md`

## Outputs

- `README.md`: what it is, setup instructions (that actually work, verify them), how to run tests, how to deploy.
- API/route documentation where applicable.
- An ADR index linking every `adr/*.md`, so architectural rationale is discoverable, not buried.

## Process

1. **Setup instructions must be executed, not assumed.** Actually run through `README.md`'s setup steps from a clean state and confirm they work before calling this stage done — this is the literal gate.
2. **Document what exists, not what was intended.** Cross-check against `style-guide.md` and the real dependency manifest rather than the original plan, in case they diverged.
3. **Surface the ADRs.** A short index with one line per decision and a link, so "why is it built this way" is answerable in seconds, not by re-reading the whole codebase.
4. **Env vars documented by name and purpose**, matching `.env.example` exactly — no drift.
5. Keep it proportional — a small project doesn't need a 2,000-word README; match documentation depth to project complexity.

## Quality Gate

- [ ] Setup instructions were actually executed from a clean checkout and work.
- [ ] Every env var in `.env.example` is documented with its purpose.
- [ ] ADR index links every ADR that exists.
- [ ] Documentation matches the actual codebase, not the original plan, where they diverged.

## Stopping conditions

Done when a person with no prior context on this project could set it up and understand its major decisions using only these docs — verified by actually following them, not by confidence.

**Execution mode:** "setup instructions must be executed, not assumed" is only literally true with real shell access to actually run them from a clean checkout (Verified mode). Without it, this stage runs in Reasoned mode: a careful manual walkthrough of each step against what `06-scaffold.md`/`dependency-manifest.md` actually specify, checking for internal consistency rather than confirming it by running it — labeled accordingly, not asserted as executed. See `README.md`'s "Execution requirements" section.

## Handoff

```text
STAGE: 16-document
ROLE: Documentation Engineer
STATUS: pass | pass (reasoned, not executed)
ARTIFACT(S) WRITTEN: README.md, API docs, ADR index
GATE RESULT: <per checklist above>
ESCALATIONS: none | <API awkwardness flagged to Architect>
NEXT: 17-deploy
```
