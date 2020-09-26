import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.01)
y = input()
with plt.xkcd():
    plt.plot(eval(y))
    plt.show()
