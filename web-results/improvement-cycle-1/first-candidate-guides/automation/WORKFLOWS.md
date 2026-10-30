# GNCore Automation: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Workflow Automation (`workflow-automation`)

Map triggers, inputs, side effects, failure modes and ownership before automating. Validate inputs, use least-privilege credentials, durable operation/payload identity and bounded idempotent retries. Preserve recoverable state and useful non-sensitive logs. Honor existing authorization; request review at an actual consequential boundary rather than repeatedly asking for already-authorized routine work. Test crash/replay on fixtures before claiming recovery or external execution.

### Resume after partial execution (`automation-resume`)

Record progress only after the operation's durable boundary and keep idempotency keys stable across retries. Inject failure after each meaningful side effect, resume against the same fixture and verify that no completed work is duplicated or silently skipped.
