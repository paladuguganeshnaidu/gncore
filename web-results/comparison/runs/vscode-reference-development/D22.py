import math

def binary_loss_grad(logits, targets):
    if not isinstance(logits, list) or not isinstance(targets, list):
        raise ValueError("logits and targets must be lists")
    if not logits or len(logits) != len(targets):
        raise ValueError("lists must be nonempty and have equal lengths")

    losses = []
    gradients = []
    for z, y in zip(logits, targets):
        if isinstance(z, bool) or not isinstance(z, (int, float)) or not math.isfinite(z):
            raise ValueError("logits must be finite numbers")
        if isinstance(y, bool) or not isinstance(y, (int, float)) or y not in (0, 1):
            raise ValueError("targets must be 0 or 1")

        if z >= 0:
            exp_neg = math.exp(-z)
            sigmoid = 1.0 / (1.0 + exp_neg)
            loss = z - z * y + math.log1p(exp_neg)
        else:
            exp_pos = math.exp(z)
            sigmoid = exp_pos / (1.0 + exp_pos)
            loss = -z * y + math.log1p(exp_pos)

        losses.append(loss)
        gradients.append((sigmoid - y) / len(logits))

    return (sum(losses) / len(logits), gradients)