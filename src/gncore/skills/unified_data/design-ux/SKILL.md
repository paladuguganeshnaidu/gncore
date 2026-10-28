---
name: design-ux
description: "Design and evaluate user flows, wireframes, visual systems, content, prototypes, accessibility, and handoffs."
license: Apache-2.0 AND MIT
---

# GNCore Design, UX, and Accessibility

## Select the work from the user's intent

Identify audience, task, content hierarchy, constraints, and the existing design language. Choose research synthesis, UX review, flow, wireframe, visual direction, component system, content, prototype, accessibility, or handoff work. Use explicit style preferences and infer a suitable direction when none is supplied.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Test representative tasks, hierarchy, readable content, keyboard operation, focus, responsive behavior, and relevant loading, empty, error, and success states.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `design-ux-audit` | Audit a user flow for task clarity, feedback, recovery, cognitive load, and accessibility. |
| `design-user-flow` | Map a user journey with entry points, decisions, states, errors, and successful completion. |
| `design-wireframe` | Specify a wireframe around user priorities, information hierarchy, and responsive states. |
| `design-minimal` | Create a restrained interface with clear hierarchy, intentional whitespace, and accessible controls. |
| `design-expressive` | Create a distinctive, layered interface without sacrificing navigation, readability, or accessibility. |
| `design-system-component` | Specify a reusable design-system component with API, states, semantics, and adoption guidance. |
| `design-content` | Write interface text that helps users understand choices, status, errors, and recovery. |
| `design-prototype` | Create a prototype test plan that resolves a specific interaction or comprehension question. |
| `design-accessibility` | Design keyboard, screen-reader, motion, contrast, and touch behavior into an interaction. |
| `design-handoff` | Prepare a design handoff with behavior, states, assets, responsive rules, and unresolved questions. |

## Focused procedures

### UX Usability Audit (`design-ux-audit`)

Perform the stated task using the current interface, record friction with steps and evidence, distinguish observation from inference, and rank fixes by task impact and confidence.

### User Flow Design (`design-user-flow`)

Identify user goal, preconditions, system responses, branches, recovery, and accessibility needs. Validate the flow against product constraints and test the highest-risk transition.

### Wireframe Specification (`design-wireframe`)

Define page purpose, content priority, primary action, supporting controls, loading/empty/error states, and breakpoints. Keep behavior and content clear before visual polish.

### Minimalist UI Direction (`design-minimal`)

Use a compact type/color system and strong alignment; retain status and essential actions, maintain contrast and visible focus, and remove ornament that does not help the task.

### Expressive UI Direction (`design-expressive`)

Choose a small set of expressive elements with clear hierarchy, test readable text and controls, preserve responsive behavior, and ensure each visual detail supports brand or content.

### Design System Component (`design-system-component`)

Inspect existing tokens and components, define component purpose and composition, document interaction and state behavior, check accessibility, and include migration or deprecation notes for changed contracts.

### UX Content Design (`design-content`)

Use the user's vocabulary, state the consequence before action, keep labels specific, explain errors with a next step, and verify length and localization constraints.

### Prototype Test Plan (`design-prototype`)

Define a single learning goal, representative participant criteria, realistic tasks, neutral prompts, observation rubric, and decision threshold. Avoid presenting a prototype preference as validated demand.

### Accessible Interaction Design (`design-accessibility`)

Specify semantic role, name, focus order, keyboard model, announcements, target size, contrast, and reduced-motion behavior. Validate with manual interaction in addition to automated scanning.

### Design to Engineering Handoff (`design-handoff`)

Annotate component reuse, tokens, breakpoints, interaction states, content, asset sources, and acceptance criteria. Review implementation with the designer and log deviations for resolution.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [leonxlnx/taste-skill / high-end-visual-design](research/leonxlnx-taste-skill-high-end-visual-design/GUIDE.md): MIT.
- [nextlevelbuilder/ui-ux-pro-max-skill / ui-ux-pro-max](research/nextlevelbuilder-ui-ux-pro-max-skill-ui-ux-pro-max/GUIDE.md): MIT.
- [pbakaus/impeccable / impeccable](research/pbakaus-impeccable-impeccable/GUIDE.md): Apache-2.0.
- [github/awesome-copilot / penpot-uiux-design](research/github-awesome-copilot-penpot-uiux-design/GUIDE.md): MIT.
- [bencium/bencium-marketplace / bencium-innovative-ux-designer](research/bencium-bencium-marketplace-bencium-innovative-ux-designer/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
