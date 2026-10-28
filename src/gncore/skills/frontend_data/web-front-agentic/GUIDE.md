---
name: web-front-agentic
description: "Design AI task interfaces that expose progress, editable intent, results, and recovery controls."
---

# GNCore Agentic

Make the task goal, inputs, running state, and result visible. Separate proposals from completed actions, show meaningful progress and recoverable errors, and provide cancel or edit controls where supported. Avoid implying actions succeeded without tool evidence.

## Working agreement

Implement the user's requested artifact in the existing stack and design system. For a style request, apply this direction without combining every installed style. Check narrow and wide layouts, keyboard interaction, content overflow, and relevant loading or error states. Use reduced-motion alternatives for motion. Report actual checks and unresolved limitations.

## Implementation references

Read [UPSTREAM.md](UPSTREAM.md) for the relevant detailed workflow, then load only the references needed for this task. Its relative resource paths resolve from this installed skill folder. Replace historical `.claude/skills/<original-name>` prefixes in example commands with the absolute path to this folder. References to other upstream skills are optional material; verify availability before using them.

The GNCore scope above governs adaptation choices: preserve the user's stack, brand, deliverable, and selected tools. Upstream example palettes and library defaults are starting points.

See [SOURCE.md](SOURCE.md) for provenance and retained license notices.
