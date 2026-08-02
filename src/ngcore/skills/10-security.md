---
name: 10-security
description: Adversarial security review of the full codebase, configuration, and dependencies. Zero-tolerance gate — no Critical or High finding may be marked "won't fix" or deferred, even if the user asks, without an explicit documented risk-acceptance from the user for that specific finding.
---


## Role

Security Engineer. Approach the codebase as an attacker, not as a colleague double-checking their own work — this is why the role is separate from Builder and Reviewer.

## Inputs

- Full codebase, `context/dependency-manifest.md`, `context/integration-notes.md`, `context/architecture.md` (for PII/payment flags set in stage 04).

## Outputs

- `context/security-report.md`: every finding with severity (Critical/High/Medium/Low), location, exploit scenario in one sentence, and the exact fix.

## Process

### 1. Map the attack surface

Entry points (routes, forms, uploads, webhooks, websockets), auth boundaries, data flow (input → processing → storage → output), trust boundaries (client/server/DB/third-party), sensitive assets (PII, credentials, payment data, admin functions).

### 2. Checklist, applied to every route/handler/component — mark pass/fail, don't skip any

**Input handling** — validated for type/length/format/range; sanitized before use; uploads restricted by type/size/magic-bytes; query params cast and validated; headers never trusted for security decisions.
**Injection** — parameterized queries only (no string concatenation); no shell/exec calls built from user input; XML external entity resolution disabled; user input never reaches a template engine unescaped; log/header values stripped of CRLF/newlines.
**Auth & session** — passwords hashed with a modern algorithm (never reversible encryption or unsalted hashes); session tokens random and sufficiently long; expiry enforced; JWT signature verified server-side, algorithm pinned (`alg: none` rejected); OAuth state parameter validated; CORS not wildcard on any authenticated route.
**Secrets** — zero hardcoded credentials, API keys, or connection strings in code or in version control history; `.env` files gitignored; secrets never logged.
**XSS/CSP** — output encoded per context (HTML/attribute/JS/URL); a real Content-Security-Policy is set, not a no-op one; `dangerouslySetInnerHTML`-equivalents audited individually.
**CSRF** — state-changing requests protected (token or same-site cookies) where session-based auth is used.
**Dependencies** — every package in `dependency-manifest.md` checked against known CVEs for its pinned version.
**Infra/config** — security headers present (HSTS, X-Content-Type-Options, frame-ancestors); admin/debug endpoints not exposed in production; error responses don't leak stack traces or internal paths to the client.
**Payments (if applicable)** — no raw card data handled outside a PCI-scoped, tokenized flow; webhook signatures verified.

### 3. Severity assignment

Critical: remote unauthenticated compromise of data or systems. High: authenticated compromise, or unauthenticated data exposure. Medium: requires unusual conditions or limited-impact exposure. Low: defense-in-depth / best-practice gaps.

### 4. Fix, don't just report

For every finding, output the exact corrected code, not a description of the problem alone.

## Quality Gate

- [ ] Every checklist item in step 2 was applied to every relevant file, not sampled.
- [ ] Zero unresolved Critical or High findings remain.
- [ ] Any Medium/Low left unresolved is explicitly logged with a reason, visible to the user.
- [ ] Every fix was applied as code, not left as prose description only.

## Stopping conditions

This gate does not pass with any open Critical/High finding. If the user wants to ship anyway, that requires an explicit, individually-named risk acceptance per finding in `decision-log.md` — the Security Engineer role documents the risk clearly but does not have authority to silently waive it, and the orchestrator must still block automated deployment (`17-deploy.md`) pending that explicit acceptance.

**Execution mode (partial):** most of the checklist in step 2 is static code/config reading and is unaffected by execution access. The execution-dependent part is live dependency-CVE lookup (step 2's "Dependencies" item) and any check that requires actually running the app (e.g., confirming a security header is present on a real response). Without live/web access for those specific items, mark them `(reasoned, not executed)` — reasoned from the pinned version and known-CVE knowledge as of training, explicitly flagged as unverified against a live advisory database. See `README.md`'s "Execution requirements" section. **This distinction matters most here**, because `17-deploy.md` requires an explicit user acknowledgment before deploying on a Reasoned-mode security result — see that skill's Quality Gate.

## Handoff

```text
STAGE: 10-security
ROLE: Security Engineer
STATUS: pass | pass (reasoned, not executed)
ARTIFACT(S) WRITTEN: context/security-report.md
GATE RESULT: <count of Critical/High/Medium/Low, and "0 unresolved Critical/High" or the escalation>
ESCALATIONS: none | <finding requiring explicit user risk-acceptance>
NEXT: 13-test (after 11-performance and 12-accessibility also complete)
```
