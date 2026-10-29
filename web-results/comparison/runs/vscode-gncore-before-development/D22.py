import math

def binary_loss_grad(logits, targets):
    if not isinstance(logits, list) or not isinstance(targets, list):
        raise ValueError("logits and targets must be lists")
    if not logits or len(logits) != len(targets):
        raise ValueError("logits and targets must be nonempty and equal length")
    for logit in logits:
        if isinstance(logit, bool) or not isinstance(logit, (int, float)) or not math.isfinite(logit):
            raise ValueError("logits must be finite numbers")
    for target in targets:
        if isinstance(target, bool) or target not in (0, 1):
            raise ValueError("targets must be 0 or 1")
    loss = 0.0
    gradients = []
    count = len(logits)
    for logit, target in zip(logits, targets):
        loss += max(0.0, logit) - logit * target + math.log1p(math.exp(-abs(logit)))
        if logit >= 0:
            probability = 1.0 / (1.0 + math.exp(-logit))
        else:
            exponential = math.exp(logit)
            probability = exponential / (1.0 + exponential)
        gradients.append((probability - target) / count)
    return loss / count, gradients