Viewed SKILL.md:1-90

Based on the GNCore [neural-networks](../../src/gncore/skills/unified_data/neural-networks/SKILL.md) skill, here is the pure reasoning analysis:

---

### 1. Output Shape

For input $X \in \mathbb{R}^{2 \times 3}$, weights $W \in \mathbb{R}^{3 \times 1}$, and bias $b \in \mathbb{R}^{1}$:
- **Matrix Multiplication**: $XW$ results in shape `(2, 1)`.
- **Bias Addition**: Adding $b$ of shape `(1,)` broadcasts along the leading batch dimension to `(2, 1)`.
- **Output Shape**: **`(2, 1)`** (both for unnormalized linear logits $Z = XW + b$ and post-activation probabilities $\hat{y} = \sigma(Z)$).
- **Contract Verification**: The output shape `(2, 1)` matches the target shape `(2, 1)` directly, preventing accidental vector/matrix broadcasting bugs (e.g., unintentional outer products from shape `(2,)` vs `(2, 1)`).

---

### 2. Appropriate Binary Loss and Input Semantics

- **Recommended Loss**: **Binary Cross-Entropy with Logits** (`BCEWithLogitsLoss` / sigmoid cross-entropy).
- **Input Semantics**:
  - **Model Input**: Raw, unscaled **logits** $Z \in (-\infty, \infty)$ of shape `(2, 1)`. A separate sigmoid activation must **not** be applied prior to this loss to avoid applying sigmoid twice or causing numerical underflow/overflow.
  - **Target Semantics**: Continuous or discrete binary labels $y \in \{0, 1\}$ of matching shape `(2, 1)` and floating-point dtype (e.g., `float32` or `float64`).
  - **Reduction**: Explicitly reduced across the batch (default is batch `mean`, yielding a scalar loss: $\mathcal{L} = \frac{1}{2} \sum_{i=1}^2 \mathcal{L}_i$).
  - **Numerical Stability**: Formulated with the log-sum-exp stabilization:
    $$\mathcal{L}_i = \max(Z_i, 0) - Z_i \cdot y_i + \log\left(1 + e^{-|Z_i|}\right)$$

---

### 3. Gradient Check with Central Finite Differences

To verify the analytic gradient of a single scalar parameter (e.g., weight $W_{0,0}$ or scalar bias $b_0$, denoted $\theta_i$):

1. **Precision & Setup**:
   - Cast tensors to `float64` (double precision) to minimize catastrophic cancellation and floating-point rounding errors.
   - Choose step size $\epsilon \approx 10^{-7}$ (balancing truncation error $\mathcal{O}(\epsilon^2)$ with numerical floating-point noise $\mathcal{O}(\eta / \epsilon)$).
2. **Forward Probing**:
   - Evaluate loss with positive perturbation: $\mathcal{L}_+ = \mathcal{L}(\theta_i + \epsilon)$.
   - Evaluate loss with negative perturbation: $\mathcal{L}_- = \mathcal{L}(\theta_i - \epsilon)$.
   - Immediately restore the parameter to its original value: $\theta_i \leftarrow \theta_i$.
3. **Central Difference Approximation**:
   $$g_{\text{num}}(\theta_i) = \frac{\mathcal{L}(\theta_i + \epsilon) - \mathcal{L}(\theta_i - \epsilon)}{2\epsilon}$$
4. **Tolerance Verification**:
   - Compute analytic gradient $g_{\text{analytic}}(\theta_i)$ via backpropagation / autograd.
   - Compare via relative error:
     $$\text{rel\_err} = \frac{|g_{\text{num}} - g_{\text{analytic}}|}{\max(|g_{\text{num}}|, |g_{\text{analytic}}|, 10^{-8})}$$
   - Pass criteria: $\text{rel\_err} < 10^{-7}$ for `float64`.

---

### 4. GNCore Workflow IDs Used

- **`nn-tensor-contracts`**: Validated tensor axes, dimensions, and broadcasting safety between $X (2,3)$, $W (3,1)$, $b (1,)$, and targets `(2,1)`.
- **`nn-loss-semantics`**: Defined loss semantics (raw logits vs. probabilities, reduction mode, target formatting, avoiding double sigmoid).
- **`nn-gradient-check`**: Formulated the central finite difference procedure, $\epsilon$ tradeoff, parameter restoration step, and relative tolerance metrics.

---

### 5. Distinction: Proposed vs. Executed Checks

- **Checks Actually Executed**:
  - *Analytical & Structural Verification*: Hand-derived dimension contraction ($(2, 3) \times (3, 1) + (1,) = (2, 1)$), confirmed broadcast alignment with target shape `(2, 1)`, and formulated the exact mathematical equations for BCE with logits and central differences.
- **Proposed Checks (Not Executed)**:
  - *Numerical Runtime Gradient Check*: Numerical evaluation of $\mathcal{L}(\theta \pm \epsilon)$ and comparative assertions with autograd on a live Python runtime were **not executed** (deferred per the constraint: *pure reasoning only; no terminal commands, file edits, or network access*).
  - *Tiny-Batch Overfit / Training Probes*: Step execution and weight update probes on synthetic fixtures were **proposed only**.