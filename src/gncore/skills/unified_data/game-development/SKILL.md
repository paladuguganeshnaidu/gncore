---
name: game-development
description: "Build and improve game mechanics, interactions, state, assets, and performance in the existing engine."
license: Apache-2.0 AND MIT
---

# GNCore Game Development

## Select the work from the user's intent

Inspect the engine, platform, input model, scene or entity structure, asset pipeline, and target player experience. Implement a small complete gameplay loop, define state transitions and reset behavior, and keep frame work separate from slower loading or UI operations.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Play the main loop and test input, pause/resume, win/loss, restart, edge collisions, resource cleanup, and target-device performance. Do not claim playtesting without running it.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `game-development` | Implement game features with deterministic state transitions, responsive input, and measurable performance. |

## Focused procedures

### Game Development (`game-development`)

Inspect engine version, scene/entity patterns, update loop, save format, and target platforms. Keep game state transitions explicit and input responsive; handle pause, restart, and persistence as applicable. Profile before optimizing and validate on target hardware when possible. Avoid changing unrelated gameplay balance or publishing builds without authorization.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [wshobson/agents / unity-ecs-patterns](research/wshobson-agents-unity-ecs-patterns/GUIDE.md): MIT.
- [gamedev-skills/awesome-gamedev-agent-skills / router](research/gamedev-skills-awesome-gamedev-agent-skills-router/GUIDE.md): Apache-2.0.
- [jeffallan/claude-skills / game-developer](research/jeffallan-claude-skills-game-developer/GUIDE.md): MIT.
- [mindrally/skills / game-development](research/mindrally-skills-game-development/GUIDE.md): Apache-2.0.
- [dylantarre/animation-principles / game-development](research/dylantarre-animation-principles-game-development/GUIDE.md): MIT.
- [miles990/claude-software-skills / game-development](research/miles990-claude-software-skills-game-development/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
