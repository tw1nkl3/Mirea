import math


def main(y, z, x):
    a = 87 * math.cos((x ** 3 / 48) - (28 * z) - 90) ** 5 - \
        41*((46 + (79 * z**3) + 65 * y)**7)
    b = (y ** 7) + (math.atan((55 * z ** 2) + (x ** 3) + 1) / 11)
    c = 4 * ((math.ceil((19 * z) - (x ** 3) - (80 * y ** 2))) ** 5)
    return a / b - c

print(main(-0.69, -0.2, -0.72))