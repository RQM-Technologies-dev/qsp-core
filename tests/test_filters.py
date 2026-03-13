import unittest

from qsp.filters import clip, moving_average, normalize_signal


class FilterTests(unittest.TestCase):
    def test_moving_average(self) -> None:
        self.assertEqual([2.0, 3.0, 4.0], moving_average([1, 2, 3, 4, 5], 3))

    def test_moving_average_invalid_window(self) -> None:
        with self.assertRaises(ValueError):
            moving_average([1, 2], 0)
        with self.assertRaises(ValueError):
            moving_average([1, 2], 3)

    def test_clip(self) -> None:
        self.assertEqual([-1.0, 0.5, 1.0], clip([-2, 0.5, 3], -1, 1))

    def test_normalize_signal(self) -> None:
        self.assertEqual([-0.5, 1.0, -0.25], normalize_signal([-2, 4, -1]))
        self.assertEqual([0.0, 0.0], normalize_signal([0, 0]))


if __name__ == "__main__":
    unittest.main()
