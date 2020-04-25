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
	ax.tick_params(
		axis='x',
		labelbottom=True,
		which='minor',
		bottom=False
	)

	ax.tick_params(
		axis='y',
		labelleft=True,
		which='major',
		left=True
	)

	for i, x in enumerate(xs):
		r = np.abs((approx_func(x, hs) - df(x)) / df(x))
		rel_error[i, :] = r
		ax.loglog(hs[::-1], r)

	ax.legend([f"x={x}" for x in xs])


	return rel_error


def print_table(complex_error, symmetric_error):
	for i, h in enumerate(hs):
		print(f'For h={h}:')
		for j, x in enumerate(xs):
			print(f'At x={x}, \n\tcomplex error={complex_error[j, i]:.4e}'
				  f'\n\tsymmetric error={symmetric_error[j, i]:.4e}')


if __name__ == "__main__":
	xs = 10.0 ** np.arange(1, 5)
	hs = 10.0 ** np.arange(-9, -16, -3)

	fig, (ax_complex, ax_symmetric) = plt.subplots(1, 2, sharey='row', figsize=(10, 5))
	complex_error = run(ax_complex, approx_func=complex_step)
	symmetric_error = run(ax_symmetric, approx_func=symmetric)
	fig.tight_layout(pad=2.0)

	plt.savefig(f"images/comp-E2Q4-comparisons")
	print_table(complex_error, symmetric_error)
	plt.show()