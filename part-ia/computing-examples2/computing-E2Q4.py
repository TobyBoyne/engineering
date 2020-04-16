import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return x ** 2 * np.sin(x ** 2)

def df(x):
	return 2 * x * np.sin(x ** 2) + 2 * x ** 3 * np.cos(x ** 2)

def complex_step(x, h):
	return f(x + 1j * h).imag / h

def symmetric(x, h):
	return (f(x + h) - f(x - h)) / (2 * h)

def run(approx_func):
	xs = 10 ** np.arange(1, 5)
	hs = 10.0 ** np.arange(-9, -16, -3)
	rel_error = np.zeros((len(xs), len(hs)))

	fig, ax = plt.subplots()
	ax.set_title(f"Relative error of {approx_func.__name__} compared to exact derivative")
	ax.set_ylabel("Relative error")
	ax.tick_params(
		axis='x',
		labelbottom=False,
		which='both',
		bottom=False
	)
	plt.subplots_adjust(bottom=0.3)

	for i, x in enumerate(xs):
		r = np.abs((approx_func(x, hs) - df(x)) / df(x))
		rel_error[i, :] = r
		ax.loglog(hs[::-1], r)

	ax.legend([f"x={x}" for x in xs])

	plt.table(rel_error, loc='bottom',
			  rowLabels=xs, colLabels=hs)
	plt.savefig(f"images/comp-E2Q4-{approx_func.__name__}")
	plt.show()

if __name__ == "__main__":
	run(approx_func=complex_step)
	run(approx_func=symmetric)