import numpy as np


def chess(n):
    m = np.zeros((n, n))
    m[1::2, ::2] = 1
    m[::2, 1::2] = 1
    return m


n = int(input())
print(chess(n))