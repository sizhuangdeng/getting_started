from numpy import *
import numpy as np

import matplotlib.pyplot as plt

a1 = matrix('1.06, 2.23, 3.58;20.09, 5.87, 9.12')
print(a1[0, 1])
print(a1[1, 2])
print(np.max(a1[:, 2]))
print(a1.shape)


plt.plot([1, 2, 3, 4], [1, 2, 7, 14])
plt.axis([0, 6, 0, 20])
plt.show()
