import numpy as np

class Rosenbrock:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __call__(self, xs):
		x0, x1 = xs
		return (self.a - x0) ** 2 + self.b * (x1 - x0 ** 2) ** 2

	def g(self, xs):
		x0, x1 = xs
		return np.array([2*(x0 - self.a) + 4*self.b*x0*(x0 ** 2 - x1),
					 2*self.b*(x1 - x0**2)])

	def J(self, xs):
		x0, x1 = xs
		return np.array([
			[2 - 4*self.b*x1 + 12*self.b*x0**2, -4*self.b*x0],
			[-4*self.b*x0, 2*self.b]
		])