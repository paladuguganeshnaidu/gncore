---
name: computer-vision
description: "Build vision datasets, augmentation, detection/segmentation and image inference with task-appropriate evaluation."
license: MIT
---

# GNCore Computer Vision

Version: 7.0.0rc1

## Choose the work

Define channel order, value range, geometry and label semantics. Split related subjects/scenes together and verify every transform preserves boxes, masks or labels as appropriate.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Versioned dataset/transform contract, baseline model or inference pipeline, task metrics and representative visual error analysis.

Use synthetic images/boxes/masks to check geometry, empty annotations, corrupt input, batch shapes and train/serve preprocessing parity. Audit duplicate groups and subgroup failures.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Choose split groups from the deployment population: adjacent frames or multiple views of the same object cannot be independent test evidence. Transform images and annotations together, audit coordinate conventions and overlay representative boxes/masks after each geometric stage. Check dimensions, bounds, degenerate/empty labels and corrupt inputs. Keep a simple baseline, tune on validation only and report task-specific metrics and group counts on the untouched evaluation set.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `computer-vision` | Build vision workflows with robust image handling, leakage-safe splits, and task-appropriate evaluation. |
| `cv-dataset-audit` | Vision dataset integrity. |
| `cv-geometric-transforms` | Image and annotation transforms. |
| `cv-detection-metrics` | Detection and segmentation evaluation. |
| `cv-inference-parity` | Image inference parity. |

## Focused procedures

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

## Primary technical references

Use the documentation matching the installed framework. These are external reference links, not copied source or a promise that the framework is installed.

- [PyTorch autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)
- [scikit-learn leakage and preprocessing](https://scikit-learn.org/stable/common_pitfalls.html)

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
