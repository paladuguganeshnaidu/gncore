---
name: pdf-documents
description: "Extract, create, combine, split, OCR, fill, review, and verify PDF documents and redactions."
license: Apache-2.0 AND MIT
---

# GNCore PDF Documents

## Select the work from the user's intent

Determine whether the PDF is text-based, scanned, tagged, form-based, or signed. Preserve originals and choose extraction, OCR, generation, merge/split, form, accessibility, review, or redaction work. Keep page coordinates, reading order, and signature effects explicit.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Render affected pages and inspect layout. Check extracted text, form values, links, and searchability. For redaction, verify underlying text and objects are removed rather than merely covered.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `pdf-extract` | Extract text or tables from a supplied PDF while preserving page references and uncertainty. |
| `pdf-create` | Create a clean PDF from approved source content and verify its page layout and metadata. |
| `pdf-accessibility` | Review or improve PDF tags, reading order, headings, links, tables, and alternative text. |
| `pdf-merge` | Combine approved PDFs in a defined order while preserving page integrity and source provenance. |
| `pdf-split` | Split a PDF into named outputs using explicit page ranges or verified section boundaries. |
| `pdf-form` | Inspect or create a fillable PDF form with labeled fields and reliable save behavior. |
| `pdf-ocr` | Make a scanned PDF searchable with OCR and verify text against original page images. |
| `pdf-redaction` | Apply and verify permanent redaction to specifically authorized PDF content. |
| `pdf-review` | Review PDF content, links, references, page numbering, and rendered layout before delivery. |
| `pdf-signature` | Prepare a PDF for an authorized signature workflow and verify fields and final artifact integrity. |

## Focused procedures

### PDF Text and Table Extraction (`pdf-extract`)

Inspect whether the PDF is text-based or scanned, extract with page numbers and table structure, OCR only when needed, compare samples visually, and flag ambiguous characters instead of guessing.

### Create a PDF Deliverable (`pdf-create`)

Preserve source meaning, embed suitable fonts, set page size and margins, verify links and selectable text, render every page, and inspect clipping, blank pages, and reading order.

### Accessible PDF Review (`pdf-accessibility`)

Check document language, title, tags, heading hierarchy, logical order, table headers, link names, and image descriptions. Run available accessibility checks and manually inspect the reading sequence.

### Merge PDFs (`pdf-merge`)

Inventory files and page counts, confirm order and rotation, preserve bookmarks where possible, create a new output without overwriting sources, then render and compare all page boundaries.

### Split PDF by Page or Section (`pdf-split`)

Confirm page numbering convention, validate range boundaries, preserve source file, use descriptive output names, and verify resulting page counts and first/last page content.

### PDF Form Workflow (`pdf-form`)

Map each field to purpose and data type, add labels and tab order, test keyboard entry and saving, verify printed output, and protect personal information in test fixtures.

### Scanned PDF OCR (`pdf-ocr`)

Detect scan quality, orientation, language, and page bounds; OCR to a searchable layer without replacing the original image; sample-check names, numbers, columns, and every critical field.

### PDF Redaction Review (`pdf-redaction`)

Confirm exact target and authorization, use true redaction rather than visual overlays, remove hidden text and metadata where required, save a new copy, and inspect extraction and rendered pages for residual content.

### PDF Content and Layout Review (`pdf-review`)

Check every page for clipping, missing glyphs, blank pages, inconsistent numbering, broken links, and cross-reference errors. Compare critical facts to the source document.

### PDF Signature Workflow Support (`pdf-signature`)

Identify required signer sequence and field locations from supplied instructions, preserve document content, check certificate or platform requirements, and do not sign or attest on anyone's behalf.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [anthropics/skills / canvas-design](research/anthropics-skills-canvas-design/GUIDE.md): Apache-2.0.
- [coreyhaines31/marketingskills / lead-magnets](research/coreyhaines31-marketingskills-lead-magnets/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
