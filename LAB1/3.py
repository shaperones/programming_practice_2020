import numpy as np
import matplotlib.pyplot as plt


def y(x):
    res = np.log((x*x + 1)*np.exp(-1*abs(x)/10))/np.log(1 + np.tan(1/(1 + (np.sin(x))**2)))
    return res


x = np.arange(-50, 50.01, 0.1)
plt.plot(x, y(x))
plt.grid(True)
plt.show()