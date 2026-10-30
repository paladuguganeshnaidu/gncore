# GNCore Python: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Python Library Engineering (`python-library`)

Inspect supported Python versions, packaging backend, and public imports. Keep public APIs small and backward-compatible unless a breaking change is requested. Use explicit types and focused modules, avoid import-time side effects, declare runtime dependencies accurately, and provide a minimal runnable example. Check wheel and source inclusion rules when packaging changes.

### Python Packaging (`python-packaging`)

For packaging changes, inspect the build backend, supported interpreters, dependencies, resources and public entrypoints. Produce the sdist, build a wheel from that archive and inspect both inventories. Clean-install outside the source checkout and invoke imports/commands from unrelated working directories on the supported interpreter range. Honor existing release authorization and keep build/compatibility evidence distinct from publication; ordinary Python fixes need only checks relevant to their behavior.

### Python Upgrade and Migration (`python-migration`)

Identify the source and target versions, supported users, deprecations, and dependency constraints. Search all call sites, update in small coherent steps, and preserve public behavior unless the request says otherwise. Verify on the supported version matrix where available and document breaking changes. Avoid broad dependency upgrades bundled into the migration.
