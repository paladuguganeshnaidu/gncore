---
name: 08-integrate
description: Wires up authentication, database, payments, and third-party services against the architecture already decided — with every credential handled as an environment variable, never hardcoded, and every integration smoke-tested before the stage is considered done.
---


## Role

Backend Engineer.

## Inputs

- `context/architecture.md` (data model, API shape)
- `context/requirements.md` (which integrations are actually needed — don't add ones that weren't scoped)

## Outputs

- Integration code (auth flows, DB connections/migrations, payment/webhook handlers, third-party API clients).
- Updated `context/dependency-manifest.md` for any new packages added.
- `context/integration-notes.md`: which services are wired, what credentials each needs (names only), and how to obtain them.

## Process

1. **Database:** apply the schema from `architecture.md`'s data model. Write migrations, not ad-hoc schema edits. Never store secrets or connection strings in code — env vars only.
2. **Auth:** implement exactly the flow `architecture.md` specified (session/JWT/OAuth/etc). Session handling, password hashing (if applicable), and token expiry all need explicit, correct choices here — this is exactly the surface `10-security.md` will scrutinize hardest next, so don't leave placeholders.
3. **Payments (if applicable):** never process raw card data directly unless the architecture explicitly calls for PCI-scope handling (it usually shouldn't — use a hosted/tokenized flow). Webhook signature verification is mandatory, not optional.
4. **Third-party APIs:** wrap each in a single client module (per `architecture.md`'s module boundaries), with credentials from env vars and rate-limit/error handling.
5. **Every credential is an environment variable**, added to `.env.example` by name only, and documented in `integration-notes.md` with instructions for the user on where to obtain the real value. Ask the user for real credentials only when needed to actually test the integration, and never echo a secret value back in plain text once received.
6. **Smoke-test every integration** — a real (or realistic sandboxed/test-mode) call through each wired path, not just "the code compiles."

## Quality Gate

- [ ] Zero hardcoded credentials anywhere in the codebase — grep confirms it.
- [ ] Every integration has a passing smoke test.
- [ ] Payment/webhook handlers verify signatures where applicable.
- [ ] `.env.example` and `integration-notes.md` are complete and in sync with what the code actually reads from `process.env` (or equivalent).
- [ ] Database changes are migrations, not direct schema edits.

## Stopping conditions

Done when every integration in scope is wired, credentialed via env vars, and smoke-tested. A failing smoke test routes to `14-debug.md`, not a silent retry loop.

## Handoff

```text
STAGE: 08-integrate
ROLE: Backend Engineer
STATUS: pass
ARTIFACT(S) WRITTEN: integration code, context/integration-notes.md, updated dependency-manifest.md
GATE RESULT: <per checklist above>
ESCALATIONS: none | <credential needed from user>
NEXT: 09-review
```
