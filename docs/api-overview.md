# API overview

The current `qsp-core` API is intentionally small.

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

## `qsp.utils`

- `ensure_real_number(value, name=...)`
- `ensure_real_sequence(values, name=..., allow_empty=False)`
- `ensure_complex_sequence(values, name=..., allow_empty=False)`
- `approx_equal(left, right, tolerance=1e-9)`
