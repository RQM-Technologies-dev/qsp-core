import unittest

from qsp.utils import approx_equal, ensure_complex_sequence, ensure_real_number, ensure_real_sequence


class UtilsTests(unittest.TestCase):
    def test_ensure_real_number(self) -> None:
        self.assertEqual(3.0, ensure_real_number(3, name="value"))
        with self.assertRaises(TypeError):
            ensure_real_number("bad", name="value")

    def test_ensure_real_sequence(self) -> None:
        self.assertEqual((1.0, 2.0), ensure_real_sequence([1, 2], name="values"))
        with self.assertRaises(ValueError):
            ensure_real_sequence([], name="values")

    def test_ensure_complex_sequence(self) -> None:
        self.assertEqual((1 + 0j, 2 + 0j), ensure_complex_sequence([1, 2], name="values"))
        with self.assertRaises(ValueError):
            ensure_complex_sequence([], name="values")

    def test_approx_equal(self) -> None:
        self.assertTrue(approx_equal(1.0, 1.0 + 1e-10))
        self.assertFalse(approx_equal(1.0, 1.1))


if __name__ == "__main__":
    unittest.main()
