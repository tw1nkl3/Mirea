def ham_dist(num1, num2):
    return bin(num1 ^ num2).count('1')
