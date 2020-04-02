from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

T = np.pi
n = np.arange(1, 7)



d = T / (2 * np.pi)
a = 1 / (np.pi * n) * np.sin(n * T)
b = 1 / (np.pi * n) * (1 - np.cos(n * T))

def f(t):
	return sum(a * np.cos(n * t)) + sum(b * np.sin(n * t)) + d

x = np.linspace(-5, 10, 1000)
y = np.array([f(i) for i in x])
plt.plot(x, y)
plt.vlines((np.pi, 2 *np.pi), 1, -1)
plt.hlines((0, 1), -5, 10)
plt.show()