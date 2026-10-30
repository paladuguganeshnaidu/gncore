---
name: deep-learning
description: "Engineer reproducible deep-learning training, checkpointing, fine-tuning and distributed optimization."
license: MIT
---

# GNCore Deep Learning

Version: 7.0.0rc1

## Choose the work

Inspect framework/device versions, precision, memory and data parallelism. Preserve optimizer/scheduler/scaler/RNG state when resume equivalence matters; scale after a small local correctness run.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Training/evaluation loops, resumable checkpoints, resource/precision configuration and an experiment record linking data, code and metrics.

Test uninterrupted versus resumed steps, accumulation/loss scaling, train/eval mode and validation isolation. Profile actual hardware before throughput claims; report nondeterminism and unexecuted distributed checks.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Checkpoint a compatible training state, not just parameters: optimizer, schedule, precision scaler, RNG, sampler/data position, progress and environment/data identity. For gradient accumulation, save partial gradient state deliberately or checkpoint at a completed optimizer-step boundary. Compare an uninterrupted and resumed short trajectory with the same batches and configuration; use justified numerical tolerances and report device/distributed nondeterminism rather than promising bitwise equality without evidence.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Tie model/data/config/environment identity to optimizer, scheduler, RNG, sampler, AMP and accumulation state; use a completed-update restart boundary when partial state is absent.
- Normalize by actual valid-example/token counts across microbatches/ranks and advance schedules only on completed optimizer updates; compare controlled interrupted and uninterrupted trajectories.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `fine-tuning` | Plan or implement a parameter-efficient or full fine-tuning workflow with controlled data and cost. |
| `pytorch-training` | Implement PyTorch training loops with correct device, optimizer, checkpoint, and evaluation handling. |
| `tensorflow-training` | Build TensorFlow/Keras training workflows with explicit data, callbacks, and evaluation behavior. |
| `deep-learning` | Develop deep learning code with explicit tensor shapes, stable optimization, and reproducible evaluation. |
| `dl-checkpoint-resume` | Checkpoint and resume equivalence. |
| `dl-mixed-precision` | Mixed precision correctness. |
| `dl-gradient-accumulation` | Gradient accumulation. |
| `dl-distributed-training` | Distributed training correctness. |
| `dl-transfer-learning` | Transfer learning and freezing. |

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
