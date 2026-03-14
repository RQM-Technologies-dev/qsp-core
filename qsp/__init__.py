"""Shared Quaternionic Signal Processing primitives for RQM Technologies.

The top-level ``qsp`` package intentionally exposes only the small, stable
foundation surface that downstream repositories should import directly:

- quaternion primitives shared across the ecosystem
- SU(2) conversion helpers built on those primitives
- reference transforms for extension in ``qsp-fft``
- simple filtering helpers for extension in ``qsp-filter``

Lower-level validation and coercion helpers remain in their module namespaces so
that ``qsp-core`` stays explicit and dependency-like rather than absorbing
downstream-specific implementation details.
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
