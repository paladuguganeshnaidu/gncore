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

## Deliver and verify

Training/evaluation loops, resumable checkpoints, resource/precision configuration and an experiment record linking data, code and metrics.

Test uninterrupted versus resumed steps, accumulation/loss scaling, train/eval mode and validation isolation. Profile actual hardware before throughput claims; report nondeterminism and unexecuted distributed checks.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Checkpoint a compatible training state, not just parameters: optimizer, schedule, precision scaler, RNG, sampler/data position, progress and environment/data identity. For gradient accumulation, save partial gradient state deliberately or checkpoint at a completed optimizer-step boundary. Compare an uninterrupted and resumed short trajectory with the same batches and configuration; use justified numerical tolerances and report device/distributed nondeterminism rather than promising bitwise equality without evidence.

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

## Focused procedures

### Model Fine-Tuning (`fine-tuning`)

Confirm the base model, license constraints, data rights, objective, validation method, hardware, and budget. Inspect existing training code and use the least costly method that can answer the goal. Keep validation data separate, record model and tokenizer revisions, and save to a new checkpoint path. Do not launch paid or long-running jobs without explicit approval.

### PyTorch Training (`pytorch-training`)

Inspect the installed PyTorch version and existing dataset/model interfaces. Set train/eval modes correctly, move batches and model to the same device, clear gradients, and use inference mode for evaluation. Save checkpoints atomically to a new path and include enough state to resume when requested. Start with a tiny smoke run before a full run.

### TensorFlow and Keras Training (`tensorflow-training`)

Inspect TensorFlow/Keras version and data pipeline semantics. Keep preprocessing consistent, avoid validation leakage, configure callbacks explicitly, and save to a new artifact path. Check output shapes and a small batch first. Do not assume GPU availability or start a long training run without user approval.

### Deep Learning Engineering (`deep-learning`)

Inspect framework versions, model inputs/outputs, tensor shapes, precision, memory limits, and baseline. Verify loss/activation compatibility, masking, gradient flow, and train/eval modes. Keep validation data out of gradient updates and log checkpoints with configuration. Do not launch GPU-intensive jobs or replace checkpoints without approval. Diagnose with a tiny batch before scaling.

### Checkpoint and resume equivalence (`dl-checkpoint-resume`)

Save model, optimizer, scheduler, precision scaler, step and relevant RNG/data-loader state together. Load with device/version awareness. Compare a short uninterrupted run with a stopped/resumed run under stated determinism limits; avoid treating weights alone as a resumable training state.

### Mixed precision correctness (`dl-mixed-precision`)

Establish a float32 reference and identify numerically sensitive operations. Use the framework's current autocast/scaling APIs, unscale before clipping, and check skipped/nonfinite steps. Compare validation quality and peak memory on the target device rather than assuming a speedup.

### Gradient accumulation (`dl-gradient-accumulation`)

Define the desired effective batch and loss normalization, including a short final microbatch. Zero gradients at the correct accumulation boundary, and step the optimizer/scheduler only when an update occurs. Compare gradients with a single equivalent batch where layer behavior permits.

### Distributed training correctness (`dl-distributed-training`)

Define rank ownership, sampler sharding, collective order and globally reduced metrics. Check duplicate/dropped examples, uneven last batches and checkpoint ownership. Prove a tiny multi-process run before scaling and retain logs for rank-specific hangs; do not silently launch a costly cluster.

### Transfer learning and freezing (`dl-transfer-learning`)

Verify checkpoint provenance and architecture compatibility. Explicitly select frozen/trainable parameters, normalization behavior and optimizer groups. Compare a frozen baseline with bounded fine-tuning on the same split; verify frozen weights remain unchanged.

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
