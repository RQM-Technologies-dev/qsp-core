import unittest

from qsp.transforms import dft, idft, validate_transform_input


class TransformTests(unittest.TestCase):
    def test_validate_transform_input(self) -> None:
        self.assertEqual((1 + 0j, 2 + 0j), validate_transform_input([1, 2]))
        self.assertEqual((), validate_transform_input([]))

    def test_dft_known_values(self) -> None:
        result = dft([1, 0, 0, 0])

        self.assertEqual([1 + 0j, 1 + 0j, 1 + 0j, 1 + 0j], result)

    def test_dft_idft_round_trip(self) -> None:
        signal = [1, 2, 3, 4]

        restored = idft(dft(signal))

        for expected, actual in zip(signal, restored):
            self.assertAlmostEqual(expected, actual.real, places=9)
            self.assertAlmostEqual(0.0, actual.imag, places=9)


if __name__ == "__main__":
    unittest.main()
