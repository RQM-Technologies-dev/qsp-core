"""Minimal SU(2) helpers built on top of quaternions."""

from __future__ import annotations

from collections.abc import Iterable

from .quaternion import Quaternion
from .utils import approx_equal

Matrix2x2 = tuple[tuple[complex, complex], tuple[complex, complex]]


def normalize_quaternion(value: Quaternion | Iterable[float]) -> Quaternion:
    """Return a normalized quaternion from a quaternion or four real values."""
    return _coerce_quaternion(value).normalize()


def is_unit_quaternion(value: Quaternion | Iterable[float], *, tolerance: float = 1e-9) -> bool:
    """Return ``True`` when a quaternion has unit norm within ``tolerance``."""
    quaternion = _coerce_quaternion(value)
    return approx_equal(quaternion.norm(), 1.0, tolerance=tolerance)


def quaternion_to_su2(value: Quaternion | Iterable[float]) -> Matrix2x2:
    """Convert a unit quaternion into the corresponding SU(2) matrix."""
    quaternion = normalize_quaternion(value)
    a = complex(quaternion.w, quaternion.x)
    b = complex(quaternion.y, quaternion.z)
    return (
        (a, b),
        (-b.conjugate(), a.conjugate()),
    )


def su2_to_quaternion(matrix: Matrix2x2, *, tolerance: float = 1e-9) -> Quaternion:
    """Convert an SU(2)-form 2x2 matrix back into a unit quaternion."""
    _validate_matrix_shape(matrix)
    a = complex(matrix[0][0])
    b = complex(matrix[0][1])
    lower_left = complex(matrix[1][0])
    lower_right = complex(matrix[1][1])

    if not approx_equal(lower_left, -b.conjugate(), tolerance=tolerance):
        raise ValueError("matrix is not in the expected SU(2) form")
    if not approx_equal(lower_right, a.conjugate(), tolerance=tolerance):
        raise ValueError("matrix is not in the expected SU(2) form")

    return Quaternion(a.real, a.imag, b.real, b.imag).normalize()


def matrix_trace(matrix: Matrix2x2) -> complex:
    """Return the trace of a 2x2 matrix."""
    _validate_matrix_shape(matrix)
    return complex(matrix[0][0]) + complex(matrix[1][1])


def _validate_matrix_shape(matrix: Matrix2x2) -> None:
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("matrix must be a 2x2 structure")


def _coerce_quaternion(value: Quaternion | Iterable[float]) -> Quaternion:
    """Return ``value`` as a :class:`Quaternion` instance."""
    if isinstance(value, Quaternion):
        return value
    return Quaternion.from_iterable(value)
