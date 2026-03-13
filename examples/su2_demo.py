"""Quaternion normalization and SU(2) conversion example."""

from qsp.quaternion import Quaternion
from qsp.su2 import quaternion_to_su2, su2_to_quaternion


if __name__ == "__main__":
    quaternion = Quaternion(0, 3, 0, 4).normalize()
    matrix = quaternion_to_su2(quaternion)
    recovered = su2_to_quaternion(matrix)

    print("unit quaternion:", quaternion)
    print("su2 matrix:", matrix)
    print("recovered quaternion:", recovered)
