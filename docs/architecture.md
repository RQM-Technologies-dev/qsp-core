# qsp-core architecture

## QSP Perspective

Quaternionic Signal Processing (QSP) is the engineering use of quaternion-valued mathematics for signals and state representations where orientation, phase, polarization, or frame relationships are intrinsic to the information being processed. In the RQM Technologies ecosystem, QSP is not just generic quaternion math; it is a modular software framework for building reusable tools across communications, robotics, navigation, sensing, and autonomy systems.

`qsp-core` is the stable mathematical foundation that makes that modular framework coherent. It defines the shared primitives every other QSP library depends on.

## Ecosystem layers

RQM Technologies is organized into three layers:

1. **Layer 1 – Foundation libraries**
   `qsp-core`, `qsp-fft`, `qsp-filter`, `qsp-modulation`, `qsp-orientation`

2. **Layer 2 – Applications**
   `eigenclock`, `quaternionic-modem`, `quaternionic-navigation`

3. **Layer 3 – Public and research material**
   `website`, `documentation`, `research-notebooks`

```
qsp-core  ←─────────────────────────────── shared foundation
    ↑
    ├── qsp-fft          (spectral transforms)
    ├── qsp-filter       (filtering operations)
    ├── qsp-modulation   (modulation / IQ)
    └── qsp-orientation  (attitude / IMU / frame transforms)
             ↑
             ├── eigenclock
             ├── quaternionic-modem
             └── quaternionic-navigation
```

## Role in the QSP Ecosystem

`qsp-core` sits at the bottom of the software stack. It is the **stable shared dependency** for every other QSP library. Its role is to provide:

- **Quaternion representations** – the `Quaternion` value type and core arithmetic (Hamilton product, conjugate, norm, normalization, scalar multiply, add, subtract)
- **Quaternion normalization** – `normalize_quaternion`, `is_unit_quaternion`
- **SU(2) helpers** – `quaternion_to_su2`, `su2_to_quaternion`, `matrix_trace`
- **Baseline transforms** – reference DFT/IDFT implementations; the boundary that `qsp-fft` extends
- **Baseline filtering helpers** – `moving_average`, `clip`, `normalize_signal`; the boundary that `qsp-filter` extends
- **Shared validation utilities** – small internal helpers that keep the foundation consistent across modules

Every downstream repository imports these primitives from `qsp-core` instead of reimplementing them. That shared dependency is what keeps the ecosystem consistent.

## Boundary

### What belongs in `qsp-core`

- Foundational quaternion math primitives
- Shared conversion helpers (quaternion ↔ SU(2), iterable ↔ quaternion)
- Low-level reusable signal utilities
- Stable public interfaces that downstream repositories depend on
- Internal validation helpers that support those foundations without adding downstream policy

### What does NOT belong in `qsp-core`

| Capability | Correct repository |
|---|---|
| Specialized spectral analysis, optimized FFT backends, windowing families | `qsp-fft` |
| Advanced filter design, IIR/FIR construction, multi-stage filtering pipelines | `qsp-filter` |
| Modulation schemes, constellation definitions, carrier/waveform logic | `qsp-modulation` |
| Attitude estimation, frame transforms, IMU fusion, orientation diagnostics | `qsp-orientation` |
| Application orchestration and end-user workflows | application-layer repos |

The boundary discipline is strict by design. Adding downstream-specific logic to `qsp-core` — even when it is mathematically adjacent to existing primitives — increases the scope of what every downstream repository must accept as a dependency, undermines the layered architecture, and makes `qsp-core` harder to keep stable.

## Downstream repositories

### `qsp-fft`

Builds high-performance and specialized spectral transforms on top of the reference `dft`/`idft` boundary provided by `qsp-core`. It should import `Quaternion`, `dft`, and `idft` from `qsp-core` and add:

- optimized FFT implementations
- windowing families and spectral analysis pipelines
- performance-focused transform backends

### `qsp-filter`

Builds richer filtering operators and filter design helpers on top of the shared baseline provided by `qsp-core`. It should import `moving_average`, `clip`, and `normalize_signal` and add:

- richer filter design APIs
- IIR/FIR construction and tuning logic
- multi-stage filtering pipelines

### `qsp-modulation`

Builds digital modulation and IQ helpers on the shared quaternion and SU(2) foundation from `qsp-core`. It should import `Quaternion`, `normalize_quaternion`, `quaternion_to_su2`, `su2_to_quaternion` and add:

- constellation definitions
- carrier, symbol, and framing logic
- protocol-specific modulation and demodulation workflows

### `qsp-orientation`

Builds attitude estimation, frame transforms, IMU fusion, and orientation diagnostics on the shared quaternion and SU(2) foundation from `qsp-core`. It should import `Quaternion`, `normalize_quaternion`, `quaternion_to_su2`, `su2_to_quaternion`, `is_unit_quaternion` and add:

- orientation state representations
- frame transformation pipelines
- IMU sensor fusion algorithms
- diagnostics and health monitoring for orientation systems

## Module layout

```text
qsp-core/
├── qsp/
│   ├── __init__.py      ← stable public surface
│   ├── quaternion.py    ← Quaternion type and core operations
│   ├── su2.py           ← SU(2) conversion helpers
│   ├── transforms.py    ← baseline DFT/IDFT reference implementations
│   ├── filters.py       ← baseline filtering helpers
│   └── utils.py         ← internal validation utilities
├── tests/
├── examples/
└── docs/
```

The top-level `qsp` namespace exports only the stable public surface. Internal helpers remain in their module namespaces.

## Design principles

- **Small and stable.** Add to `qsp-core` only what is clearly needed by multiple downstream repositories and has no downstream-specific concerns.
- **Pure Python.** No compiled extensions or heavy numeric libraries in the foundation layer.
- **Dependency-light.** The only dependency is the Python standard library.
- **Public API changes are breaking changes.** Downstream repos depend on this boundary. Deprecate before removing.
