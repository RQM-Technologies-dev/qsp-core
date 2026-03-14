# Downstream usage guidance

Downstream repositories should treat `qsp-core` as the canonical source for shared quaternionic primitives.

## Package name vs import name

> **PyPI distribution name:** `qsp-core`
> **Python import name:** `qsp`
>
> Declare `qsp-core` as the dependency in your project configuration (e.g. `pyproject.toml`), then import from the `qsp` namespace in your code.

```toml
# pyproject.toml
[project]
dependencies = ["qsp-core"]
```

```python
# your_module.py
from qsp import Quaternion, dft, idft
```

## Recommended dependency pattern

- `qsp-fft` should import the shared quaternion and transform foundations from `qsp-core` and extend the transform layer with optimized or specialized implementations.
- `qsp-filter` should import the shared filtering foundations from `qsp-core` and extend them with richer filter design and processing utilities.
- `qsp-modulation` should import quaternion and SU(2) helpers from `qsp-core` instead of reimplementing them.
- `qsp-orientation` should import quaternion and SU(2) helpers from `qsp-core` as the shared foundation for attitude estimation, frame transforms, and IMU fusion.
- `eigenclock`, `quaternionic-modem`, and `quaternionic-navigation` should depend on `qsp-core` directly or indirectly through the higher-level QSP libraries.

Prefer the top-level `qsp` imports for stable shared primitives. Reach into
module-level helpers such as `qsp.filters.validate_signal` only when a
downstream repository explicitly needs that lower-level behavior.

## What each downstream library should import

### `qsp-fft`

Use `qsp-core` for the reference transform boundary and any shared quaternion
primitives that higher-level spectral work needs:

```python
from qsp import Quaternion, dft, idft
```

Keep the following in `qsp-fft`, not `qsp-core`:

- optimized FFT implementations
- windowing families and spectral analysis pipelines
- performance-focused transform backends

### `qsp-filter`

Use `qsp-core` for small, reusable filtering helpers that define the shared
baseline behavior:

```python
from qsp import clip, moving_average, normalize_signal
```

Keep the following in `qsp-filter`, not `qsp-core`:

- richer filter design APIs
- IIR/FIR construction and tuning logic
- multi-stage filtering pipelines

### `qsp-modulation`

Use `qsp-core` for quaternion and SU(2) primitives that modulation layers can
share without duplicating math foundations:

```python
from qsp import (
    Quaternion,
    is_unit_quaternion,
    normalize_quaternion,
    quaternion_to_su2,
    su2_to_quaternion,
)
```

Keep the following in `qsp-modulation`, not `qsp-core`:

- constellation definitions
- carrier, symbol, and framing logic
- protocol-specific modulation and demodulation workflows

### `qsp-orientation`

Use `qsp-core` for quaternion and SU(2) primitives that orientation and frame
transform work depends on:

```python
from qsp import (
    Quaternion,
    is_unit_quaternion,
    normalize_quaternion,
    quaternion_to_su2,
    su2_to_quaternion,
)
```

Keep the following in `qsp-orientation`, not `qsp-core`:

- attitude state representations and estimation algorithms
- frame transformation pipelines
- IMU sensor fusion and calibration
- orientation diagnostics and health monitoring

## What should stay in qsp-core

- Quaternion math primitives
- SU(2) conversion helpers
- Baseline transform validation and reference transforms
- Shared filtering utilities
- Small shared validation helpers that support those foundations without adding downstream policy

`qsp-core` should remain small, stable, and explicit. Add new helpers here only
when they are clearly reusable across multiple downstream repositories and do
not pull downstream-specific concerns into the foundation layer.

## What should move to higher-level repositories

- Optimized FFT implementations
- Advanced filtering pipelines
- Domain-specific modulation logic
- Attitude estimation, IMU fusion, and orientation diagnostics
- Application-specific workflows and orchestration
