import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sin(x) + np.cos(10 * x) / 5

def moving_avg(arr):
	"""Returns moving average array of data points of length == len(arr) - 2 due to edges"""
	avg = np.zeros(len(arr) - 2)
	for i in range(len(avg)):
		avg[i] = sum(arr[i:i+3]) / 3
	return avg

if __name__ == "__main__":
	xs = np.linspace(0, 2 * np.pi, 50)
	ys = f(xs)
	ys_avg = moving_avg(ys)

	plt.plot(xs, ys)
	plt.plot(xs[1:-1], ys_avg)
	plt.legend(("Original", "Smoothed"))
	plt.show()