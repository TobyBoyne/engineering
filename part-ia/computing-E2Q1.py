import numpy as np
n = 26 * 10 ** 6

def linear(m):
	return m * n * 10 ** -8

def binary(m):
	return 2 * 10 ** -5 * n * np.log(n) + m * 10 ** -6 * np.log(n)

if __name__ == '__main__':
	for m in (10 ** 3, 10 ** 4, 3 * 10 ** 5, 5 * 10 ** 5):
		print(f'For m = {m}: linear = {linear(m)}, binary = {binary(m)}')