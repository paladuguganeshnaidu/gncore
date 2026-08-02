# Context engineering

The baseline framework's biggest hidden cost: every skill's "Input" was effectively "the whole conversation so far." That works for a 20-minute build and falls over on anything real — token cost balloons, and worse, the model has no way to distinguish a **settled decision** from a **stale draft that was later overridden**.

This framework replaces conversational replay with a **ledger**: a small set of living documents in `context/`, each owned by exactly one stage, read by only the stages that need them.

## The ledger

| File | Owner (writes) | Readers | Contains |
| --- | --- | --- | --- |
| `clarify.md` | 01-think | 03-plan | Resolved ambiguities, explicit assumptions and their risk level |
| `research-notes.md` | 02-research | 04-architect | Verified current facts (library versions, platform limits) with source and date checked |
| `pattern-library.md` | none (static reference, not written per-build) | 04-architect, 05-design | Durable, framework-agnostic decision structure (theme-to-token character, component-state checklist, data-model and deployment-topology decision trees) — never a source of a specific package name; that's always `research-notes.md` |
| `requirements.md` | 03-plan | 04, 05, 07, 16, 18 | Purpose, audience, features, non-functional requirements (perf/a11y/security budgets), explicit non-goals |
| `architecture.md` | 04-architect | 05, 06, 07, 08, 10, 11, 15 | Tech stack, data model, API shape, module boundaries, budgets (bundle size, TTFB, coverage floor) |
| `adr/*.md` | 04-architect (+ any stage that makes a reversible-decision-with-tradeoffs) | 16-document, future maintainers | One Architecture Decision Record per significant choice: context, decision, alternatives considered, consequences |
| `design-system.md` | 05-design | 06, 07, 12 | Tokens, components, states, copy voice |
| `style-guide.md` | 07-build (first write), amended by 15-refactor | 07, 09, 15 | Coding conventions actually observed in the codebase — not aspirational, descriptive of what's there |
| `dependency-manifest.md` | 06-scaffold, amended by 08-integrate | 10-security, 15-refactor | Every package, its version, and why it was chosen (links to research-notes.md where relevant) |
| `review-report.md` / `security-report.md` / `performance-report.md` / `accessibility-report.md` / `test-report.md` | 09–13 respectively | 14-debug, 18-verify | Findings, severity, status |
| `deployment-record.md` | 17-deploy | 18-verify, 19-git | Platform, env vars (names only, never values), commit SHA deployed, rollback command |
| `decision-log.md` | any stage, append-only | orchestrator, all stages | One line per user-facing decision made and when — the audit trail |

## Retrieval rules

1. **A stage reads only the ledger files its contract lists**, not the full history. `07-build.md` reads `architecture.md` and `design-system.md` — it does not need `research-notes.md` once `architecture.md` has already incorporated the relevant facts.
2. **Ledger files are compressed summaries, not transcripts.** When a stage produces a ledger artifact, it writes conclusions and rationale, not the back-and-forth that produced them. The back-and-forth is disposable; the decision is not.
3. **Superseded content is marked, not deleted.** If `architecture.md` changes mid-build, the old value moves to a "Superseded" section with the reason, rather than silently vanishing — this is what lets `16-document.md` produce an honest ADR index later instead of reconstructing history from memory.
4. **Priority order when context is tight:** `requirements.md` and `architecture.md` (the contract) > the specific report the current stage is gating on > everything else. Never drop `requirements.md` to save space — every downstream stage's gate ultimately checks against it.
5. **Style is tracked, not re-inferred.** `style-guide.md` exists so 07-build.md and 15-refactor.md don't have to re-scan the whole codebase to guess naming conventions every time — read the file.
6. **Dependencies are tracked, not re-derived.** `dependency-manifest.md` is the single source of truth `10-security.md` checks for known CVEs — it should never need to re-parse `package.json` from scratch to know what's installed and why.

## What this buys

- A stage loaded on day 4 of a build gets exactly the ~5 files relevant to its job, not a replay of days 1–3.
- Gates become checkable against a fixed artifact (`requirements.md`) instead of a moving target (whatever was said in chat).
- The audit trail (`decision-log.md`) makes `16-document.md`'s job mechanical instead of speculative.
