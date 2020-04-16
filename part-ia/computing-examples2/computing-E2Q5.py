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

def convolution(G, A):
	n = len(G)
	d = n //2
	Y, X = A.shape
	B = np.zeros((Y - 2 * d, X - 2 * d))
	for (i, j), _ in np.ndenumerate(B):
		B[i, j] = np.sum(G * A[i:i+n, j:j+n])
	return B


if __name__ == "__main__":
	xs = np.linspace(0, 2 * np.pi, 50)
	ys = f(xs)
	ys_avg = moving_avg(ys)

	plt.plot(xs, ys)
	plt.plot(xs[1:-1], ys_avg)
	plt.legend(("Original", "Smoothed"))
	plt.savefig(fname="images/comp-E2Q5-movingavg")
	plt.show()

	# get southwing image and store as 2D greyscale by taking R values (assuming R==G==B)
	image = plt.imread("images/southwing.jpg")
	image = image[:, :, 0]

	G = np.array([
		[-1, -1, -1],
		[-1,  8, -1],
		[-1, -1, -1]
	])
	n = len(G)
	d = n // 2
	B = convolution(G, image)

	plt.imshow(B, cmap="gray")
	plt.imsave("images/comp-E2Q5-edgedetect.png", B, cmap="gray")
	plt.show()