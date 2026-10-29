---
name: documentation
description: "Write technical references, tutorials, API documentation and migration guides from verified software behavior."
license: MIT
---

# GNCore Documentation

Version: 7.0.0rc1

## Choose the work

Identify the reader and task. Derive claims from code, schemas and observed commands; preserve identifiers, placeholders and supported version boundaries.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Task-oriented documentation with reproducible examples, prerequisites, error cases and migration or compatibility notes when needed.

Execute practical examples in an isolated environment, check local links and compare documented commands/schema fields with implementation. Mark examples that require unavailable services.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Derive examples from the real help/API contract, including prerequisites, changed defaults and compatibility boundaries. Make examples copyable without inventing flags or endpoints. Include a realistic failure and safe recovery route, such as an existing output collision, while preserving user data. Label untested examples explicitly and verify commands, links and migration behavior when execution is available.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `documentation-translation` | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. |
| `technical-writing` | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. |
| `documentation-api` | Document API behavior from the implementation and contract, with examples users can reproduce. |

## Focused procedures

### Technical Localization (`documentation-translation`)

Identify source locale, target locale, audience, and approved glossary. Preserve code, placeholders, links, units, legal meaning, and formatting tokens. Flag ambiguous source text instead of guessing. Use locale-appropriate dates and numbers; do not translate identifiers. Verify UI length and right-to-left behavior when relevant.

### Technical Writing (`technical-writing`)

Inspect the actual behavior and audience before drafting. Put the shortest successful path first, identify prerequisites and supported versions, and verify commands and output. Keep terminology consistent and label assumptions. Do not document unimplemented behavior or expose credentials. Update nearby references when a public command or interface changes.

### API Documentation (`documentation-api`)

Inspect routes, schemas, authentication, error behavior, and versioning. Document required and optional fields, examples, pagination, rate limits, and known constraints. Verify examples against a safe environment or schema. Keep secrets and personal data out. Clearly flag undocumented behavior instead of guessing.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
