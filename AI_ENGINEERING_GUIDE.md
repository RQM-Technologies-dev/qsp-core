# AI Engineering Guide — QSP Ecosystem

This repository is part of the **Quaternionic Signal Processing (QSP) ecosystem** developed by **RQM Technologies**.

The QSP ecosystem is a modular set of Python libraries for quaternion-based signal processing, orientation handling, communications, and autonomy systems.

Repositories in the ecosystem include:

```
qsp-core
qsp-fft
qsp-filter
qsp-modulation
qsp-orientation
```

Future repositories may include:

```
quaternionic-modem
quaternionic-navigation
eigenclock
```

---

# Authority / Precedence

When this file and other documentation conflict, apply the following order of precedence (highest to lowest):

1. **`AGENTS.md`** (repo root) — repo-specific rules and explicit overrides. Wins over this guide only where it explicitly states a local exception; rules not mentioned in `AGENTS.md` fall back to this guide.
2. **`AI_ENGINEERING_GUIDE.md`** (this file) — shared cross-repo doctrine. Applies to all QSP repositories as the default baseline.
3. **Per-repo docs** (e.g., `docs/architecture.md`, `docs/api-overview.md`) — authoritative for that repository's internal structure and design decisions.

---

# Design Philosophy

Quaternionic Signal Processing (QSP) treats quaternions as first-class representations for signals and state vectors whose meaning depends on orientation, phase, polarization, or frame relationships.

The goal of the ecosystem is to provide reusable tools for:

* communications systems
* robotics
* navigation
* autonomy
* sensing
* spatial computing

Each repository should remain **small, focused, and composable**.

---

# Repository Boundaries

Each repository has a clear role.

### qsp-core

Foundational primitives:

* quaternion math
* SU(2) helpers
* baseline transforms
* shared utilities

### qsp-fft

Spectral analysis utilities.

### qsp-filter

Filtering and normalization helpers.

### qsp-modulation

Digital modulation and IQ helpers.

### qsp-orientation

Orientation estimation, coordinate frame transforms, IMU integration, and drift diagnostics.

---

# Engineering Rules

When generating code for this repository:

1. **Keep functions small and composable**
2. **Prefer pure functional design**
3. **Avoid unnecessary classes**
4. **Minimize dependencies**
5. **Respect repository boundaries**
6. **Do not duplicate functionality from other QSP repos**

---

# API Discipline

Public APIs should be:

* stable
* clearly documented
* exported through `__init__.py`

Internal helpers should not be exposed unnecessarily.

---

# Testing Expectations

All new functionality must include pytest tests.

Tests should verify:

* mathematical correctness
* edge cases
* API surface stability

---

# Documentation Expectations

Each repository should include:

```
README.md
AGENTS.md
docs/architecture.md
docs/api-overview.md
```

Documentation should explain:

* repository purpose
* boundaries
* public API
* relationship to other QSP repos

---

# Extension Guidelines

When adding new functionality:

1. Confirm it belongs in this repository.
2. Avoid expanding the repository's scope.
3. If functionality belongs elsewhere, propose a new repository.

---

# Ecosystem Goal

The QSP ecosystem is intended to support production-grade software for communications, robotics, navigation, sensing, and autonomy systems.

Code should prioritize:

* clarity
* stability
* composability
* testability

---

# Why this improves your workflow

Without this file:

Copilot acts like a **generic Python assistant**.

With this file:

Copilot acts like a **developer inside the RQM Technologies architecture**.

That makes a huge difference.

---

# Where to put it

Add this file to **every QSP repository root**:

```
AI_ENGINEERING_GUIDE.md
```

And reference it in `AGENTS.md`.

This doctrine is meant to be replicated across the QSP ecosystem, not only in `qsp-core`. The current rollout target is:

- `qsp-core`
- `qsp-fft`
- `qsp-filter`
- `qsp-modulation`
- `qsp-orientation`

Each repository should carry this shared baseline guide plus a repo-local `AGENTS.md` that defines its own boundaries, priorities, and exceptions.

---

# Your repo stack now

Right now you already have a surprisingly strong foundation:

```
qsp-core
qsp-fft
qsp-filter
qsp-modulation
qsp-orientation
```

That is already **a real platform**.

The documentation alignment we discussed will make it **much easier for AI and future contributors to extend correctly**.
