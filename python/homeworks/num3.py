def main(m, a, b):
    result = 0
    for j in range(1, b+1):
        for k in range(1, a+1):
            for c in range(1, m+1):
                term = 54 + 3 * (92 * c ** 2 + 14 * j ** 3) + 50 * k ** 7
                result += term
    return result

print(main(2, 2, 3))