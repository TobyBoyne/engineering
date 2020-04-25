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

def run(ax, approx_func):
	rel_error = np.zeros((len(xs), len(hs)), dtype=np.float64)

	ax.set_title(f'{approx_func.__name__}')
	ax.set_ylabel('Relative error')
	# ax.tick_params(
	# 	axis='x',
	# 	labelbottom=False,
	# 	which='both',
	# 	bottom=False
	# )

	for i, x in enumerate(xs):
		r = np.abs((approx_func(x, hs) - df(x)) / df(x))
		rel_error[i, :] = r
		ax.loglog(hs[::-1], r)

	ax.legend([f"x={x}" for x in xs])


	return rel_error


if __name__ == "__main__":
	xs = 10.0 ** np.arange(1, 5)
	hs = 10.0 ** np.arange(-9, -16, -3)

	fig, ((ax_complex, ax_symmetric), (table_complex, table_symmetric)) = plt.subplots(2, 2, sharey='row')
	run(ax_complex, approx_func=complex_step)
	run(ax_symmetric, approx_func=symmetric)
	plt.savefig(f"images/comp-E2Q4-comparisons")
	plt.show()