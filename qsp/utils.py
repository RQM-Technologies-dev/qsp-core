"""Small shared helpers used across qsp-core modules."""

from __future__ import annotations

from numbers import Real
from typing import Iterable, TypeVar

T = TypeVar("T")


def ensure_real_number(value: Real, *, name: str) -> float:
    """Return *value* as a float when it is a real number."""
    if not isinstance(value, Real):
        raise TypeError(f"{name} must be a real number")
    return float(value)


def ensure_complex_sequence(values: Iterable[complex], *, name: str, allow_empty: bool = False) -> tuple[complex, ...]:
    """Convert *values* into a tuple of complex numbers."""
    try:
        items = tuple(complex(value) for value in values)
    except TypeError as error:
        raise TypeError(f"{name} must be an iterable of numeric values") from error

    if not allow_empty and not items:
        raise ValueError(f"{name} must not be empty")
    return items


def ensure_real_sequence(values: Iterable[Real], *, name: str, allow_empty: bool = False) -> tuple[float, ...]:
    """Convert *values* into a tuple of floats."""
    try:
        items = tuple(ensure_real_number(value, name=name) for value in values)
    except TypeError as error:
        raise TypeError(f"{name} must be an iterable of real numbers") from error

    if not allow_empty and not items:
        raise ValueError(f"{name} must not be empty")
    return items


def approx_equal(left: complex, right: complex, *, tolerance: float = 1e-9) -> bool:
    """Return True when two numeric values are within *tolerance* of each other."""
    return abs(left - right) <= tolerance


def pairwise_sum(values: Iterable[T], *, start: T) -> T:
    """Accumulate values from left to right without importing extra helpers."""
    total = start
    for value in values:
        total += value
    return total
