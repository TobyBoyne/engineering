import numpy as np

class Rosenbrock:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __call__(self, xs):
		x0, x1 = xs
		return (self.a - x0) ** 2 + self.b * (x1 - x0 ** 2) ** 2

	def newton(self, xs_0, tol):
		# As g and J are only used in solving, define them locally
		def g(xs):
			x0, x1 = xs
			return np.array([2*(x0 - self.a) + 4*self.b*x0*(x0 ** 2 - x1),
						 2*self.b*(x1 - x0**2)])

		def J(xs):
			x0, x1 = xs
			return np.array([
				[2 - 4*self.b*x1 + 12*self.b*x0**2, -4*self.b*x0],
				[-4*self.b*x0, 2*self.b]
			])

		g_0 = np.linalg.norm(g(xs_0))
		xs = xs_0
		while np.linalg.norm(g(xs)) / g_0 > tol:
			xs = xs - np.linalg.solve(J(xs), g(xs))
		return xs


if __name__ == "__main__":
	r1 = Rosenbrock(2, 100)
	r2 = Rosenbrock(5, 8)

	# confirm results from q7
	print(r1.newton(np.array([1.1, 1.1]), tol=1e-9))
	# show that for different values of a/b, f_min is still 0
	root = r2.newton(np.array([1.1, 1.1]), tol=1e-9)
	assert r2(root) < 1e-10