---
name: presentations-powerpoint
description: "Create and refine presentations with a clear storyline, visual hierarchy, accurate charts, and verified layouts."
license: Apache-2.0 AND MIT
---

# GNCore Presentations and PowerPoint

## Select the work from the user's intent

Identify audience, decision, delivery context, source evidence, and template. Build a narrative before decorating slides. Select executive briefing, data story, visual design, editing, speaker notes, accessibility, templating, or deck QA work; keep one clear message per slide when practical.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Render every slide and inspect overflow, contrast, typography, cropping, chart labels, numerical accuracy, speaker notes, and template consistency.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `ppt-storyline` | Turn an audience, decision, and evidence set into a coherent presentation narrative. |
| `ppt-create` | Create a presentation deck from a brief and source material with a clear storyline and consistent design. |
| `ppt-executive` | Prepare an executive deck that leads with decisions, implications, risks, and evidence. |
| `ppt-data-story` | Explain data in slides with faithful charts, denominators, uncertainty, and a decision-relevant takeaway. |
| `ppt-visual-design` | Improve slide hierarchy, typography, color, alignment, and visual consistency without weakening content. |
| `ppt-edit` | Revise an existing deck while preserving intended content, theme, and editable structure. |
| `ppt-speaker-notes` | Write speaker notes that support a timed presentation without duplicating slide text. |
| `ppt-accessibility` | Review a presentation for reading order, contrast, meaningful text, captions, and accessible charts. |
| `ppt-template` | Create a reusable PowerPoint template with reliable masters, layouts, typography, and color tokens. |
| `ppt-deck-qa` | Run a final slide-by-slide quality pass on a saved presentation and its exported PDF. |

## Focused procedures

### Presentation Storyline (`ppt-storyline`)

Define audience, purpose, one takeaway, decision requested, and time limit. Order claims as a logical story, support each with evidence, and remove slides that do not advance the outcome.

### Create a PowerPoint Deck (`ppt-create`)

Build a slide outline before authoring, use a consistent theme and native editable elements, cite claims, and keep one main point per slide. Export/render every slide and fix overflow, clipping, and weak contrast.

### Executive Presentation (`ppt-executive`)

Put the recommendation and decision needed early, show the few metrics that support it with context, include alternatives and risks, and close with owners and next gates.

### Data Story Presentation (`ppt-data-story`)

Verify chart values against source data, label units and periods, use honest scales, expose uncertainty and exclusions, and narrate association versus causation accurately.

### Presentation Visual Design (`ppt-visual-design`)

Use the supplied brand system, align repeated elements, maintain readable type and contrast, avoid decorative clutter, and inspect slides at presentation size and on a rendered overview.

### Edit an Existing PPTX (`ppt-edit`)

Inspect slide masters, layouts, notes, charts, and embedded media before editing. Make scoped changes, preserve source, render the whole deck, and compare changed and neighboring slides for layout regressions.

### Speaker Notes and Talk Track (`ppt-speaker-notes`)

Estimate speaking time, explain transitions and evidence, mark pauses or demos, and keep notes consistent with slide claims. Check the talk track against the actual exported deck.

### Accessible Presentation (`ppt-accessibility`)

Use logical reading order, descriptive titles and alt text, sufficient contrast, accessible chart labels, and captions for essential audio/video. Validate using built-in checking and manual slide review.

### PowerPoint Template Design (`ppt-template`)

Define purpose-specific layouts and theme tokens, test short and long titles, charts and images, check placeholders and footers, and create a sample deck to verify editability and rendering.

### PowerPoint Deck QA (`ppt-deck-qa`)

Check slide order, duplicated or missing content, citations, spelling, notes, links, image quality, embedded media, dimensions, and rendering. Open both final artifacts and report defects by slide number.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [firecrawl/anydoc / convert-documents-to-markdown](research/firecrawl-anydoc-convert-documents-to-markdown/GUIDE.md): MIT.
- [anthropics/financial-services / pptx-author](research/anthropics-financial-services-pptx-author/GUIDE.md): Apache-2.0.
- [minimax-ai/skills / pptx-generator](research/minimax-ai-skills-pptx-generator/GUIDE.md): MIT.
- [anthropics/financial-services / ppt-template-creator](research/anthropics-financial-services-ppt-template-creator/GUIDE.md): Apache-2.0.
- [anthropics/financial-services / funding-digest](research/anthropics-financial-services-funding-digest/GUIDE.md): Apache-2.0.
- [yuan1z0825/nature-skills / nature-image2ppt](research/yuan1z0825-nature-skills-nature-image2ppt/GUIDE.md): MIT.
- [bytedance/deer-flow / ppt-generation](research/bytedance-deer-flow-ppt-generation/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
