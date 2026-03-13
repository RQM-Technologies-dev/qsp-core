import math
import unittest

from qsp.quaternion import Quaternion


class QuaternionTests(unittest.TestCase):
    def test_to_tuple_and_repr(self) -> None:
        quaternion = Quaternion(1, 2, 3, 4)

        self.assertEqual((1.0, 2.0, 3.0, 4.0), quaternion.to_tuple())
        self.assertIn("Quaternion", repr(quaternion))

    def test_norm_and_conjugate(self) -> None:
        quaternion = Quaternion(1, 2, 2, 1)

        self.assertTrue(math.isclose(quaternion.norm(), 3.1622776601683795))
        self.assertEqual((1.0, -2.0, -2.0, -1.0), quaternion.conjugate().to_tuple())

    def test_add_subtract_and_scalar_multiply(self) -> None:
        first = Quaternion(1, 2, 3, 4)
        second = Quaternion(0.5, -1, 2, 0)

        self.assertEqual((1.5, 1.0, 5.0, 4.0), first.add(second).to_tuple())
        self.assertEqual((0.5, 3.0, 1.0, 4.0), first.subtract(second).to_tuple())
        self.assertEqual((2.0, 4.0, 6.0, 8.0), first.scalar_multiply(2).to_tuple())

    def test_hamilton_product(self) -> None:
        first = Quaternion(1, 2, 3, 4)
        second = Quaternion(5, 6, 7, 8)

        self.assertEqual((-60.0, 12.0, 30.0, 24.0), first.multiply(second).to_tuple())

    def test_normalize_and_from_iterable(self) -> None:
        quaternion = Quaternion.from_iterable([0, 3, 0, 4]).normalize()

        for expected, actual in zip((0.0, 0.6, 0.0, 0.8), quaternion.to_tuple()):
            self.assertAlmostEqual(expected, actual, places=9)
        self.assertTrue(math.isclose(quaternion.norm(), 1.0))

    def test_normalize_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            Quaternion(0, 0, 0, 0).normalize()


if __name__ == "__main__":
    unittest.main()
