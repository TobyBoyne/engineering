import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return (x + 2) ** 4

def df(x, h=None):
	return 4 * (x + 2) ** 3

def one_sided(x, h):
	return (f(x + h) - f(x)) / h

def symmetric(x, h):
	return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == "__main__":
	h_powers = np.arange(5)
	hs = 10.0 ** (-h_powers)
	x = 100
	for func in (df, one_sided, symmetric):
		line = np.array([func(x, h) for h in hs])
		plt.plot(h_powers, line)

	plt.legend(("Real derivative", "One sided", "Symmetric"))
	plt.xlabel("-log(h)")
	plt.show()