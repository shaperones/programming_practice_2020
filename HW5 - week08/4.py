import numpy as np

n = np.random.randint(10, 101)  # случайный порядок матрицы
ranmatr = np.random.randint(n, size=(n, n))  # рандомная матрица n*n
print(ranmatr)

m = np.max(ranmatr)  # считаю макс и сумму
s = np.sum(ranmatr)
print(m, ' ', s)

ranmatr = ranmatr / np.max(ranmatr)  # делю на макс
print(ranmatr)

ranmatr = ranmatr - np.mean(ranmatr, axis=1)  # вычитаю среднее по строке
print(ranmatr)

ranmatr[ranmatr == m] = -1   # меняю максимальное значение на -1
print(ranmatr)