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

## Deliver and verify

A shape-checked model and training step, gradient/overfit probes, configuration and finite-loss evidence; retain the simplest useful baseline.

Compare analytic gradients with finite differences on a tiny case, check finite values and nonzero parameter updates, and overfit a tiny batch. Validate activation/loss compatibility and evaluation-mode behavior.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `nn-tensor-contracts` | Tensor and target contracts. |
| `nn-gradient-check` | Gradient verification. |
| `nn-training-debug` | Diagnose a stalled training step. |
| `nn-loss-semantics` | Loss and activation semantics. |
| `nn-initialization` | Initialization and signal flow. |
| `nn-evaluation-modes` | Evaluation and validation isolation. |

## Focused procedures

### Tensor and target contracts (`nn-tensor-contracts`)

Write a table of each layer's input/output axes, dtype, device and target encoding. Test batch size one and non-square shapes to expose accidental broadcasting. Make reductions explicit and reject an incompatible target before the optimizer step.

### Gradient verification (`nn-gradient-check`)

Choose a tiny float64 differentiable model away from activation kinks. Perturb one parameter by plus/minus epsilon and compare the central finite difference with the analytic gradient using absolute and relative tolerances. Restore parameters after each probe; explain the epsilon/error tradeoff.

### Diagnose a stalled training step (`nn-training-debug`)

Freeze randomness and overfit a tiny labeled batch. Inspect finite inputs/logits/loss, gradient norms, learning rate and before/after weights. Verify zero_grad/backward/step order and whether parameters are registered and require gradients before changing architecture.

### Loss and activation semantics (`nn-loss-semantics`)

Match binary, multiclass or multilabel targets to the selected loss API. Determine whether it expects logits or probabilities, target dtype, class dimension, masking and reduction. Test a hand-computed example; avoid applying softmax twice or averaging padding as real targets.

### Initialization and signal flow (`nn-initialization`)

Inspect layer fan-in/fan-out and activation distributions on a fixed batch. Compare saturation, activation variance and gradient norms across depth. Change initialization or normalization only with a diagnosed signal-flow problem and retain a measured baseline.

### Evaluation and validation isolation (`nn-evaluation-modes`)

Switch training-dependent layers to evaluation behavior and disable gradient recording for inference. Verify validation does not update parameters or running statistics and restore training mode afterward. Test repeated predictions and stateful layers explicitly.

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

For a tiny CPU-only gradient and learning probe, run `python scripts/gradient_probe.py` from this skill folder. It checks a synthetic XOR fixture; it does not establish production model quality.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
