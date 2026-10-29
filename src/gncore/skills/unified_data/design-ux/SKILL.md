---
name: design-ux
description: "Design developer-facing and product interfaces, flows, accessible interaction and reusable component systems."
license: MIT
---

# GNCore UX and Design Systems

Version: 7.0.0rc1

## Choose the work

Start from the user's task and existing design language. Choose research, flow, prototype or component specification only as needed; keep observed usability evidence separate from preference.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Task flow, semantic tokens, component/state specifications or prototype with concrete content and accessibility behavior.

Walk through a complete task, error recovery, keyboard access, long labels and narrow layouts. Identify untested assumptions and unavailable participant or browser evidence.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `ux-research` | Plan and synthesize ethical user research that ties observations to product decisions. |
| `design-system` | Extend a design system with accessible tokens and reusable components that fit existing conventions. |
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

### UX Research (`ux-research`)

Define the decision and research question before selecting a method. Recruit representative participants, use neutral prompts, obtain consent, and minimize personal data. Distinguish direct observation from interpretation; preserve contradictory evidence. Summarize themes with confidence and limitations, then map findings to testable design changes. Never invent participant quotes or counts.

### Design System Engineering (`design-system`)

Inspect existing tokens, components, naming, accessibility states, and consumers. Reuse established primitives; add the smallest composable API. Define default, hover, focus, disabled, error, and responsive behavior as relevant. Validate contrast and interaction semantics. Document migration or deprecation when a public component contract changes.

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

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
