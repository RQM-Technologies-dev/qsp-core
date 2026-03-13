import unittest

import qsp


class PackageApiTests(unittest.TestCase):
    def test_top_level_api_is_intentional(self) -> None:
        expected_exports = {
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
        }

        self.assertEqual(expected_exports, set(qsp.__all__))
        self.assertFalse(hasattr(qsp, "validate_signal"))
        self.assertFalse(hasattr(qsp, "validate_transform_input"))

    def test_internal_helpers_do_not_leak_into_top_level_api(self) -> None:
        internal_names = {
            "approx_equal",
            "ensure_complex_sequence",
            "ensure_real_number",
            "ensure_real_sequence",
        }

        for name in internal_names:
            with self.subTest(name=name):
                self.assertFalse(hasattr(qsp, name))


if __name__ == "__main__":
    unittest.main()
