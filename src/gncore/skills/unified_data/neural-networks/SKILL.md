---
name: neural-networks
description: "Design and debug neural networks through tensor contracts, gradient checks, loss semantics and tiny-batch experiments."
license: MIT
---

# GNCore Neural Networks

Version: 7.0.0rc1

## Choose the work

Write shapes, dtypes, target encoding and loss reduction explicitly. Check forward and backward numerical behavior on a tiny deterministic batch before increasing architecture or compute.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Shape/label/reduction-aware model or numerical code with task-relevant forward/backward evidence and configuration; retain the simplest useful baseline.

Check loss/activation compatibility and evaluation behavior. For custom derivatives or suspected gradient bugs, compare controlled central differences. For training changes, verify finite values, parameter updates and a tiny-batch diagnostic; label unexecuted accelerator checks.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Choose shapes, label semantics, reductions and dtype from the mathematical contract. Use stable logit-space losses and task-relevant invalid-input checks. Numerical derivatives are useful for custom operations or suspected gradient bugs; control stochastic and stateful behavior. For training changes, test parameter updates and a tiny-batch learning diagnostic before scaling.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Match tensor axes, label semantics, dtype and reduction; compute losses in stable logit space rather than taking a log of probabilities that can underflow.
- For custom derivatives or suspected gradient errors, freeze stochastic/stateful behavior and check central differences away from kinks; reject malformed/nonfinite inputs and verify tiny-batch parameter updates when training changes.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `nn-tensor-contracts` | Tensor and target contracts. |
| `nn-gradient-check` | Gradient verification. |
| `nn-training-debug` | Diagnose a stalled training step. |
| `nn-loss-semantics` | Loss and activation semantics. |
| `nn-initialization` | Initialization and signal flow. |
| `nn-evaluation-modes` | Evaluation and validation isolation. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

For a tiny CPU-only gradient and learning probe, run `python scripts/gradient_probe.py` from this skill folder. It checks a synthetic XOR fixture; it does not establish production model quality.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
