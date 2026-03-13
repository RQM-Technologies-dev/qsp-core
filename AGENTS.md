# RQM Technologies – Agent Instructions

This repository is the foundation of the RQM Technologies ecosystem.

## Role of this repository

`qsp-core` contains the base Quaternionic Signal Processing primitives used by all other RQM Technologies projects.

It must remain:

- small
- modular
- pure Python
- dependency-light
- mathematically clear

This repo provides the shared math utilities that downstream repositories depend on.
Downstream repositories should import shared quaternion, SU(2), transform, and filtering primitives from `qsp-core` instead of reimplementing that foundation logic locally.

## Ecosystem architecture

The full RQM Technologies ecosystem is structured as:

RQM-Technologies

qsp-core
qsp-fft
qsp-filter
qsp-modulation

eigenclock
quaternionic-modem
quaternionic-navigation

website
documentation
research-notebooks

### Layer 1 – Core math libraries

These repositories implement reusable quaternionic signal processing primitives.

- qsp-core (this repo)
- qsp-fft
- qsp-filter
- qsp-modulation

### Layer 2 – Applications

These repositories implement domain systems built on QSP.

- eigenclock
- quaternionic-modem
- quaternionic-navigation

### Layer 3 – Public interface

These repositories provide public-facing material.

- website
- documentation
- research-notebooks

## Rules for agents

When making changes to this repository:

1. Do not add UI code.
2. Do not add deployment code.
3. Do not add website content.
4. Keep functions small and testable.
5. Prefer pure Python.
6. Avoid unnecessary dependencies.
7. When functionality changes, update README and docs.

## Repository structure

The expected structure for this repository is:

qsp/
tests/
examples/
docs/

## Immediate priorities

Agents working in this repository should focus on:

- quaternion math utilities
- SU(2) utilities
- spectral transforms
- signal filters

All functionality should be reusable by downstream repositories.
