import math

def binary_loss_grad(logits, targets):
    if type(logits) is not list or type(targets) is not list:
        raise ValueError("logits and targets must be lists")
    n = len(logits)
    if n == 0 or len(targets) != n:
        raise ValueError("logits and targets must be equal non-empty length")
    
    losses = []
    grads = []
    for z, y in zip(logits, targets):
        if type(z) is bool or not isinstance(z, (int, float)) or not math.isfinite(z):
            raise ValueError("each logit must be a finite numeric value")
        if type(y) is bool or y not in (0, 1):
            raise ValueError("each target must be 0 or 1")
        
        # Numerically stable BCE with logits
        loss_i = max(z, 0.0) - y * z + math.log1p(math.exp(-abs(z)))
        losses.append(loss_i)
        
        # Numerically stable sigmoid
        if z >= 0:
            sig = 1.0 / (1.0 + math.exp(-z))
        else:
            ez = math.exp(z)
            sig = ez / (1.0 + ez)
        
        grads.append((sig - y) / n)
        
    mean_loss = sum(losses) / n
    return (mean_loss, grads)
