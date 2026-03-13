"""Quaternion primitives used throughout qsp-core."""

from __future__ import annotations

import math
from typing import Iterable

from .utils import ensure_real_number


class Quaternion:
    """A small, explicit quaternion value type."""

    def __init__(self, w: float, x: float, y: float, z: float) -> None:
        self.w = ensure_real_number(w, name="w")
        self.x = ensure_real_number(x, name="x")
        self.y = ensure_real_number(y, name="y")
        self.z = ensure_real_number(z, name="z")

    def __repr__(self) -> str:
        return (
            f"Quaternion(w={self.w!r}, x={self.x!r}, "
            f"y={self.y!r}, z={self.z!r})"
        )

    @classmethod
    def from_iterable(cls, values: Iterable[float]) -> "Quaternion":
        """Create a quaternion from four ordered values."""
        items = tuple(values)
        if len(items) != 4:
            raise ValueError("Quaternion.from_iterable expects exactly four values")
        return cls(*items)

    def to_tuple(self) -> tuple[float, float, float, float]:
        """Return the quaternion as a 4-tuple."""
        return (self.w, self.x, self.y, self.z)

    def norm(self) -> float:
        """Return the Euclidean norm of the quaternion."""
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    def conjugate(self) -> "Quaternion":
        """Return the quaternion conjugate."""
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def add(self, other: "Quaternion") -> "Quaternion":
        """Return the component-wise sum of two quaternions."""
        other_quaternion = self._coerce_other(other)
        return Quaternion(
            self.w + other_quaternion.w,
            self.x + other_quaternion.x,
            self.y + other_quaternion.y,
            self.z + other_quaternion.z,
        )

    def subtract(self, other: "Quaternion") -> "Quaternion":
        """Return the component-wise difference of two quaternions."""
        other_quaternion = self._coerce_other(other)
        return Quaternion(
            self.w - other_quaternion.w,
            self.x - other_quaternion.x,
            self.y - other_quaternion.y,
            self.z - other_quaternion.z,
        )

    def scalar_multiply(self, scalar: float) -> "Quaternion":
        """Multiply the quaternion by a real scalar."""
        factor = ensure_real_number(scalar, name="scalar")
        return Quaternion(
            self.w * factor,
            self.x * factor,
            self.y * factor,
            self.z * factor,
        )

    def multiply(self, other: "Quaternion") -> "Quaternion":
        """Return the Hamilton product of two quaternions."""
        other_quaternion = self._coerce_other(other)
        w1, x1, y1, z1 = self.to_tuple()
        w2, x2, y2, z2 = other_quaternion.to_tuple()
        return Quaternion(
            w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
            w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
            w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
            w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
        )

    def normalize(self) -> "Quaternion":
        """Return a unit-length copy of the quaternion."""
        magnitude = self.norm()
        if magnitude == 0.0:
            raise ValueError("Cannot normalize a zero quaternion")
        return self.scalar_multiply(1.0 / magnitude)

    @staticmethod
    def _coerce_other(other: "Quaternion") -> "Quaternion":
        if not isinstance(other, Quaternion):
            raise TypeError("Expected a Quaternion instance")
        return other
