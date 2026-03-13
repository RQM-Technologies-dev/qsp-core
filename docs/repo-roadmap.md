# Repository roadmap

Recommended build order for the RQM Technologies software stack:

1. **`qsp-core`** – establish the reusable quaternion, SU(2), transform, filter, and validation foundation
2. **`qsp-fft`** – build higher-performance and specialized spectral transforms on top of `qsp-core`
3. **`qsp-filter`** – build richer filtering operators and filter design helpers on top of `qsp-core`
4. **`qsp-modulation`** – build modulation and demodulation logic on top of the shared QSP layer
5. **Applications** – `eigenclock`, `quaternionic-modem`, and `quaternionic-navigation`
6. **Public artifacts** – `website`, `documentation`, and `research-notebooks`

The key design rule is that repositories above `qsp-core` should reuse the shared math primitives instead of creating local copies. That keeps the base behavior consistent across the ecosystem.
