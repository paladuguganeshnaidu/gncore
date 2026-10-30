# GNCore NLP and Language Pipelines: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Natural Language Processing (`nlp`)

Inspect languages, tokenization, labels, privacy constraints, and intended use. Establish a simple baseline and split by user/document when duplicates could leak. Evaluate per-class and per-language behavior, not only one aggregate metric. Minimize retention of raw text and redact sensitive examples. Treat generated labels as noisy; document model and data provenance. Do not claim factuality or safety from benchmark scores alone.

### Token and label alignment (`nlp-token-alignment`)

Preserve original text and tokenizer offsets. Define labels for special tokens and subwords, mask ignored positions from loss/metrics and test Unicode plus truncation boundaries. Inspect a hand-labeled example end to end instead of assuming token counts align.

### Text classification baseline (`nlp-text-classification`)

Split related documents/users before fitting vocabulary or learning preprocessing. Establish a simple lexical baseline, inspect label imbalance and tune thresholds on validation data. Report per-class support/errors and test empty, long and out-of-language input.

### Sequence masks and generation (`nlp-sequence-modeling`)

Specify padding side, attention masks, causal visibility, target shifting and stop tokens. Check a short hand-computed sequence for future-token leakage and ignored padding. Bound generation length and verify batch versus single-input behavior.

### Language and task evaluation (`nlp-evaluation`)

Choose metrics that correspond to classification, retrieval, extraction or generation, and retain dataset/language provenance. Examine errors by language/length and independent source groups. Separate semantic accuracy from surface similarity and reviewer preference.
