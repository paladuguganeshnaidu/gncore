# GNCore Cybersecurity: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

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
