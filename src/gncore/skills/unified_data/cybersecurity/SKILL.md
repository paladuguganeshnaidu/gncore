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

## Deliver and verify

Evidence-linked findings or a scoped security patch, abuse cases, severity rationale and practical mitigation/verification steps.

Reproduce safely in local or authorized targets. Check negative authorization cases, sensitive logging and dependency evidence. Do not claim absence of vulnerabilities from a scanner result alone.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

For each finding, trace attacker-controlled input through the relevant boundary to an observable impact, then propose a repair that preserves authorized behavior. Distinguish finding recall, false alarms and repair correctness. Path containment requires canonical component-aware checks and a symlink/race policy, not a string prefix or filename sanitizer alone. Retest the exploit path and safe neighboring cases; do not call an entire application secure from a small fixture.

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

### Web Security Engineering (`web-security`)

Trace attacker-controlled values from entry to storage and rendering. Check authentication and object-level authorization on every sensitive operation, output encoding, CSRF protections where relevant, secret handling, and safe error responses. Tie findings to code paths and exploit conditions; do not claim a vulnerability without evidence.

### Privacy Review (`privacy-review`)

Map data collected, source, purpose, recipients, storage, access, retention, deletion, and user controls. Identify data minimization and security improvements. Flag jurisdiction-specific legal questions rather than asserting compliance. Do not expose raw personal data in logs, examples, or reports; use synthetic or redacted samples.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
