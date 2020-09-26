import numpy as np


def ufff(x):
    res = np.log(np.e ** (1 / (np.sin(x) + 1)) / (5 / 4 + 1 / x ** 15)) / np.log(1 + x ** 2)
    return res


a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
    print(ufff(a[i]))
# ввод - в 1 строку через пробел, выводит каждое занчение с новой строки
