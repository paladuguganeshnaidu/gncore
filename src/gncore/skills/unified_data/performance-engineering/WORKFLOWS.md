# GNCore Performance Engineering: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Python Performance (`python-performance`)

Measure a representative baseline before optimizing. Profile CPU and memory with available tools, identify the dominant hotspot, and optimize that path while preserving outputs and errors. Avoid clever micro-optimizations without evidence. Re-run the same workload and report hardware, input scale, and before/after measurements.

### Comparable benchmark design (`perf-benchmark-design`)

Specify representative input, machine/runtime versions, warmup, repeats and measurement boundaries. Separate setup from the measured operation and retain raw timings, not just a best run. Compare equivalent outputs and report dispersion and measurement noise.

### Memory and allocation diagnosis (`perf-memory-profile`)

Distinguish retained state, allocation rate and peak working set on the same workload. Identify the allocation/retention path before optimizing and verify object lifetime after the change. Report tool limitations and workload-dependent tradeoffs.

### Tail latency and saturation (`perf-tail-latency`)

Record load generation, concurrency, timeouts and latency percentiles, including failed requests. Ramp only an authorized local/staging target and identify the saturation knee. Avoid coordinated-omission or success-only summaries that hide slow/failed work.

### Performance regression review (`perf-regression`)

Reproduce baseline and candidate under matching conditions, check correctness first and compare distributions with a practical change threshold. Trace regressions to a measured path and retain the raw evidence; avoid brittle single-run timing assertions in unit tests.
