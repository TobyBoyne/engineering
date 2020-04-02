import numpy as np

def f(x, y):
	return np.e ** (x * y) * np.cos(y) ** 2 * np.sin(x ** 2)

def in_circle(x, y):
	# returns 4 if the chosen point is within the unit circle, else 0
	return 4 if x**2 + y**2 < 1 else 0

def function_mean(f, a, b, N):
	# creates N random numbers uniformly distributed between -a and +a (or -b and +b)
	xs = 2 * a * np.random.rand(N) - a
	ys = 2 * b * np.random.rand(N) - b

	# iterate through the xs and ys, taking one from each in pairs to compute f(x, y) at that point
	return sum(f(x_i, y_i) for (x_i, y_i) in zip(xs, ys)) / N


for power in (2, 5, 6):
	print("Mean of f =", function_mean(f, 1, 1, pow(10, power)), "for N = 10 ^", power)
	print("Pi =",function_mean(in_circle, 1, 1, pow(10, power)), "for N = 10 ^", power)