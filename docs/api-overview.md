# API overview

The current `qsp-core` API is intentionally small. Downstream repositories
should usually import from the top-level `qsp` namespace and only reach into
module-level helpers when they need a lower-level building block.

## Top-level `qsp` API

- `Quaternion`
- `normalize_quaternion(value)`
- `is_unit_quaternion(value, tolerance=1e-9)`
- `quaternion_to_su2(value)`
- `su2_to_quaternion(matrix, tolerance=1e-9)`
- `matrix_trace(matrix)`
- `dft(values)`
- `idft(values)`
- `moving_average(values, window_size)`
- `clip(values, minimum, maximum)`
- `normalize_signal(values)`

## `qsp.quaternion`

- `Quaternion(w, x, y, z)`
- `Quaternion.from_iterable(values)`
- `to_tuple()`
- `norm()`
- `conjugate()`
- `multiply(other)`
- `add(other)`
- `subtract(other)`
- `scalar_multiply(scalar)`
- `normalize()`

## `qsp.su2`

- `normalize_quaternion(value)`
- `is_unit_quaternion(value, tolerance=1e-9)`
- `quaternion_to_su2(value)`
- `su2_to_quaternion(matrix, tolerance=1e-9)`
- `matrix_trace(matrix)`

## `qsp.transforms`

- `validate_transform_input(values)`
- `dft(values)`
- `idft(values)`

These transforms are reference implementations for shared usage and testing. High-performance or specialized spectral algorithms should live in `qsp-fft`.

## `qsp.filters`

- `validate_signal(values, allow_empty=True)`
- `moving_average(values, window_size)`
- `clip(values, minimum, maximum)`
- `normalize_signal(values)`

## Internal helpers

`qsp.utils` contains small shared validation helpers used by the package
internally:

- `ensure_real_number(value, name=...)`
- `ensure_real_sequence(values, name=..., allow_empty=False)`
- `ensure_complex_sequence(values, name=..., allow_empty=False)`
- `approx_equal(left, right, tolerance=1e-9)`

These helpers are intentionally kept out of the top-level API so the public
surface remains compact and stable.
