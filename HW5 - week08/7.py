import numpy as np
a = np.arange(12).reshape(3, 4)
b = np.arange(25).reshape(5, 5)
np.save('file_folder', a)
c = np.load('file_folder.npy')
print(c)