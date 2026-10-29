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

## Deliver and verify

A versioned model bundle, preprocessing/serving contract, release gate, monitoring thresholds and rollback plan.

Round-trip the artifact in a clean environment, compare prediction parity, test incompatible schemas, failed loads and rollback. Keep promotion and traffic changes pending explicit deployment authorization.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

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

## Focused procedures

### Reproducible ML Experiments (`experiment-tracking`)

Capture the source revision, dataset/version, configuration, seed, dependencies, model identifier, metrics, and artifact location. Keep secrets out of logs. Make repeated runs distinguishable and avoid overwriting artifacts. Use the repository's existing tracker; add a new service only when requested.

### Model Serving and Inference APIs (`model-serving`)

Trace model loading and inference lifecycle, validate inputs and output shapes, set appropriate timeouts and resource limits, and preserve version identity. Handle cold starts and model errors explicitly. Do not deploy, expose endpoints, or change production configuration unless requested. Measure latency and memory before claiming capacity.

### MLOps and Model Release (`mlops`)

Trace training data, code, dependencies, model artifact, evaluation, and serving contract. Define reproducible build metadata, compatibility checks, rollback path, and monitoring for drift and failures. Keep credentials outside artifacts. Do not deploy, promote, or alter production traffic without explicit authorization. Separate offline evidence from live performance and define an owner for alerts.

### Machine Learning Experiment Tracking (`ml-experiment-tracking`)

Define the question and baseline before changing code. Record data version, split, code revision, config, seed, environment, metrics, and artifact path for every run. Compare like with like and account for randomness. Keep experiments isolated and avoid overwriting outputs. Do not introduce a tracking service or upload sensitive data without approval.

### Model Documentation (`model-card`)

Use only verified project evidence for training data, method, metrics, and provenance. State intended and excluded uses, evaluation setup, subgroup coverage, limitations, monitoring, and update cadence. Mark unknowns plainly. Do not infer consent, representativeness, fairness, or regulatory status without evidence.

### Edge and Hardware-Constrained ML (`hardware-ml`)

Identify target processor, runtime, memory, latency, power, and accuracy requirements. Measure an unoptimized baseline on representative inputs. Compare quantization or compression with task metrics and worst-case behavior; verify supported operators and numerical drift. Keep original artifacts and provide a rollback path. Do not claim deployment readiness from desktop measurements.

### Model artifact and provenance (`mlops-artifact-contract`)

Bundle model and preprocessing state with input schema, dependency versions, data/split identity and verified evaluation. Hash files and round-trip the bundle in a clean environment. Keep credentials and unnecessary training records outside the artifact.

### Prediction service contract (`mlops-serving-contract`)

Validate feature names/order, dtype, missingness and batch bounds before inference. Use the artifact's exact preprocessing and test predictions against an offline fixture. Define load failures, timeouts and incompatible model/schema errors without silently changing predictions.

### Drift and model monitoring (`mlops-drift-monitoring`)

Separate input drift, label/target changes, prediction drift and service reliability. Define reference windows, delayed-label availability, thresholds and an accountable response. Test a synthetic shifted fixture; do not label input drift alone as measured accuracy degradation.

### Model promotion and rollback (`mlops-promotion-rollback`)

Compare candidate and baseline on the same accepted evaluation set and compatibility checks. Prepare canary/shadow criteria, immutable model identities and a tested rollback path. Keep actual production promotion and traffic changes pending deployment authorization.

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
