import math

def categorical_loss_grad(logits, labels):
    if not isinstance(logits, list) or len(logits) == 0:
        raise ValueError("logits must be a nonempty list")
    if not isinstance(labels, list) or len(labels) != len(logits):
        raise ValueError("labels must be a list matching logits length")
    
    n_samples = len(logits)
    if not isinstance(logits[0], list):
        raise ValueError("logits elements must be lists")
    n_classes = len(logits[0])
    if n_classes < 2:
        raise ValueError("logits must have at least 2 classes")
    
    for row in logits:
        if not isinstance(row, list) or len(row) != n_classes:
            raise ValueError("logits must be rectangular")
        for val in row:
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise ValueError("logits elements must be numbers, not bool")
            if not math.isfinite(val):
                raise ValueError("logits elements must be finite")
    
    for y in labels:
        if isinstance(y, bool) or not isinstance(y, int):
            raise ValueError("labels elements must be integers, not bool")
        if y < 0 or y >= n_classes:
            raise ValueError("label index out of range")
            
    total_loss = 0.0
    grad = []
    for i in range(n_samples):
        row = logits[i]
        target = labels[i]
        max_val = max(row)
        exp_vals = [math.exp(v - max_val) for v in row]
        sum_exp = sum(exp_vals)
        probs = [ev / sum_exp for ev in exp_vals]
        
        sample_loss = math.log(sum_exp) + max_val - row[target]
        total_loss += sample_loss
        
        sample_grad = [(p - (1.0 if j == target else 0.0)) / n_samples for j, p in enumerate(probs)]
        grad.append(sample_grad)
        
    mean_loss = total_loss / n_samples
    return mean_loss, grad