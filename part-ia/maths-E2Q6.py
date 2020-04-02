# maths examples2 question6

import matplotlib.pyplot as plt
import numpy as np

def f(x):
	y = (1+x) / (1 - x**2)
	y[np.abs(y) > 20] = np.nan
	return y

x = np.linspace(-5, 5, num=10000)
ys_f = f(x)
ys_approx = 1 + x + x**2
line1, = plt.plot(x, ys_f)
line2, = plt.plot(x, ys_approx)
plt.legend((line1, line2), ("f(x)", "1+x+x^2"))
plt.ylim(-10, 10)
plt.grid()

# find range x where tolerance is tol
for tol in (0.1, 0.01, 0.001):
	within_tol = [x for (x, exact, approx) in zip(x, ys_f, ys_approx) if abs((exact-approx)/exact) <= tol]
	print(f"For tolerance = {tol*100}%, the range for x is\n"
		  f"{within_tol[0]} < x < {within_tol[-1]}")


plt.show()

