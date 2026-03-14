<img src="https://github.com/RQM-Technologies-dev/qsp-core/actions/workflows/ci.yml/badge.svg">

# qsp-core

`qsp-core` is the shared Quaternionic Signal Processing foundation library for the RQM Technologies ecosystem.

It provides small, reusable, pure-Python building blocks that downstream repositories can depend on for quaternion math, SU(2) utilities, baseline transforms, and simple filtering helpers.

## QSP Perspective

Quaternionic Signal Processing (QSP) is the engineering use of quaternion-valued mathematics for signals and state representations where orientation, phase, polarization, or frame relationships are intrinsic to the information being processed. In the RQM Technologies ecosystem, QSP is not just generic quaternion math; it is a modular software framework for building reusable tools across communications, robotics, navigation, sensing, and autonomy systems.

`qsp-core` is the stable mathematical foundation that makes that modular framework coherent. It defines the shared primitives every other QSP library depends on.

## Role in the QSP Ecosystem

`qsp-core` is the **lowest shared layer** of the RQM Technologies QSP stack. Its job is to provide the stable, reusable primitives that every other QSP library imports instead of reimplementing locally.

Responsibilities of `qsp-core`:

- **Quaternion representations** – the `Quaternion` value type and core arithmetic
- **Quaternion normalization** – `normalize_quaternion`, `is_unit_quaternion`
- **SU(2) helpers** – `quaternion_to_su2`, `su2_to_quaternion`, `matrix_trace`
- **Baseline transforms** – reference DFT/IDFT implementations for shared use and testing
- **Baseline filtering helpers** – `moving_average`, `clip`, `normalize_signal`
- **Shared validation utilities** – internal helpers that keep the foundation consistent

More specialized capabilities belong in downstream repositories. See the [Downstream Repositories](#downstream-repositories) section below.

## Boundary

The following belong in `qsp-core`:

- Foundational quaternion math primitives
- Shared conversion helpers (quaternion ↔ SU(2), iterable ↔ quaternion)
- Low-level reusable signal utilities
- Stable public interfaces that downstream repositories depend on

The following do **not** belong in `qsp-core`:

| Capability | Correct repository |
|---|---|
| Specialized spectral analysis, optimized FFT backends, windowing | `qsp-fft` |
| Advanced filter design, IIR/FIR construction, multi-stage pipelines | `qsp-filter` |
| Modulation schemes, constellation definitions, waveform logic | `qsp-modulation` |
| Attitude estimation, frame transforms, IMU fusion, diagnostics | `qsp-orientation` |
| Application orchestration and end-user workflows | application-layer repos |

Do not add downstream-specific logic to `qsp-core` even when it is mathematically related to the existing primitives. Keep the boundary discipline strict so downstream repositories remain independent and `qsp-core` remains small and stable.

## Ecosystem architecture

RQM Technologies is organized as a layered ecosystem:

- **Layer 1 – Foundation:** `qsp-core`, `qsp-fft`, `qsp-filter`, `qsp-modulation`
- **Layer 2 – Applications:** `eigenclock`, `quaternionic-modem`, `quaternionic-navigation`
- **Layer 3 – Public and research:** `website`, `documentation`, `research-notebooks`

`qsp-core` is the base of Layer 1. All other QSP libraries sit above it.

## Downstream repositories

`qsp-core` is the intended shared dependency for the following downstream libraries:

- **`qsp-fft`** – builds high-performance and specialized spectral transforms on the reference `dft`/`idft` boundary and shared quaternion primitives
- **`qsp-filter`** – builds richer filtering operators and filter design helpers on the shared baseline filtering utilities
- **`qsp-modulation`** – builds digital modulation and IQ helpers on the shared quaternion and SU(2) primitives
- **`qsp-orientation`** – builds attitude estimation, frame transforms, IMU fusion, and orientation diagnostics on the shared quaternion and SU(2) foundation

Application-layer repositories (`eigenclock`, `quaternionic-modem`, `quaternionic-navigation`) depend on `qsp-core` directly or indirectly through the higher-level QSP libraries.

See [`docs/downstream-usage.md`](docs/downstream-usage.md) for detailed import guidance.

## Current module layout

```text
qsp-core/
├── qsp/
│   ├── __init__.py
│   ├── quaternion.py
│   ├── su2.py
│   ├── transforms.py
│   ├── filters.py
│   └── utils.py
├── tests/
├── examples/
└── docs/
```

### Modules

- `qsp.quaternion` – `Quaternion` value type and core operations
- `qsp.su2` – SU(2) conversion helpers built on unit quaternions
- `qsp.transforms` – baseline DFT/IDFT utilities; reference implementations for `qsp-fft`
- `qsp.filters` – simple signal helpers; baseline implementations for `qsp-filter`
- `qsp.utils` – small internal validation helpers shared across modules

## Public API

The top-level `qsp` package exports the stable foundation surface:

- `Quaternion`
- `normalize_quaternion`, `is_unit_quaternion`, `quaternion_to_su2`, `su2_to_quaternion`, `matrix_trace`
- `dft`, `idft`
- `moving_average`, `clip`, `normalize_signal`

Downstream repositories should use top-level `qsp` imports as their primary dependency surface:

- `qsp-fft` should build on `dft`, `idft`, and shared quaternion/SU(2) primitives
- `qsp-filter` should build on `moving_average`, `clip`, and `normalize_signal`
- `qsp-modulation` should build on `Quaternion`, `normalize_quaternion`, `quaternion_to_su2`, `su2_to_quaternion`
- `qsp-orientation` should build on `Quaternion`, `normalize_quaternion`, `quaternion_to_su2`, `su2_to_quaternion`, `is_unit_quaternion`

Lower-level helpers such as `validate_signal()` and `validate_transform_input()` remain available from their module namespaces but are not part of the top-level public API.

See [`docs/api-overview.md`](docs/api-overview.md) for the full annotated API reference.

## Future extensions

Appropriate future growth for `qsp-core` includes:

- Additional quaternion arithmetic helpers (slerp, exp, log)
- Expanded SU(2) utilities
- More robust input validation and conversion helpers
- Improved API guarantees and stability documentation for downstream repos

The following should **not** be added to `qsp-core` in future work:

- Optimized FFT backends or spectral analysis algorithms → `qsp-fft`
- Advanced filtering pipelines or filter design APIs → `qsp-filter`
- Protocol-specific modulation or demodulation logic → `qsp-modulation`
- Attitude estimation, IMU fusion, or orientation diagnostics → `qsp-orientation`

See [`docs/repo-roadmap.md`](docs/repo-roadmap.md) for the full build-order roadmap and future scope.

## Publishing

Releases are published to [PyPI](https://pypi.org/project/qsp-core/) automatically via GitHub Actions using [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/) (OIDC – no long-lived API tokens required).

The publish workflow (`.github/workflows/publish.yml`) is triggered when a GitHub Release is published. It builds both a source distribution (`sdist`) and a wheel, then uploads them to PyPI through the `pypa/gh-action-pypi-publish` action.

To publish a new release:
1. Create and push a version tag (e.g. `v0.2.0`).
2. Draft and publish a GitHub Release targeting that tag.
3. The workflow runs automatically and uploads the distributions to PyPI.

> **One-time setup:** A Trusted Publisher entry for this repository must be configured in the PyPI project settings before the first automated publish. You must also create a `pypi` environment in the GitHub repository settings (used by the publish job for deployment protection rules). See the [PyPI Trusted Publishing guide](https://docs.pypi.org/trusted-publishers/adding-a-publisher/) for instructions.

## Package name vs import name

> **PyPI distribution name:** `qsp-core`
> **Python import name:** `qsp`
>
> Install the package as `qsp-core` (e.g. `pip install qsp-core`) and import it as `qsp` (e.g. `from qsp import Quaternion`).
> This distinction applies across the whole RQM Technologies ecosystem: every downstream repository depends on the `qsp-core` distribution but imports from the `qsp` namespace.

## Local installation

Install the package locally from the repository root:

```bash
python -m pip install -e .
```

## Running tests

This repository keeps the test stack minimal and uses the Python standard library:

```bash
python -m unittest discover -s tests
```

## Running examples

Run the example modules from the repository root:

```bash
python -m examples.quaternion_basics
python -m examples.su2_demo
python -m examples.transform_demo
python -m examples.filter_demo
```

## Documentation

Additional ecosystem and API notes live in `docs/`:

- `docs/architecture.md`
- `docs/api-overview.md`
- `docs/repo-roadmap.md`
- `docs/downstream-usage.md`
