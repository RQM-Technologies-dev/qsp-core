"""Small filtering helpers intended for reuse across QSP projects."""

from __future__ import annotations

from .utils import ensure_real_number, ensure_real_sequence


def validate_signal(values: list[float] | tuple[float, ...], *, allow_empty: bool = True) -> tuple[float, ...]:
    """Validate and coerce a real-valued signal into a tuple of floats."""
    return ensure_real_sequence(values, name="values", allow_empty=allow_empty)


def moving_average(values: list[float] | tuple[float, ...], window_size: int) -> list[float]:
    """Return the sliding-window moving average of *values*."""
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


def clip(values: list[float] | tuple[float, ...], minimum: float, maximum: float) -> list[float]:
    """Clip each sample in *values* to the inclusive range [minimum, maximum]."""
    signal = validate_signal(values)
    lower = ensure_real_number(minimum, name="minimum")
    upper = ensure_real_number(maximum, name="maximum")
    if lower > upper:
        raise ValueError("minimum must be less than or equal to maximum")
    return [min(max(sample, lower), upper) for sample in signal]


def normalize_signal(values: list[float] | tuple[float, ...]) -> list[float]:
    """Scale a signal so that its maximum absolute value becomes one."""
    signal = validate_signal(values)
    if not signal:
        return []

    peak = max(abs(sample) for sample in signal)
    if peak == 0.0:
        return [0.0 for _ in signal]
    return [sample / peak for sample in signal]
