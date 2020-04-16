import numpy as np
n = 26e6

def linear(m):
	return m * n * 1e-8

def binary(m):
	return 2e-5 * n * np.log(n) + m * 1e-6 * np.log(n)

if __name__ == '__main__':
	for m in (1e3, 1e4, 3e5, 5e5):
		print(f'For m = {m}: linear = {linear(m)}, binary = {binary(m)}')