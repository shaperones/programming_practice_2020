import numpy as np


def fill_gaps(a):
    if np.all(np.isnan(a)):  # если ол из нан, то все из ноль
        a[:] = 0
    else:
        a[np.isnan(a)] = a[~np.isnan(a)].mean()  # оказывается, среднее можно посчитать в обход нанов
    return a


# примеры работы
matrix = np.array([1, 2, 3, 0, 8, np.nan])
badmatrix = np.array([np.nan, np.nan, np.nan, np.nan, np.nan, np.nan])
print(fill_gaps(matrix))
print(fill_gaps(badmatrix))
