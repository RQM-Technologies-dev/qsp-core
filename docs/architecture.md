# qsp-core architecture

RQM Technologies is organized into three layers:

1. **Core math libraries** – `qsp-core`, `qsp-fft`, `qsp-filter`, `qsp-modulation`
2. **Applications** – `eigenclock`, `quaternionic-modem`, `quaternionic-navigation`
3. **Public and research material** – `website`, `documentation`, `research-notebooks`

`qsp-core` sits at the bottom of the software stack. It should remain small, pure Python, and reusable. Its role is to provide stable quaternion, SU(2), baseline transform, filter, and validation helpers that higher-level repositories can import directly.

This repository intentionally implements only the shared foundation layer. Advanced FFT work belongs in `qsp-fft`, richer filtering in `qsp-filter`, and modulation-specific logic in `qsp-modulation`.
