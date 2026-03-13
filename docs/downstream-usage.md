# Downstream usage guidance

Downstream repositories should treat `qsp-core` as the canonical source for shared quaternionic primitives.

## Recommended dependency pattern

- `qsp-fft` should import the shared quaternion and transform foundations from `qsp-core` and extend the transform layer with optimized or specialized implementations.
- `qsp-filter` should import the shared filtering foundations from `qsp-core` and extend them with richer filter design and processing utilities.
- `qsp-modulation` should import quaternion and SU(2) helpers from `qsp-core` instead of reimplementing them.
- `eigenclock`, `quaternionic-modem`, and `quaternionic-navigation` should depend on `qsp-core` directly or indirectly through the higher-level QSP libraries.

Prefer the top-level `qsp` imports for stable shared primitives. Reach into
module-level helpers such as `qsp.filters.validate_signal` only when a
downstream repository explicitly needs that lower-level behavior.

## What should stay in qsp-core

- Quaternion math primitives
- SU(2) conversion helpers
- Baseline transform validation and reference transforms
- Shared filtering utilities
- Small shared validation helpers

## What should move to higher-level repositories

- Optimized FFT implementations
- Advanced filtering pipelines
- Domain-specific modulation logic
- Application-specific workflows and orchestration
