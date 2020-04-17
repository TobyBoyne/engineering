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
	hs = 10.0 ** np.arange(-1, -5, -1)
	x = 2
	fig, ax = plt.subplots()
	exact = df(x)

	lines = {
		"one sided": np.abs(np.array([one_sided(x, h) for h in hs]) - exact),
		"one sided squared": np.abs(np.array([one_sided(x, h) for h in hs]) - exact) ** 2,
		"symmetric": np.abs(np.array([symmetric(x, h) for h in hs]) - exact)
	}

	for name, line in lines.items():
		ax.loglog(hs, line, label=name)

	# show decreasing h to the right
	ax.invert_xaxis()
	ax.legend()
	ax.set_xlabel("h")

	plt.show()