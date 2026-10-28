---
name: security
description: "Review web security and privacy boundaries using concrete code paths, data flows, and source-backed requirements."
license: Apache-2.0 AND MIT
---

# GNCore Security

## Select the work from the user's intent

Map sensitive data, identity, access control, trust boundaries, and external exposure. Inspect relevant authentication, input, query, output, session, logging, retention, and consent behavior. Choose review depth based on the requested change and actual risk.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Reproduce relevant issues locally when practical, verify allowed and denied cases, and distinguish observed vulnerabilities or privacy gaps from hypothetical concerns.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `web-security` | Review web features for input, session, authorization, and output-handling vulnerabilities. |
| `privacy-review` | Reduce privacy risk by tracing personal data, purpose, access, retention, and user control. |

## Focused procedures

### Web Security Engineering (`web-security`)

Trace attacker-controlled values from entry to storage and rendering. Check authentication and object-level authorization on every sensitive operation, output encoding, CSRF protections where relevant, secret handling, and safe error responses. Tie findings to code paths and exploit conditions; do not claim a vulnerability without evidence.

### Privacy Review (`privacy-review`)

Map data collected, source, purpose, recipients, storage, access, retention, deletion, and user controls. Identify data minimization and security improvements. Flag jurisdiction-specific legal questions rather than asserting compliance. Do not expose raw personal data in logs, examples, or reports; use synthetic or redacted samples.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [firebase/agent-skills / firebase-security-rules-auditor](research/firebase-agent-skills-firebase-security-rules-auditor/GUIDE.md): Apache-2.0.
- [addyosmani/agent-skills / security-and-hardening](research/addyosmani-agent-skills-security-and-hardening/GUIDE.md): MIT.
- [samber/cc-skills-golang / golang-security](research/samber-cc-skills-golang-golang-security/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-compliance](research/microsoft-azure-skills-azure-compliance/GUIDE.md): MIT.
- [microsoft/azure-skills / entra-app-registration](research/microsoft-azure-skills-entra-app-registration/GUIDE.md): MIT.
- [supabase/agent-skills / supabase-postgres-best-practices](research/supabase-agent-skills-supabase-postgres-best-practices/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-enterprise-infra-planner](research/microsoft-azure-skills-azure-enterprise-infra-planner/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
