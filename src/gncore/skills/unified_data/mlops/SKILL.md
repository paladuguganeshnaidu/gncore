---
name: mlops
description: "Package, serve, monitor and roll back models with reproducible artifacts and explicit promotion gates."
license: MIT
---

# GNCore MLOps

Version: 7.0.0rc1

## Choose the work

Link model weights to data/split/code/dependency versions and the exact serving schema. Separate offline validation from live service reliability, drift and business outcomes.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A versioned model bundle, preprocessing/serving contract, release gate, monitoring thresholds and rollback plan.

Round-trip the artifact in a clean environment, compare prediction parity, test incompatible schemas, failed loads and rollback. Keep promotion and traffic changes pending explicit deployment authorization.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Promote an immutable compatible bundle of model, preprocessor, feature contract, data/code identity and runtime. Verify serving parity and wrong/missing/reordered-input behavior before exposure. Gate promotion on both labeled quality and operational constraints, then stage rollout with a compatible rollback target. Feature or prediction drift is a diagnostic signal, not measured accuracy loss; track delayed labels and quality slices separately and define action thresholds for each.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Promote a compatible immutable model/preprocessor/schema/data/code/runtime bundle and verify missing, reordered or malformed serving inputs against training behavior.
- Check artifact trust before executable deserialization; hashes establish identity, not safety. Gate on quality and operations, align delayed labels by maturity/cohort and retain a compatible rollback target.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `experiment-tracking` | Make model experiments traceable across code, data, configuration, environment, and artifacts. |
| `model-serving` | Package model inference behind a reliable API with validation, resource limits, and observable behavior. |
| `mlops` | Package, register, and monitor models with reproducible artifacts and explicit release gates. |
| `ml-experiment-tracking` | Make model experiments comparable with consistent splits, metrics, configuration, and artifact provenance. |
| `model-card` | Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions. |
| `hardware-ml` | Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs. |
| `mlops-artifact-contract` | Model artifact and provenance. |
| `mlops-serving-contract` | Prediction service contract. |
| `mlops-drift-monitoring` | Drift and model monitoring. |
| `mlops-promotion-rollback` | Model promotion and rollback. |

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
