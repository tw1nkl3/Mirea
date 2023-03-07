import math


def main(y):
    if y < 4:
        return 82*(1 + y ** 3) ** 2 + 47 * (26 * y) ** 4
    elif 4 <= y < 19:
        return y / 93
    else:
        return 97 * (5 * y) ** 6 - 3
