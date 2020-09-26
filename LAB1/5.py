import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
p, v = np.polyfit(x, y, deg=int(input()), cov=True)
p_f = np.poly1d(p)
x = np.arange(0.9, 5.01, 0.01)
plt.plot(x, p_f(x))
plt.grid()
plt.show()
# ввод - степень многочлена, вывод - график с аппроксимационной кривой и точками с заданными погрешностями
