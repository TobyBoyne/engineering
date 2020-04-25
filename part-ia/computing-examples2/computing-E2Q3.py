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


def get_line(func):
	return np.abs(np.array([func(x, h) for h in hs]) - exact)


if __name__ == "__main__":
	hs = 10.0 ** np.arange(-1, -5, -1)
	x = 2
	fig, ax = plt.subplots()
	exact = df(x)

	ax.loglog(hs, get_line(one_sided), label="One sided")
	ax.loglog(hs, get_line(one_sided) ** 2, label="One sided squared", linestyle="--")
	ax.loglog(hs, get_line(symmetric), label="Symmetric")

	# show decreasing h to the right
	ax.invert_xaxis()
	ax.legend()
	ax.set_xlabel("h")
	fig.savefig('images/comp-E2Q3-derivativeaccuracy')
	plt.show()