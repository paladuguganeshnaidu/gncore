---
name: word-documents
description: "Create, edit, format, review, and prepare accessible Word documents, reports, templates, forms, and redlines."
license: Apache-2.0 AND MIT
---

# GNCore Microsoft Word and DOCX Documents

## Select the work from the user's intent

Inspect the source document, audience, required structure, template, tracked changes, and intended output format. Preserve styles, numbering, fields, tables, headers, footers, and existing revisions when editing. Use structural styles and real document objects rather than visual spacing tricks.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Render the document and inspect pagination, table splits, headings, images, links, and accessibility structure. Reopen the delivered file and report conversion or rendering limitations.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `word-draft` | Create a structured Word document from a brief, source material, and intended audience. |
| `word-edit` | Edit an existing Word document for clarity and structure while preserving required content. |
| `word-format` | Repair Word styles, spacing, headers, pagination, tables, and section layout. |
| `word-redline` | Prepare or review DOCX edits with traceable changes and comments for human approval. |
| `word-accessibility` | Improve DOCX structure and accessibility for navigation, screen readers, and document reuse. |
| `word-template` | Create a reusable Word template with stable styles, fields, sections, and usage rules. |
| `word-report` | Produce a sourced report in Word with executive summary, evidence, findings, and appendices. |
| `word-merge` | Combine supplied DOCX materials into one coherent document without losing provenance or structure. |
| `word-forms` | Design a fillable Word form with clear labels, logical completion order, and safe review. |
| `word-review` | Proofread a final DOCX for content consistency, references, fields, and page-level layout. |

## Focused procedures

### Draft a Word Document (`word-draft`)

Confirm purpose, audience, length, source facts, and required sections. Use semantic heading styles, consistent lists and tables, and clear citations; verify the saved DOCX reopens and its rendered pages are readable.

### Edit and Restructure DOCX (`word-edit`)

Inspect the full document and styles, preserve factual meaning and required clauses, make scoped edits, then reopen and compare the resulting document for missing text, broken structure, and layout regressions.

### Word Formatting Repair (`word-format`)

Inspect styles and section breaks before direct formatting, apply consistent styles, check headers/footers and page numbering, render every page, and fix overflow or awkward page breaks.

### Word Tracked Changes Review (`word-redline`)

Preserve the source, use tracked changes when available, anchor comments to exact text, distinguish proposed language from accepted language, and verify revisions/comments remain visible after reopening.

### Accessible Word Document (`word-accessibility`)

Use heading styles, meaningful link text, table headers, alt text for informative visuals, sufficient contrast, and logical reading order. Check accessibility tools and render the document to confirm layout.

### Word Template Design (`word-template`)

Separate editable content from fixed layout, define named styles and reusable blocks, test long/short content and page breaks, and confirm the template opens cleanly in supported Word-compatible tools.

### Word Report Production (`word-report`)

Trace each material claim to a source, separate facts from judgment, maintain cross-references and captions, update table of contents and fields, and inspect rendered pages and links.

### Word Document Merge (`word-merge`)

Inventory sources and versions, resolve intended order, normalize styles carefully, retain citations and attribution, inspect tables/images/headers after merge, and verify no source section was omitted.

### Word Form Design (`word-forms`)

Define respondent and data purpose, use accessible controls and instructions, mark required fields, protect only intended regions, and test completion, save, and print behavior.

### Word Final Proof and QA (`word-review`)

Check spelling, terminology, dates, names, numbering, links, citations, headers/footers, and document metadata; reopen and render the final saved file and resolve each detected defect.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [claude-office-skills/skills / docx-manipulation](research/claude-office-skills-skills-docx-manipulation/GUIDE.md): MIT.
- [nexu-io/open-design / docx](research/nexu-io-open-design-docx/GUIDE.md): Apache-2.0.
- [claude-office-skills/skills / pdf-to-docx](research/claude-office-skills-skills-pdf-to-docx/GUIDE.md): MIT.
- [minimax-ai/skills / minimax-docx](research/minimax-ai-skills-minimax-docx/GUIDE.md): MIT.
- [nexu-io/open-design / minimax-docx](research/nexu-io-open-design-minimax-docx/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
