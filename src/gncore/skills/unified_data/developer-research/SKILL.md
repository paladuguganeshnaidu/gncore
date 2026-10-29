---
name: developer-research
description: "Investigate technical options, papers, APIs and reproducible engineering experiments from primary evidence."
license: MIT
---

# GNCore Technical Research

Version: 7.0.0rc1

## Choose the work

Define the decision, constraints and evidence standard. Inspect code and primary documentation; distinguish source claims, reproduction results and inference.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

A cited technical comparison or bounded prototype with version assumptions, unresolved questions and a recommendation tied to the actual project.

Trace material claims to sources or measurements, compare methods and environments fairly, and label unavailable reproduction evidence. Do not invent citations, capabilities or benchmark results.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Rank supplied evidence by provenance, version and direct relevance; keep primary evidence separate from secondary assertions and inference. Check units, defaults and compatibility contracts, not merely renamed symbols. Design the smallest experiment that distinguishes competing explanations, with bounded deadlines and realistic tolerances. Record assumptions, unavailable evidence and observations that would change the recommendation. Never describe a planned reproduction as completed.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `research-synthesis` | Synthesize supplied or sourced evidence with provenance, disagreement, and uncertainty kept visible. |
| `research-api-compatibility` | API and dependency compatibility. |
| `research-paper-reproduction` | Research result reproduction. |
| `research-technical-decision` | Evidence-backed technical decision. |

## Focused procedures

### Research Synthesis (`research-synthesis`)

Translate the question into scope, date range, and evidence standard. Prioritize primary sources; record citation details and distinguish source claims from your synthesis. Compare methods and note conflicting findings, limitations, and missing evidence. Do not invent citations, quotations, or consensus. State when evidence is insufficient or likely outdated.

### API and dependency compatibility (`research-api-compatibility`)

Inspect installed versions, call sites, official release notes and primary API documentation. Reproduce the needed behavior in a minimal fixture and record migration/compatibility constraints before recommending a dependency change.

### Research result reproduction (`research-paper-reproduction`)

Record the paper revision, dataset rights/splits, baseline, metric definitions and compute budget. Reproduce the smallest decisive experiment first, keep deviations visible and separate a partial implementation from replication of published results.

### Evidence-backed technical decision (`research-technical-decision`)

Compare options on the project's actual constraints, prototype the uncertain boundary and cite primary evidence with dates/versions. State what would change the recommendation; do not substitute general popularity for workload evidence.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
