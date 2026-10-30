# GNCore Deep Learning: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

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
