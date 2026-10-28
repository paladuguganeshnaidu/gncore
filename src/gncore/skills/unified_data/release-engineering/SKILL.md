---
name: release-engineering
description: "Prepare a software release with consistent versions, tested artifacts, migration notes, and a reviewable delivery plan."
license: MIT
---

# GNCore Release Engineering

## Select the work from the user's intent

Inspect the release process, pending changes, package metadata, supported runtimes, CI, credentials requirements, and rollback path. Synchronize versions and release notes, build artifacts, and verify a clean installation. Use the user's chosen release scope and destination.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check the artifact contents, tests, metadata, migration compatibility, and remote state. Distinguish committed, pushed, tagged, uploaded, and publicly verified states.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `release-readiness` | Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates. |

## Focused procedures

### Release Readiness Review (`release-readiness`)

Inspect the release scope, version, changelog, artifacts, compatibility matrix, known issues, and rollback plan. Verify required checks and distinguish passed from skipped. Check migrations and external dependencies for rollout sequencing. Do not publish or deploy without authorization. End with a go/no-go recommendation tied to evidence and unresolved risks.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [magnus919/agent-skills / release-engineering](research/magnus919-agent-skills-release-engineering/GUIDE.md): MIT.
- [jorgerosal/wordpress-skills / wp-ci-cd-and-release-engineering](research/jorgerosal-wordpress-skills-wp-ci-cd-and-release-engineering/GUIDE.md): MIT.
- [samber/developer-relations-skills / engineering-blog-post](research/samber-developer-relations-skills-engineering-blog-post/GUIDE.md): MIT.
- [wondelai/skills / release-it](research/wondelai-skills-release-it/GUIDE.md): MIT.
- [callstackincubator/agent-skills / writing-user-docs](research/callstackincubator-agent-skills-writing-user-docs/GUIDE.md): MIT.
- [alirezarezvani/claude-skills / engineering-advanced-skills](research/alirezarezvani-claude-skills-engineering-advanced-skills/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
