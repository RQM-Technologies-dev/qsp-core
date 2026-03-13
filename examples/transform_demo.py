"""Simple DFT and IDFT example."""

from qsp.transforms import dft, idft


if __name__ == "__main__":
    signal = [1, 2, 3, 4]
    spectrum = dft(signal)
    restored = idft(spectrum)

    print("signal:", signal)
    print("spectrum:", spectrum)
    print("restored:", restored)
