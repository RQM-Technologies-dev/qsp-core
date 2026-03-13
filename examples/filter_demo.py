"""Simple filtering utilities example."""

from qsp.filters import clip, moving_average, normalize_signal


if __name__ == "__main__":
    signal = [0.0, 2.0, 4.0, 6.0, 8.0]

    print("signal:", signal)
    print("moving average:", moving_average(signal, 3))
    print("clipped:", clip(signal, 1.0, 5.0))
    print("normalized:", normalize_signal(signal))
