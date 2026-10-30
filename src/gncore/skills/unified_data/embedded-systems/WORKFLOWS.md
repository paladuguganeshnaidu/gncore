# GNCore Embedded Systems: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Firmware state machines (`embedded-state-machine`)

Separate pure state transitions from peripheral effects. Define events, deadlines and valid states; make retries bounded and recovery explicit. Simulate event sequences, repeated inputs and reset without requiring a device.

### Peripheral protocol integration (`embedded-protocols`)

Verify board pins, voltage assumptions, bus configuration, frame format and timeout behavior against the actual hardware documentation. Isolate the transport behind a testable boundary and inject truncated, delayed and corrupt frames in host tests.

### Timers and interrupt boundaries (`embedded-timing`)

Define tick units, counter width, wraparound and interrupt/main-loop ownership. Keep interrupt work bounded and use wrap-safe elapsed-time comparisons. Test deadlines across counter rollover and report which timing claims still require hardware measurement.

### Constrained memory and firmware builds (`embedded-memory`)

Record flash/RAM limits, stack/heap use and linker configuration for the target. Prefer bounded buffers and deterministic allocation where required. Inspect map/build output and exercise maximum frames and reset paths; desktop simulation does not certify device memory headroom.
