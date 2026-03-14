# API overview

The `qsp-core` public API is intentionally small and stable. Downstream repositories
should import from the top-level `qsp` namespace and only reach into module-level
helpers when they need a specific lower-level building block.

Changes to the top-level API are treated as breaking changes. Do not remove or
incompatibly modify these without considering downstream impact.

## Quaternion primitives

These are the core building blocks for quaternion-valued computation. Every downstream
QSP library that works with quaternions should depend on these rather than providing
its own implementation.

### Top-level exports

| Symbol | Description |
|---|---|
| `Quaternion` | Immutable quaternion value type `(w, x, y, z)` |

### `qsp.quaternion.Quaternion`

| Method / class method | Description |
|---|---|
| `Quaternion(w, x, y, z)` | Construct from four real components |
| `Quaternion.from_iterable(values)` | Construct from any four-element iterable |
| `to_tuple()` | Return `(w, x, y, z)` as a 4-tuple |
| `norm()` | Euclidean norm |
| `conjugate()` | Quaternion conjugate `(w, -x, -y, -z)` |
| `add(other)` | Component-wise sum |
| `subtract(other)` | Component-wise difference |
| `scalar_multiply(scalar)` | Scale by a real scalar |
| `multiply(other)` | Hamilton product |
| `normalize()` | Return unit-length copy |

**Downstream reuse:** `qsp-fft`, `qsp-filter`, `qsp-modulation`, and `qsp-orientation`
should all import `Quaternion` from `qsp` rather than defining their own type.

---

## SU(2) helpers

Conversion utilities between unit quaternions and SU(2) 2×2 complex matrices.
These are the shared interface for any downstream library that works with rotation
representations or spin-½ group elements.

### Top-level exports

| Symbol | Description |
|---|---|
| `normalize_quaternion(value)` | Normalize a quaternion or four real values to unit length |
| `is_unit_quaternion(value, tolerance=1e-9)` | Test for unit norm within tolerance |
| `quaternion_to_su2(value)` | Convert a unit quaternion to its SU(2) 2×2 matrix |
| `su2_to_quaternion(matrix, tolerance=1e-9)` | Convert an SU(2) matrix back to a unit quaternion |
| `matrix_trace(matrix)` | Return the trace of a 2×2 matrix |

**Downstream reuse:** `qsp-modulation` and `qsp-orientation` should import these
directly from `qsp` rather than reimplementing quaternion–matrix conversions.

---

## Transforms

Reference DFT and IDFT implementations intended for shared use across the ecosystem
and as the baseline boundary for `qsp-fft`. These are not optimized for production
performance; they exist to establish a stable shared interface.

### Top-level exports

| Symbol | Description |
|---|---|
| `dft(values)` | Discrete Fourier Transform over a complex sequence |
| `idft(values)` | Inverse Discrete Fourier Transform |

### `qsp.transforms` (module-level)

| Symbol | Description |
|---|---|
| `validate_transform_input(values)` | Validate that input is a non-empty complex sequence (internal) |

**Note:** High-performance or specialized spectral algorithms belong in `qsp-fft`,
not here. The `dft`/`idft` here are reference implementations only.

---

## Filtering helpers

Baseline signal utilities intended for shared use across the ecosystem and as the
boundary that `qsp-filter` extends. These are intentionally simple.

### Top-level exports

| Symbol | Description |
|---|---|
| `moving_average(values, window_size)` | Simple moving average over a real sequence |
| `clip(values, minimum, maximum)` | Clip each element to `[minimum, maximum]` |
| `normalize_signal(values)` | Normalize a real sequence to `[0, 1]` |

### `qsp.filters` (module-level)

| Symbol | Description |
|---|---|
| `validate_signal(values, allow_empty=True)` | Validate a real-valued signal sequence (internal) |

**Note:** Advanced filter design, IIR/FIR construction, and multi-stage pipelines
belong in `qsp-filter`, not here.

---

## Internal utilities

`qsp.utils` contains small shared validation helpers used internally by the package.
These are **not** part of the public API. They may change without a deprecation cycle.

| Symbol | Description |
|---|---|
| `ensure_real_number(value, name=...)` | Assert that a value is a finite real number |
| `ensure_real_sequence(values, name=..., allow_empty=False)` | Assert a sequence of finite real numbers |
| `ensure_complex_sequence(values, name=..., allow_empty=False)` | Assert a sequence of complex or real numbers |
| `approx_equal(left, right, tolerance=1e-9)` | Approximate equality for scalars and complex values |

These helpers are intentionally kept out of the top-level API so the public
surface remains compact and stable. Downstream repositories should not depend on
them directly.
