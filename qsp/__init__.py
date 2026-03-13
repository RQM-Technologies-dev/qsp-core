"""Shared Quaternionic Signal Processing primitives for RQM Technologies."""

from .filters import clip, moving_average, normalize_signal, validate_signal
from .quaternion import Quaternion
from .su2 import (
    is_unit_quaternion,
    matrix_trace,
    normalize_quaternion,
    quaternion_to_su2,
    su2_to_quaternion,
)
from .transforms import dft, idft, validate_transform_input

__all__ = [
    "Quaternion",
    "clip",
    "dft",
    "idft",
    "is_unit_quaternion",
    "matrix_trace",
    "moving_average",
    "normalize_quaternion",
    "normalize_signal",
    "quaternion_to_su2",
    "su2_to_quaternion",
    "validate_signal",
    "validate_transform_input",
]
