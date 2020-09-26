import numpy as np
import matplotlib.pyplot as plt


def wei(x):
    i = 0
    s = 0
    while i < 20:
        k = np.cos(np.pi * x * (a ** i))
        m = b ** i
        s += k * m
        i += 1
    return s


a = int(input('введите a - нечетное !=1  '))
b = float(input('затем 0 < b < 1  '))
x = np.arange(-5, 5, 0.0001)
plt.figure(figsize=(15, 10))
plt.plot(x, wei(x))
plt.grid(True)
plt.show()
# ввод - два числа из определения функции вейерштрассе, вывод - график
