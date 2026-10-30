# GNCore Systems Programming: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Ownership and resource lifetime (`systems-ownership`)

Map allocation, ownership transfer, borrowing and cleanup for each resource. Use RAII or language-native lifetime guarantees where possible; define cancellation/error cleanup and test repeated creation/destruction without leaks or use-after-free.

### FFI and ABI boundaries (`systems-ffi`)

Specify ABI, fixed-width types, layout/alignment, lengths, encoding, ownership and matching destruction on both sides. Enforce checkable null, handle, length, alignment and overflow contracts, and document caller obligations for pointer provenance, lifetime and readable extent that cannot be established by superficial pointer inspection. Translate errors without unwinding across an incompatible boundary; test caller-language cleanup, invalid handles and in-flight callback teardown.

### Integer and buffer boundaries (`systems-safe-arithmetic`)

State allowed numeric ranges and byte/element units. Check overflow before allocation/index arithmetic and validate buffer length before access. Exercise minimum/maximum values and malformed input with compiler/runtime checks enabled.

### Native concurrency (`systems-concurrency`)

Identify shared state, synchronization and the ownership of shutdown. Specify lock order and atomic memory-order requirements before choosing lock-free structures. Test cancellation, contention and race instrumentation where supported; explain the limits of stress tests.
