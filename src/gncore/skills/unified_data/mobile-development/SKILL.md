---
name: mobile-development
description: "Build mobile application flows with platform-appropriate navigation, state, permissions, accessibility, and lifecycle handling."
license: Apache-2.0 AND MIT
---

# GNCore Mobile Development

## Select the work from the user's intent

Inspect the target platform, framework, navigation patterns, data flow, and device constraints. Choose native conventions where they improve familiarity. Handle offline or unreliable networking, permission denial, background/foreground transitions, keyboard insets, and touch interaction.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify the key flow at relevant device sizes, accessibility settings, lifecycle states, and error cases. Report simulator, device, and platform checks separately.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `mobile-app` | Implement mobile features with reliable navigation, offline behavior, accessibility, and platform conventions. |

## Focused procedures

### Mobile App Engineering (`mobile-app`)

Identify the framework, supported OS versions, navigation, persistence, and permission model first. Follow existing platform conventions and handle loading, empty, error, offline, and denied-permission states. Keep secrets out of the client, minimize collected data, and test small/large screens and accessibility settings. Avoid platform migrations or store submissions unless requested.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [sickn33/agentic-awesome-skills / frontend-mobile-development-component-scaffold](research/sickn33-agentic-awesome-skills-frontend-mobile-development-component-scaffold/GUIDE.md): MIT.
- [rohitg00/awesome-claude-code-toolkit / mobile-development](research/rohitg00-awesome-claude-code-toolkit-mobile-development/GUIDE.md): Apache-2.0.
- [jame581/godotprompter / mobile-development](research/jame581-godotprompter-mobile-development/GUIDE.md): MIT.
- [mattpocock/skills / tdd](research/mattpocock-skills-tdd/GUIDE.md): MIT.
- [wshobson/agents / react-native-design](research/wshobson-agents-react-native-design/GUIDE.md): MIT.
- [solana-mobile/solana-mobile-skills / solana-mobile](research/solana-mobile-solana-mobile-skills-solana-mobile/GUIDE.md): Apache-2.0.
- [tencentcloudbase/cloudbase-skills / cloudbase](research/tencentcloudbase-cloudbase-skills-cloudbase/GUIDE.md): MIT.
- [heroui-inc/heroui / heroui-native](research/heroui-inc-heroui-heroui-native/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
