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

## Deliver and verify

A reproducible text/token contract, baseline, evaluation by relevant label/language and explicit handling of long/empty/unknown input.

Test Unicode, special tokens, mask shapes, offset/label alignment and duplicate leakage. Measure task quality separately from fluency; do not present generated labels as verified ground truth.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Make the supervision unit explicit before tokenization: document word/subtoken alignment, special-token and padding masks, and reconstruction for task-level metrics. Define truncation and long-input behavior so labels/spans do not silently shift or disappear. When fitting/evaluating a model, group correlated documents, authors or conversations appropriately. Check short, empty, Unicode, padded and truncated examples; token accuracy dominated by padding is not entity or conversation quality.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `nlp` | Build NLP pipelines that respect language, label quality, privacy, and task-specific evaluation. |
| `nlp-token-alignment` | Token and label alignment. |
| `nlp-text-classification` | Text classification baseline. |
| `nlp-sequence-modeling` | Sequence masks and generation. |
| `nlp-evaluation` | Language and task evaluation. |

## Focused procedures

### Natural Language Processing (`nlp`)

Inspect languages, tokenization, labels, privacy constraints, and intended use. Establish a simple baseline and split by user/document when duplicates could leak. Evaluate per-class and per-language behavior, not only one aggregate metric. Minimize retention of raw text and redact sensitive examples. Treat generated labels as noisy; document model and data provenance. Do not claim factuality or safety from benchmark scores alone.

### Token and label alignment (`nlp-token-alignment`)

Preserve original text and tokenizer offsets. Define labels for special tokens and subwords, mask ignored positions from loss/metrics and test Unicode plus truncation boundaries. Inspect a hand-labeled example end to end instead of assuming token counts align.

### Text classification baseline (`nlp-text-classification`)

Split related documents/users before fitting vocabulary or learning preprocessing. Establish a simple lexical baseline, inspect label imbalance and tune thresholds on validation data. Report per-class support/errors and test empty, long and out-of-language input.

### Sequence masks and generation (`nlp-sequence-modeling`)

Specify padding side, attention masks, causal visibility, target shifting and stop tokens. Check a short hand-computed sequence for future-token leakage and ignored padding. Bound generation length and verify batch versus single-input behavior.

### Language and task evaluation (`nlp-evaluation`)

Choose metrics that correspond to classification, retrieval, extraction or generation, and retain dataset/language provenance. Examine errors by language/length and independent source groups. Separate semantic accuracy from surface similarity and reviewer preference.

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
