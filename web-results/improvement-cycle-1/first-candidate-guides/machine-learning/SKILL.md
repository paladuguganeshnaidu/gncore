---
name: machine-learning
description: "Develop classical ML and time-series experiments with leakage-safe splits, baselines and deployment-relevant evaluation."
license: MIT
---

# GNCore Machine Learning

Version: 7.0.0rc1

## Choose the work

Define the prediction moment, target, unit of independence and decision cost before selecting a model. Fit learned preprocessing only on training data and keep holdout evaluation separate from tuning.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Reproducible data/split/preprocessing and baseline pipeline, recorded configuration, appropriate metrics and error analysis.

Test split disjointness and feature availability, preprocessing parity and baseline improvement. Report per-group/horizon failures and unknowns; never infer measured accuracy from an unexecuted plan.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Start from the prediction moment, horizon and deployment population. Audit every feature for point-in-time availability, then choose entity/time split boundaries that match that population. Fit preprocessing and selection within training folds, tune on validation and leave final evaluation sealed. Compare a simple baseline and report task-appropriate metrics: imbalance-aware operating points for classification, or suitable regression/forecast measures with sample/group counts; avoid inferring generalization from a leaky split or one favorable score.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Choose deployment-time and entity boundaries from the prediction moment; fit preprocessing, feature selection, calibration and thresholds only within training/validation scope.
- Retain an untouched final test and task-appropriate baseline/metrics: classification imbalance and alert budgets when relevant, regression/forecast metrics otherwise; report group support and uncertainty.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `ml-problem-framing` | Decide whether a machine learning approach fits the task, data, constraints, and failure costs. |
| `ml-dataset-audit` | Audit dataset provenance, schema, representativeness, label quality, leakage, and split strategy. |
| `ml-preprocessing-pipeline` | Build deterministic preprocessing that prevents leakage and preserves training-to-serving parity. |
| `ml-model-train` | Implement a reproducible model training run with configuration, baseline, checkpoints, and evaluation. |
| `ml-model-evaluation` | Evaluate model quality, uncertainty, subgroup behavior, and representative errors against a baseline. |
| `ml-model-improvement` | Improve a model through controlled experiments with a fixed evaluation protocol and root-cause analysis. |
| `ml-llm-evaluation` | Evaluate an LLM feature with representative tasks, rubrics, adversarial cases, latency, and cost. |
| `ml-rag` | Build and evaluate retrieval-augmented answers with source access controls and abstention. |
| `ml-finetuning` | Assess fine-tuning suitability and prepare a controlled, leakage-safe fine-tuning workflow. |
| `ml-release-monitor` | Prepare a model release with provenance, compatibility, rollback, and drift monitoring gates. |
| `machine-learning` | Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation. |
| `model-training` | Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation. |
| `train` | Build and run a reproducible model training workflow with a baseline, tracked configuration, and held-out evaluation. |
| `preprocess` | Design a repeatable preprocessing pipeline that preserves schema, prevents leakage, and records transformations. |
| `evaluate` | Evaluate model quality with leakage-safe splits, task-appropriate metrics, baselines, and error analysis. |
| `improve` | Find evidence-based model improvements through error analysis and controlled experiments against a fixed baseline. |
| `data-preparation` | Prepare reproducible model datasets while preventing leakage and preserving provenance. |
| `feature-engineering` | Build features that are valid at prediction time and reproducible across training and inference. |
| `model-evaluation` | Evaluate model quality with valid splits, suitable metrics, uncertainty, and error analysis. |
| `feature-engineering-practice` | Create leakage-safe, interpretable features that match the model's serving-time information. |
| `time-series` | Analyze and forecast time-indexed data with temporal splits, leakage controls, and useful uncertainty. |

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
