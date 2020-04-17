import numpy as np

h = 1e-7

def df(f, x):
	return (f(x + h) - f(x - h)) / (2 * h)

def ddf(f, x):
	return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2


def quadratic(x):
	return x ** 2 + 4 * x + 3

def cubic(x):
	return x ** 3 + x ** 2



def newton(f, x_0):
	"""Return next iteration of Newton's method"""
	return x_0 - df(f, x_0) / ddf(f, x_0)

def solve_single_var(f, x_0, tol=1e-4):
	while abs(df(f, x_0)) / abs(ddf(f, x_0)) > tol:
		x_0 = newton(f, x_0)
	return x_0


if __name__ == "__main__":

	# Solve 1 turning point in quadratic
	root = solve_single_var(quadratic, x_0=-1)
	print(f"Cost of quadratic is minimised at x={root:.3f}")

	# Solve two turning points for cubic
	root1 = solve_single_var(cubic, x_0=1)
	root2 = solve_single_var(cubic, x_0=-5)
	print(f"Cost of cubic is minimised at x={root1:.4f} and x={root2:.4f}")
