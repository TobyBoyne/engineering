import numpy as np
import boto3


s3 = boto3.client('s3')

exact = 8500/3

def f(x):
	return x**3 + x**2

def approx_integral(f, a, b, xs, ws, n):
	integral = (b - a) * sum(ws[i] * f(xs[i]) for i in range(n))
	error = abs(integral - exact)/abs(exact)
	print(integral, error)


approx_integral(f, 0, 10, [5 - 5 * (3**(-1/2)), 5 + 5 * (3**(-1/2))], [1/2, 1/2], 2)

x = 0
for i in range(100000000):
	x += 1

print(x)