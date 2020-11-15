import numpy as np
import time
from random import randint
import matplotlib.pyplot as plt

n = np.random.randint(200)


def python1():
    start = time.time()
    x = randint(0, 100)
    y = randint(-50, 50)
    z = 2 * x ** 2 + 4 * y
    return time.time() - start


def numpy1():
    start = time.time()
    x = np.random.randint(0, 100)
    y = np.random.randint(-50, 50)
    z = 2 * x ** 2 + 4 * y
    return time.time() - start


def python2():
    start = time.time()
    x = [[randint(0, 100) for k in range(n)] for l in range(n)]
    y = [[randint(-50, 50) for k in range(n)] for l in range(n)]
    z = [[0 for k in range(n)] for l in range(n)]
    for i in range(n):
        for j in range(n):
            el = 0
            for k in range(n):
                el += x[i][k] * y[k][j]
                z[i][j] = el
    return time.time() - start


def numpy2():
    start = time.time()
    x = np.random.randint(100, size=n * n).reshape(n, n)
    y = np.random.randint(-50, 50, size=n * n).reshape(n, n)
    z = x * y
    return time.time() - start


t = np.arange(0, 1, 0.01)
y1 = python1()
y2 = python2()
y3 = numpy1()
y4 = numpy2()
plt.plot(t, y1, 'b', t, y2, 'r', t, y3, 'g', t, y4, '-r')
plt.show()
