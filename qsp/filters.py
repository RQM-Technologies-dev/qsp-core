"""Small filtering helpers intended for reuse across QSP projects."""

from __future__ import annotations

from collections.abc import Iterable

from .utils import ensure_real_number, ensure_real_sequence


def validate_signal(values: Iterable[float], *, allow_empty: bool = True) -> tuple[float, ...]:
    """Validate a real-valued signal and return it as a tuple of floats."""
    return ensure_real_sequence(values, name="values", allow_empty=allow_empty)


def moving_average(values: Iterable[float], window_size: int) -> list[float]:
    """Return the sliding-window moving average for a real-valued signal."""
    signal = validate_signal(values)
    if not isinstance(window_size, int) or window_size <= 0:
        raise ValueError("window_size must be a positive integer")
    if not signal:
        return []
    if window_size > len(signal):
        raise ValueError("window_size must not exceed the signal length")

    return [
        sum(signal[index : index + window_size]) / window_size
        for index in range(len(signal) - window_size + 1)
    ]


def clip(values: Iterable[float], minimum: float, maximum: float) -> list[float]:
    """Clip each signal sample to the inclusive range ``[minimum, maximum]``."""
    signal = validate_signal(values)
    lower = ensure_real_number(minimum, name="minimum")
    upper = ensure_real_number(maximum, name="maximum")
    if lower > upper:
        raise ValueError("minimum must be less than or equal to maximum")
    return [min(max(sample, lower), upper) for sample in signal]


def normalize_signal(values: Iterable[float]) -> list[float]:
    """Scale a signal so its maximum absolute value becomes one."""
    signal = validate_signal(values)
    if not signal:
        return []

    peak = max(abs(sample) for sample in signal)
    if peak == 0.0:
        return [0.0 for _ in signal]
    return [sample / peak for sample in signal]
