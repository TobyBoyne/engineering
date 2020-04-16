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
	hs = 10.0 ** np.arange(-5, -10, -1)
	x = 100
	fig, (ax1, ax2) = plt.subplots(1, 2)
	exact = df(x)
	for func, ax in ((one_sided, ax1), (symmetric, ax2)):
		line = np.abs(np.array([func(x, h) for h in hs]) - exact)
		ax.loglog(hs, line, label=func.__name__)
		# show decreasing h to the right
		ax.invert_xaxis()
		ax.legend()
		ax.set_xlabel("h")

	plt.show()