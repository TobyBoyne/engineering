import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 4, 0.1)
y = np.arange(-2, 4, 0.1)

X, Y = np.meshgrid(x, y)
Z = X*Y*(2 - X - 2*Y)

p = plt.contour(X, Y, Z, np.arange(-1, 1, 0.1))
plt.rc('figure', figsize=(10,10))
plt.savefig('maths-E10Q8-contour')
plt.show()