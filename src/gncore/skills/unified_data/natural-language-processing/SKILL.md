---
name: natural-language-processing
description: "Build tokenization, text classification, sequence labeling and language-model adaptation pipelines."
license: MIT
---

# GNCore NLP and Language Pipelines

Version: 7.0.0rc1

## Choose the work

Identify language, normalization, target labels and document/user split units. Preserve token/label alignment, truncation policy, padding masks and privacy boundaries.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A reproducible text/token contract, baseline, evaluation by relevant label/language and explicit handling of long/empty/unknown input.

Test Unicode, special tokens, mask shapes, offset/label alignment and duplicate leakage. Measure task quality separately from fluency; do not present generated labels as verified ground truth.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Make the supervision unit explicit before tokenization: document word/subtoken alignment, special-token and padding masks, and reconstruction for task-level metrics. Define truncation and long-input behavior so labels/spans do not silently shift or disappear. When fitting/evaluating a model, group correlated documents, authors or conversations appropriately. Check short, empty, Unicode, padded and truncated examples; token accuracy dominated by padding is not entity or conversation quality.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Define label units, special/padding masks and whether offsets address original or normalized text; retain mappings through normalization and truncation.
- Group correlated conversations/documents, preserve label-bearing long content and reconstruct/deduplicate overlapping windows before task-level evaluation; test short, padded and truncated boundaries.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `nlp` | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. |
| `nlp-token-alignment` | Token and label alignment. |
| `nlp-text-classification` | Text classification baseline. |
| `nlp-sequence-modeling` | Sequence masks and generation. |
| `nlp-evaluation` | Language and task evaluation. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
