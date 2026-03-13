import unittest

from qsp.quaternion import Quaternion
from qsp.su2 import (
    is_unit_quaternion,
    matrix_trace,
    normalize_quaternion,
    quaternion_to_su2,
    su2_to_quaternion,
)


class Su2Tests(unittest.TestCase):
    def test_normalize_quaternion_and_unit_check(self) -> None:
        quaternion = normalize_quaternion((0, 3, 0, 4))

        for expected, actual in zip((0.0, 0.6, 0.0, 0.8), quaternion.to_tuple()):
            self.assertAlmostEqual(expected, actual, places=9)
        self.assertTrue(is_unit_quaternion(quaternion))
        self.assertFalse(is_unit_quaternion((1, 1, 0, 0)))

    def test_quaternion_to_su2_and_back(self) -> None:
        quaternion = Quaternion(0, 1, 0, 0)

        matrix = quaternion_to_su2(quaternion)
        recovered = su2_to_quaternion(matrix)

        self.assertEqual((1j, 0j), matrix[0])
        self.assertEqual((-0j, -1j), matrix[1])
        self.assertEqual((0.0, 1.0, 0.0, 0.0), recovered.to_tuple())

    def test_matrix_trace(self) -> None:
        matrix = ((1 + 2j, 0j), (0j, 3 - 1j))

        self.assertEqual((4 + 1j), matrix_trace(matrix))

    def test_invalid_su2_shape_raises(self) -> None:
        with self.assertRaises(ValueError):
            matrix_trace(((1 + 0j,),))

    def test_invalid_su2_form_raises(self) -> None:
        with self.assertRaises(ValueError):
            su2_to_quaternion(((1 + 0j, 1 + 0j), (1 + 0j, 1 + 0j)))


if __name__ == "__main__":
    unittest.main()
