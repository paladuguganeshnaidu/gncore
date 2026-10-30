# GNCore Computer Vision: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Computer Vision (`computer-vision`)

Inspect image formats, dimensions, labels, duplicate/near-duplicate groups, and provenance. Split by source, person, or scene where needed to prevent leakage. Normalize consistently and validate augmentations preserve labels. Use task-appropriate metrics and inspect representative errors. Protect biometric and personal imagery; do not download, retain, or expose images without authorization.

### Vision dataset integrity (`cv-dataset-audit`)

Inventory image encodings, shapes, corrupt files, annotation bounds and duplicate/subject groups. Split by the group that must generalize, then report per-split counts and excluded records without exposing private imagery.

### Image and annotation transforms (`cv-geometric-transforms`)

Apply resize/crop/flip consistently to images, boxes, masks and keypoints. Specify coordinate conventions and interpolation separately for images versus categorical masks. Use a synthetic checkerboard and known box to verify exact transformed bounds and clipping.

### Detection and segmentation evaluation (`cv-detection-metrics`)

State IoU thresholds, class matching and aggregation before evaluating. Handle empty predictions/annotations explicitly, retain per-class support, and inspect failure examples. Keep confidence-threshold tuning separate from final holdout reporting.

### Image inference parity (`cv-inference-parity`)

Record decoding, orientation, channel order, scaling and normalization with the artifact. Compare a known image through training-validation preprocessing and the serving path. Reject unsupported/corrupt input and bound decoded dimensions and batch memory.
