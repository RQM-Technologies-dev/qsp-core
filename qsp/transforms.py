"""Baseline transform helpers for the qsp-core foundation layer."""

from __future__ import annotations

import cmath
import math

from .utils import ensure_complex_sequence


def validate_transform_input(values: list[complex] | tuple[complex, ...]) -> tuple[complex, ...]:
    """Validate and coerce transform input into a tuple of complex values."""
    return ensure_complex_sequence(values, name="values", allow_empty=True)


def dft(values: list[complex] | tuple[complex, ...]) -> list[complex]:
    """Compute a simple O(n^2) discrete Fourier transform.

    This is a small reference implementation for qsp-core. More advanced
    transform work should live in qsp-fft.
    """
    samples = validate_transform_input(values)
    count = len(samples)
    if count == 0:
        return []

    output: list[complex] = []
    for k in range(count):
        total = 0j
        for n, sample in enumerate(samples):
            angle = -2j * math.pi * k * n / count
            total += sample * cmath.exp(angle)
        output.append(total)
    return output


def idft(values: list[complex] | tuple[complex, ...]) -> list[complex]:
    """Compute the inverse discrete Fourier transform matching :func:`dft`."""
    spectrum = validate_transform_input(values)
    count = len(spectrum)
    if count == 0:
        return []

    output: list[complex] = []
    for n in range(count):
        total = 0j
        for k, sample in enumerate(spectrum):
            angle = 2j * math.pi * k * n / count
            total += sample * cmath.exp(angle)
        output.append(total / count)
    return output
