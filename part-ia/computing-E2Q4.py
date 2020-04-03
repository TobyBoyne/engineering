import numpy as np
import matplotlib.pyplot as plt

# TODO: look at error for x=10000

def f(x):
	return x ** 2 * np.sin(x ** 2)

def df(x):
	return 2 * x * np.sin(x ** 2) + 2 * x ** 3 * np.cos(x ** 2)

def complex_step(x, h):
	return f(x + 1j * h).imag / h

if __name__ == "__main__":
	xs = 10 ** np.arange(1, 5)
	hs = 10.0 ** np.arange(-9, -16, -3)
	rel_error = np.zeros((4, 3))

	fig, ax = plt.subplots()
	ax.tick_params(
		axis='x',
		labelbottom=False
	)
	plt.subplots_adjust(left=0.2, bottom=0.3)

	for i, x in enumerate(xs):
		r = abs((complex_step(x, hs) - df(x)) / df(x))
		rel_error[i, :] = r
		ax.loglog(hs[::-1], r)

	ax.legend(xs)
	print(complex_step(10000, 1e-15))
	print(df(xs))
	for x in xs:
		print(x, df(x))
	# print(complex_step(10000, 1e-9) - df(10000))


	plt.table(rel_error, loc='bottom',
			  rowLabels=xs, colLabels=hs)
	plt.show()