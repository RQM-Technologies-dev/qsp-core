# Repository roadmap

## Build order

Recommended build order for the RQM Technologies software stack:

1. **`qsp-core`** – establish the reusable quaternion, SU(2), transform, filter, and validation foundation
2. **`qsp-orientation`** – build attitude estimation, frame transforms, and IMU fusion on the shared foundation
3. **`qsp-modulation`** – build modulation and demodulation logic on the shared QSP layer
4. **`qsp-fft`** – build higher-performance and specialized spectral transforms on top of `qsp-core`
5. **`qsp-filter`** – build richer filtering operators and filter design helpers on top of `qsp-core`
6. **Applications** – `eigenclock`, `quaternionic-modem`, and `quaternionic-navigation`
7. **Public artifacts** – `website`, `documentation`, and `research-notebooks`

The key design rule is that repositories above `qsp-core` should reuse the shared math primitives instead of creating local copies. That keeps the base behavior consistent across the ecosystem.

## Future extensions appropriate for `qsp-core`

The following represent appropriate future growth for `qsp-core`:

- **Additional quaternion utilities** – slerp (spherical linear interpolation), exp, log, and angle-axis construction helpers
- **Expanded SU(2) utilities** – additional group-theoretic helpers for downstream orientation and modulation work
- **More robust conversion utilities** – better coercion from NumPy arrays, lists, and other common formats
- **Shared validation helpers** – lightweight assertion utilities that prevent duplicated validation code across downstream repos
- **Improved API guarantees** – explicit stability annotations, deprecation machinery, and version-aligned compatibility notes for downstream repos
- **Additional baseline transforms** – DTFT or other reference implementations if they become shared reference boundaries for downstream repos

Each addition should be evaluated against the criterion: *Is this clearly reusable by multiple downstream repositories and free of downstream-specific concerns?*

## What must NOT be added to `qsp-core`

The following work belongs in downstream repositories, not here:

| Future capability | Correct repository |
|---|---|
| Optimized FFT backends, FFTW/NumPy wrappers, windowing families | `qsp-fft` |
| Advanced filtering pipelines, filter design APIs, IIR/FIR tuning | `qsp-filter` |
| Protocol-specific modulation/demodulation, constellation tables, waveform encoding | `qsp-modulation` |
| Attitude estimation algorithms, IMU fusion, sensor calibration | `qsp-orientation` |
| Application orchestration, end-to-end workflows, product logic | application-layer repos |

Adding these to `qsp-core` would grow its dependency surface, violate the layered architecture, and force unrelated downstream repos to carry unnecessary weight.
