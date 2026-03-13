"""Small internal helpers shared across qsp-core modules."""

from __future__ import annotations

from numbers import Real
from typing import Iterable


def ensure_real_number(value: Real, *, name: str) -> float:
    """Return ``value`` as a float when it is a real number."""
    if not isinstance(value, Real):
        raise TypeError(f"{name} must be a real number")
    return float(value)


def ensure_complex_sequence(values: Iterable[complex], *, name: str, allow_empty: bool = False) -> tuple[complex, ...]:
    """Return ``values`` as a tuple of complex numbers."""
    try:
        items = tuple(complex(value) for value in values)
    except TypeError as error:
        raise TypeError(f"{name} must be an iterable of numeric values") from error

    if not allow_empty and not items:
        raise ValueError(f"{name} must not be empty")
    return items


def ensure_real_sequence(values: Iterable[Real], *, name: str, allow_empty: bool = False) -> tuple[float, ...]:
    """Return ``values`` as a tuple of floats."""
    try:
        items = tuple(ensure_real_number(value, name=name) for value in values)
    except TypeError as error:
        raise TypeError(f"{name} must be an iterable of real numbers") from error

    if not allow_empty and not items:
        raise ValueError(f"{name} must not be empty")
    return items


def approx_equal(left: complex, right: complex, *, tolerance: float = 1e-9) -> bool:
    """Return ``True`` when two numeric values are within ``tolerance``."""
    return abs(left - right) <= tolerance
