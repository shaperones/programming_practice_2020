import numpy as np
import matplotlib.pyplot as plt


def y(x):
    res = x * x - x - 6
    return res


x = np.arange(-3, 4.01, 0.01)
plt.plot(x, y(x))
plt.grid(True)
plt.show()
