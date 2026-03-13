# Downstream usage guidance

Downstream repositories should treat `qsp-core` as the canonical source for shared quaternionic primitives.

## Recommended dependency pattern

- `qsp-fft` should import quaternion and validation helpers from `qsp-core` and extend the transform layer.
- `qsp-filter` should import signal validation and normalization helpers from `qsp-core` and extend the filtering layer.
- `qsp-modulation` should import quaternion and SU(2) helpers from `qsp-core` instead of reimplementing them.
- `eigenclock`, `quaternionic-modem`, and `quaternionic-navigation` should depend on `qsp-core` directly or indirectly through the higher-level QSP libraries.

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
