---
name: cybersecurity
description: "Review application, dependency, cloud and agent security using concrete attack paths and scoped evidence."
license: MIT
---

# GNCore Cybersecurity

Version: 7.0.0rc1

## Choose the work

Establish assets, trust boundaries, authorization and attacker capabilities. Prioritize reachable risks and distinguish observed findings from generic hardening suggestions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Evidence-linked findings or a scoped security patch, abuse cases, severity rationale and practical mitigation/verification steps.

Reproduce safely in local or authorized targets. Check negative authorization cases, sensitive logging and dependency evidence. Do not claim absence of vulnerabilities from a scanner result alone.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

For each finding, trace attacker-controlled input through the relevant boundary to an observable impact, then propose a repair that preserves authorized behavior. Distinguish finding recall, false alarms and repair correctness. Path containment requires canonical component-aware checks and a symlink/race policy, not a string prefix or filename sanitizer alone. Retest the exploit path and safe neighboring cases; do not call an entire application secure from a small fixture.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Separate demonstrated exploits, statically established paths and unresolved hypotheses; record attacker control, impact, repair and safe neighboring behavior.
- Measure false alarms and repaired behavior separately from finding recall; secret removal does not revoke exposed credentials or derived sessions.

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
| `web-security` | Review web features for input, session, authorization, and output-handling vulnerabilities. |
| `privacy-review` | Reduce privacy risk by tracing personal data, purpose, access, retention, and user control. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
