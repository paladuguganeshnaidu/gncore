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

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Task flow, semantic tokens, component/state specifications or prototype with concrete content and accessibility behavior.

Walk through a complete task, error recovery, keyboard access, long labels and narrow layouts. Identify untested assumptions and unavailable participant or browser evidence.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Translate aesthetic intent into concrete task hierarchy and behavior. Specify the narrow-screen ordering, reflow, control names, keyboard path, visible and restored focus, persistent error/success feedback and destructive-action recovery. Infer consequential omissions from the primary journey without adding unrelated features. A proposed specification is not a tested interface: verify the implemented flow with keyboard, zoom and representative assistive technology when available.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Specify narrow-screen content/action order, semantic names, keyboard path, visible/restored focus and persistent linked errors; include consequential secret/destructive states when relevant.
- Announce async status without surprising focus moves; define focus after dialogs, removals and validation. Separate the proposed interaction specification from tested behavior.

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

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
