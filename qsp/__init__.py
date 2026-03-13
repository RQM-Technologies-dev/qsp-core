"""Shared Quaternionic Signal Processing primitives for RQM Technologies.

The top-level package exports the small, stable foundation API that downstream
repositories are expected to import directly. Lower-level validation helpers
remain available from their module namespaces.
"""

from .filters import clip, moving_average, normalize_signal
from .quaternion import Quaternion
from .su2 import (
    is_unit_quaternion,
    matrix_trace,
    normalize_quaternion,
    quaternion_to_su2,
    su2_to_quaternion,
)
from .transforms import dft, idft

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
]
