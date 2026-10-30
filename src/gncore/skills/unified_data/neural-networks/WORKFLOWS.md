# GNCore Neural Networks: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Tensor and target contracts (`nn-tensor-contracts`)

Write a table of each layer's input/output axes, dtype, device and target encoding. Test batch size one and non-square shapes to expose accidental broadcasting. Make reductions explicit and reject an incompatible target before the optimizer step.

### Gradient verification (`nn-gradient-check`)

Use numerical gradients for custom mathematical operations or suspected derivative errors. Compare analytic and central-difference derivatives on a tiny float64 smooth case, restoring parameters after each perturbation. Freeze random/stateful behavior and use identical reduction/data for both evaluations; avoid nonsmooth activation boundaries. Check extreme-logit stability separately. Standard-layer changes may need forward/backward or tiny-batch update tests instead of a full numerical-gradient sweep.

### Diagnose a stalled training step (`nn-training-debug`)

Freeze randomness and overfit a tiny labeled batch. Inspect finite inputs/logits/loss, gradient norms, learning rate and before/after weights. Verify zero_grad/backward/step order and whether parameters are registered and require gradients before changing architecture.

### Loss and activation semantics (`nn-loss-semantics`)

Match binary, multiclass or multilabel targets to the selected loss API. Determine whether it expects logits or probabilities, target dtype, class dimension, masking and reduction. Test a hand-computed example; avoid applying softmax twice or averaging padding as real targets.

### Initialization and signal flow (`nn-initialization`)

Inspect layer fan-in/fan-out and activation distributions on a fixed batch. Compare saturation, activation variance and gradient norms across depth. Change initialization or normalization only with a diagnosed signal-flow problem and retain a measured baseline.

### Evaluation and validation isolation (`nn-evaluation-modes`)

Switch training-dependent layers to evaluation behavior and disable gradient recording for inference. Verify validation does not update parameters or running statistics and restore training mode afterward. Test repeated predictions and stateful layers explicitly.
