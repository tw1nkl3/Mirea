import numpy as np
import pandas as pd

""" matrix = []
for i in range(8):
    row = []
    for j in range(8):
        if (i+j) % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for row in matrix:
    print(row)"""


""" matrix = np.arange(0, 5, 1)[:, np.newaxis] + np.arange(0, 5, 1)
print(matrix) """


""" matrix = np.arange(5).reshape(1,5) + np.zeros((5,5))
print(matrix) """


""" arr = np.random.rand(3, 3, 3)
print(arr) """


""" matrix = np.zeros((5, 5))

matrix[0, :] = 1
matrix[-1, :] = 1
matrix[:, 0] = 1
matrix[:, -1] = 1

print(matrix) """

""" arr = np.random.rand(10)
print(sorted(arr)) """


""" matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Форма матрицы:", matrix.shape)
print("Размер матрицы:", matrix.size)
print("Размерность матрицы:", matrix.ndim)"""


""" a = pd.Series([1, 2, 3])
b = pd.Series([4, 5, 6])

distance = np.sqrt(np.sum((a.values - b.values)**2))
print(distance) """


""" url = 'https://raw.githubusercontent.com/akmand/datasets/master/nba-player-stats-19_20.csv'
df = pd.read_csv(url)

print(df.head()) """


