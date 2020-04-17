import numpy as np

h = 1e-7
a = 2
b = 100

def df(f, x):
	return (f(x + h) - f(x - h)) / (2 * h)

def ddf(f, x):
	return (f(x + h) - 2 * f(x) + f(x - h)) / h ** 2


def g(xs):
	x0, x1 = xs
	return np.array([2*(x0 - a) + 4*b*x0*(x0 ** 2 - x1),
					 2*b*(x1 - x0**2)])

def J(xs):
	x0, x1 = xs
	return np.array([
		[2 - 4*b*x1 + 12*b*x0**2,	-4*b*x0],
		[-4*b*x0,					2*b]
	])


def quadratic(x):
	return x ** 2 + 4 * x + 3

def cubic(x):
	return x ** 3 + x ** 2

def rosenbrock(xs):
	return (a - xs[0]) ** 2 + b * (xs[1] - xs[0] ** 2) ** 2


def newton(f, x):
	"""Return next iteration of Newton's method"""
	return x - df(f, x) / ddf(f, x)

def newton_multi(xs):
	"""Return next iteration of Newton's method for multiple variables"""
	return xs - np.linalg.solve(J(xs), g(xs))

def solve_single_var(f, x_0, tol=1e-4):
	x = x_0
	while abs(df(f, x)) / abs(ddf(f, x)) > tol:
		x = newton(f, x)
	return x

def solve_multi_var(f, xs_0, tol=1e-4):
	g_0 = np.linalg.norm(g(xs_0))
	xs = xs_0
	while np.linalg.norm(g(xs)) / g_0 > tol:
		xs = newton_multi(xs)
	return xs

if __name__ == "__main__":

	# Solve 1 turning point in quadratic
	root = solve_single_var(quadratic, x_0=-1)
	print(f"Cost of quadratic is minimised at x={root:.3f}")

	# Solve two turning points for cubic
	root1 = solve_single_var(cubic, x_0=1)
	root2 = solve_single_var(cubic, x_0=-5)
	print(f"Cost of cubic is minimised at x={root1:.4f} and x={root2:.4f}")

	# Solve Rosenbrock
	root = solve_multi_var(rosenbrock, np.array([1.1, 1.1]), tol=1e-9)
	f_min = rosenbrock(root)
	print(f"Minimum value of {f_min} found at [x0, x1]={root}")