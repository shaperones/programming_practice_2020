import numpy as np
p = np.array(['у ', 'лукоморья ', 'дуб ', 'зеленый, ', 'златая ', 'цепь ', 'на ', 'дубе ', 'том'])
n = np.array(['у ', 'лукоморья ', 'дуб ', 'срубили, ', 'кота ', 'на ', 'мясо ', 'порубили '])
i = len(np.setdiff1d(n, p))/len(n)  # та самая функция, удаляющая совпадения, оценивает оригинальность текста
print(i)
