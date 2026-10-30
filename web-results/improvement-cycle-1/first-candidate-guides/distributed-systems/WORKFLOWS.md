# GNCore Distributed Systems: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Idempotent operations (`dist-idempotency`)

Define the operation identity, key scope, retention and same-key/different-payload behavior. Persist result and side effect within the consistency boundary, and replay after simulated timeout/crash. Do not implement exactly-once claims with an in-memory duplicate set.

### Queue delivery and recovery (`dist-queues`)

State ordering, delivery guarantees, acknowledgment point and poison-message policy. Test duplicate/redelivered messages and a crash between side effect and acknowledgment. Bound retries and dead-letter handling without silently dropping work.

### Consistency and stale writers (`dist-consistency`)

Identify which reads/writes require linearizable, transactional or eventual behavior. Define version/fencing tokens and test a stale owner after lease expiry. Make unavailable versus stale responses explicit during partial failure.

### Timeouts, backoff and retry budgets (`dist-timeouts`)

Allocate an end-to-end deadline and propagate cancellation to dependencies. Retry only safe transient failures with bounded jitter/backoff and a shared budget. Simulate ambiguous timeout completion and prevent retry amplification across layers.
