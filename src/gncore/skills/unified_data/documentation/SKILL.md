---
name: documentation
description: "Write and maintain technical and API documentation from verified behavior, examples, and audience needs."
license: Apache-2.0 AND MIT
---

# GNCore Documentation

## Select the work from the user's intent

Identify reader, task, source of truth, supported versions, and the action the documentation should enable. Trace examples to actual APIs and command behavior. Use a clear progression from purpose and setup to a working example, constraints, and troubleshooting.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Run examples where practical, validate links and symbols, check argument and response shapes, and distinguish documented guarantees from implementation details.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `technical-writing` | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. |
| `documentation-api` | Document API behavior from the implementation and contract, with examples users can reproduce. |

## Focused procedures

### Technical Writing (`technical-writing`)

Inspect the actual behavior and audience before drafting. Put the shortest successful path first, identify prerequisites and supported versions, and verify commands and output. Keep terminology consistent and label assumptions. Do not document unimplemented behavior or expose credentials. Update nearby references when a public command or interface changes.

### API Documentation (`documentation-api`)

Inspect routes, schemas, authentication, error behavior, and versioning. Document required and optional fields, examples, pagination, rate limits, and known constraints. Verify examples against a safe environment or schema. Keep secrets and personal data out. Clearly flag undocumented behavior instead of guessing.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [cloudflare/skills / cloudflare](research/cloudflare-skills-cloudflare/GUIDE.md): Apache-2.0.
- [scrapegraphai/just-scrape / just-scrape](research/scrapegraphai-just-scrape-just-scrape/GUIDE.md): MIT.
- [mastra-ai/skills / mastra](research/mastra-ai-skills-mastra/GUIDE.md): Apache-2.0.
- [addyosmani/agent-skills / documentation-and-adrs](research/addyosmani-agent-skills-documentation-and-adrs/GUIDE.md): MIT.
- [samber/cc-skills-golang / golang-documentation](research/samber-cc-skills-golang-golang-documentation/GUIDE.md): MIT.
- [github/awesome-copilot / documentation-writer](research/github-awesome-copilot-documentation-writer/GUIDE.md): MIT.
- [vercel/components.build / building-components](research/vercel-components.build-building-components/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
