import numpy as np


# funcs stores each function and its derivatives
FUNCS = {
	"quadratic": (lambda x: x ** 2 + 3 * x + 4,
				  lambda x: 2 * x + 3,
				  lambda x: 2),
	"cubic":	(lambda x: x ** 3 + x ** 2,
				 lambda x: 3 * x ** 2 + 2 * x,
				 lambda x: 6 * x + 2)
}

def newton(f, df, ddf, x0):
	"""Return next iteration of Newton's method"""
	return x0 - df(x0) / ddf(x0)

def solve_single_var(f, df, ddf, x0=1, tol=1e-4):
	while abs(df(x0) / ddf(x0)) > tol:
		x0 = newton(f, df, ddf, x0)
	return x0

if __name__ == "__main__":
	# Solve 1 turning point in quadratic
	root = solve_single_var(*FUNCS["quadratic"])
	print(f"Cost of quadratic is minimised at x={root}")

	# Solve two turning points for cubic
	root1 = solve_single_var(*FUNCS["cubic"], x0=1)
	root2 = solve_single_var(*FUNCS["cubic"], x0=-5)
	print(f"Cost of cubic is minimised at x={root1:.4f} and x={root2:.4f}")
