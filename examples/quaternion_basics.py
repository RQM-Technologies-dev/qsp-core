"""Basic quaternion operations in qsp-core."""

from qsp.quaternion import Quaternion


if __name__ == "__main__":
    first = Quaternion(1, 2, 3, 4)
    second = Quaternion(0, 1, 0, 0)

    print("first:", first)
    print("second:", second)
    print("sum:", first.add(second))
    print("product:", first.multiply(second))
    print("normalized first:", first.normalize())
