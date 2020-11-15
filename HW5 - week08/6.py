import numpy as np


def norm(m):
    amax = np.max(m)
    amin = np.min(m)
    return m / max(abs(amax), abs(amin))  # min рассматриваю для случаев с отрицательными элементами


matrix = np.array([[1, 1, 1], [4, 1, -1]])  # пример работы
print(matrix)
print(norm(matrix))