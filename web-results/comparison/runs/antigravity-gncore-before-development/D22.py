import math

def binary_loss_grad(logits, targets):
    if not isinstance(logits, list) or not isinstance(targets, list):
        raise ValueError("logits and targets must be lists")
    n = len(logits)
    if n == 0 or len(targets) != n:
        raise ValueError("logits and targets must be non-empty lists of equal length")
    
    losses = []
    grads = []
    for z, y in zip(logits, targets):
        if isinstance(z, bool) or not isinstance(z, (int, float)) or math.isnan(z) or math.isinf(z):
            raise ValueError("logits must be finite numeric values")
        if isinstance(y, bool) or (y != 0 and y != 1):
            raise ValueError("targets must be integers 0 or 1")
        
        # Numerically stable BCE with logits
        loss_i = max(z, 0.0) - y * z + math.log1p(math.exp(-abs(z)))
        losses.append(loss_i)
        
        # Numerically stable sigmoid
        if z >= 0.0:
            sig_z = 1.0 / (1.0 + math.exp(-z))
        else:
            ez = math.exp(z)
            sig_z = ez / (1.0 + ez)
        grads.append((sig_z - y) / n)
        
    mean_loss = sum(losses) / n
    return (mean_loss, grads)
