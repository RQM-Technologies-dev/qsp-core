# RQM Technologies – Agent Instructions

This repository is the foundation of the RQM Technologies QSP ecosystem.

## Role of this repository

`qsp-core` is the **foundational Layer-1 library** of the Quaternionic Signal Processing ecosystem. It contains the base mathematical primitives used by all other RQM Technologies QSP projects.

It must remain:

- small and focused
- modular
- pure Python
- dependency-light
- mathematically clear and stable

This repo provides the shared math utilities that downstream repositories depend on.
Downstream repositories must import shared quaternion, SU(2), transform, and filtering primitives from `qsp-core` instead of reimplementing that foundation logic locally.

## Ecosystem architecture

The full RQM Technologies ecosystem is structured as:

```
RQM-Technologies
├── Layer 1 – Foundation
│   ├── qsp-core         ← this repo
│   ├── qsp-fft
│   ├── qsp-filter
│   └── qsp-modulation
├── Layer 2 – Applications
│   ├── eigenclock
│   ├── quaternionic-modem
│   └── quaternionic-navigation
└── Layer 3 – Public interface
    ├── website
    ├── documentation
    └── research-notebooks
```

### Layer 1 – Core math libraries

These repositories implement reusable quaternionic signal processing primitives.

- `qsp-core` (this repo) – shared foundation primitives
- `qsp-fft` – high-performance and specialized spectral transforms
- `qsp-filter` – richer filter design and processing utilities
- `qsp-modulation` – modulation schemes, constellation logic, IQ helpers
- `qsp-orientation` – attitude estimation, frame transforms, IMU fusion, orientation diagnostics

### Layer 2 – Applications

These repositories implement domain systems built on QSP.

- `eigenclock`
- `quaternionic-modem`
- `quaternionic-navigation`

### Layer 3 – Public interface

These repositories provide public-facing material.

- `website`
- `documentation`
- `research-notebooks`

## Boundary – what belongs here and what does not

### What belongs in `qsp-core`

- Foundational quaternion math primitives (`Quaternion` type, arithmetic, normalization)
- Shared conversion helpers (quaternion ↔ SU(2), iterable ↔ quaternion)
- Baseline transform reference implementations (`dft`, `idft`)
- Low-level reusable signal utilities (`moving_average`, `clip`, `normalize_signal`)
- Stable public interfaces that downstream repositories depend on
- Internal validation helpers that support the foundation without adding downstream policy

### What does NOT belong in `qsp-core`

| Capability | Correct repository |
|---|---|
| Specialized spectral analysis, optimized FFT backends, windowing | `qsp-fft` |
| Advanced filter design, IIR/FIR construction, multi-stage pipelines | `qsp-filter` |
| Modulation schemes, constellation definitions, waveform logic | `qsp-modulation` |
| Attitude estimation, frame transforms, IMU fusion, diagnostics | `qsp-orientation` |
| Application orchestration and end-user workflows | application-layer repos |

**Do not add downstream-specific logic to `qsp-core`** even when it is mathematically related to the existing primitives. The boundary discipline is what keeps downstream repositories independent and `qsp-core` small and stable.

## Rules for agents

When making changes to this repository:

1. Do not add UI code.
2. Do not add deployment code.
3. Do not add website content.
4. Keep functions small and testable.
5. Prefer pure Python.
6. Avoid unnecessary dependencies.
7. When functionality changes, update README and docs.
8. **Do not duplicate functionality that belongs in a downstream repository** (`qsp-fft`, `qsp-filter`, `qsp-modulation`, `qsp-orientation`).
9. **Do not absorb specialized downstream logic** into `qsp-core` even under the guise of "convenience helpers."
10. **Treat public API changes as breaking changes.** Downstream repos depend on stability. Deprecate before removing.
11. **Add new helpers to `qsp-core` only when** they are clearly reusable across multiple downstream repositories and do not pull downstream-specific concerns into the foundation layer.

## Public API stability

`qsp-core` is intended to be a **stable shared dependency**. Its public surface is:

- `Quaternion` and its methods
- `normalize_quaternion`, `is_unit_quaternion`, `quaternion_to_su2`, `su2_to_quaternion`, `matrix_trace`
- `dft`, `idft`
- `moving_average`, `clip`, `normalize_signal`

All of these are exported from the top-level `qsp` namespace. Do not remove or incompatibly change these without considering the downstream impact on `qsp-fft`, `qsp-filter`, `qsp-modulation`, and `qsp-orientation`.

Internal helpers in `qsp.utils`, `qsp.filters.validate_signal`, and `qsp.transforms.validate_transform_input` are not part of the public surface and may change more freely.

## Repository structure

The expected structure for this repository is:

```
qsp/
tests/
examples/
docs/
```

## Immediate priorities

Agents working in this repository should focus on:

- quaternion math utilities
- SU(2) utilities
- baseline spectral transforms
- baseline signal filters
- shared validation utilities

All functionality should be reusable by downstream repositories.
