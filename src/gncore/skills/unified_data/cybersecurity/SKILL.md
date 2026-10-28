---
name: cybersecurity
description: "Assess threats, code risks, vulnerabilities, incidents, identity, cloud controls, and security validation plans."
license: Apache-2.0 AND MIT
---

# GNCore Cybersecurity

## Select the work from the user's intent

Define assets, trust boundaries, adversary capabilities, exposure, and authorized scope. Use threat modeling, secure-code review, triage, incident response, identity, cloud review, controls, phishing analysis, secret response, or validation planning as the situation requires.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Tie each finding to a reachable path, evidence, impact, and mitigation. Distinguish a scoped test from a claim that the entire system is secure.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cyber-threat-model` | Map assets, trust boundaries, threats, controls, and residual risk for a bounded system. |
| `cyber-secure-code` | Review a code change for exploitable input, identity, authorization, secret, and data-flow flaws. |
| `cyber-vulnerability-triage` | Prioritize a reported vulnerability using affected assets, exploitability, exposure, and impact evidence. |
| `cyber-incident-response` | Coordinate defensive incident response with containment, evidence preservation, and recovery gates. |
| `cyber-identity-access` | Review identities and permissions for least privilege, lifecycle, ownership, and audit evidence. |
| `cyber-cloud-review` | Assess cloud configuration against an explicit threat model and approved security baseline. |
| `cyber-security-controls` | Map supplied evidence to security control requirements with traceable, bounded conclusions. |
| `cyber-phishing` | Triage a suspected phishing report and provide safe containment and user guidance. |
| `cyber-secret-response` | Respond to a potentially exposed credential without echoing or spreading the secret. |
| `cyber-security-test-plan` | Define a bounded security test plan with written authorization, targets, limits, and stop conditions. |

## Focused procedures

### Threat Model (`cyber-threat-model`)

Use an explicit scope and attacker model, diagram data flows and entry points, rank plausible threats, tie mitigations to owners, and record residual risk. Do not probe systems outside authorized scope.

### Secure Code Review (`cyber-secure-code`)

Trace attacker-controlled inputs to sensitive operations, verify server-side authorization and safe encoding, identify reproducible findings, and recommend minimal fixes with regression tests. Avoid unapproved live exploitation.

### Vulnerability Triage (`cyber-vulnerability-triage`)

Verify affected versions and reachable paths, validate evidence in a safe environment, assess exposure and compensating controls, assign severity using policy, and coordinate fix/mitigation and retest.

### Cyber Incident Response (`cyber-incident-response`)

Establish scope and confidence, preserve logs and chain of custody, select reversible containment with owner approval, coordinate communications, eradicate safely, and verify recovery. Keep hypotheses separate from confirmed facts.

### Identity and Access Review (`cyber-identity-access`)

Inventory human and service identities, roles, privilege, owner, last use, and authentication controls. Validate exceptions and break-glass paths; recommend revocation only through authorized change control.

### Cloud Security Review (`cyber-cloud-review`)

Check identity boundaries, public exposure, encryption, network paths, logging, backups, and configuration drift. Cite exact resources and evidence; do not change production settings without authorization.

### Security Control Evidence (`cyber-security-controls`)

Use the named control version, identify evidence period and system scope, note sample and gaps, and distinguish designed from operating effectiveness. Do not claim certification or compliance from incomplete evidence.

### Phishing Response Triage (`cyber-phishing`)

Preserve message headers and indicators, verify links without opening them, identify affected users and credential exposure, and route containment through authorized tooling. Do not forward malicious content broadly.

### Exposed Secret Response (`cyber-secret-response`)

Identify credential type and exposure window without printing its value, notify the owner, revoke or rotate using approved procedure, audit use, and remove exposure from accessible history where possible.

### Authorized Security Test Plan (`cyber-security-test-plan`)

Record asset owner approval, exact scope, allowed techniques, dates, rate limits, data handling, contacts, and stop rules. Keep testing non-destructive and report only verified findings to authorized recipients.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [sickn33/agentic-awesome-skills / security-auditor](research/sickn33-agentic-awesome-skills-security-auditor/GUIDE.md): MIT.
- [mindrally/skills / python-cybersecurity-tool-development](research/mindrally-skills-python-cybersecurity-tool-development/GUIDE.md): Apache-2.0.
- [microsoft/azure-skills / azure-kusto-irql](research/microsoft-azure-skills-azure-kusto-irql/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
