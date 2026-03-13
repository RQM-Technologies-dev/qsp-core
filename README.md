# qsp-core

`qsp-core` is the shared Quaternionic Signal Processing foundation library for the RQM Technologies ecosystem.

It provides small, reusable, pure-Python building blocks that downstream repositories can depend on for quaternion math, SU(2) utilities, baseline transforms, and simple filtering helpers.

## Why this repository exists

RQM Technologies is organized as a layered ecosystem:

- **Foundation layer:** `qsp-core`, `qsp-fft`, `qsp-filter`, `qsp-modulation`
- **Application layer:** `eigenclock`, `quaternionic-modem`, `quaternionic-navigation`
- **Public and research layer:** `website`, `documentation`, `research-notebooks`

`qsp-core` is the lowest shared layer. Future repositories should import common quaternion and SU(2) logic from `qsp-core` instead of reimplementing the same primitives independently.

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

- `qsp.quaternion` – starter `Quaternion` type and core operations
- `qsp.su2` – minimal SU(2) conversion helpers built on unit quaternions
- `qsp.transforms` – baseline DFT/IDFT utilities for future `qsp-fft` work
- `qsp.filters` – simple signal helpers for future `qsp-filter` work
- `qsp.utils` – small shared validation helpers used across modules

## Downstream repositories expected to depend on qsp-core

- `qsp-fft`
- `qsp-filter`
- `qsp-modulation`
- `eigenclock`
- `quaternionic-modem`
- `quaternionic-navigation`

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
