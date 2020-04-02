import numpy as np
import matplotlib.pyplot as plt

plt.figure()

dt = 0.01
m = 1
k = 40
f = 0

# set up the points on the time axis
ts = np.linspace(0, 20, num=int(20 / dt), endpoint=True)
# plot the analytical solution
plt.plot(ts, 0.01 * np.cos(np.sqrt(k / m) * ts))


def compute_solution(f=0):
	xs = np.array([0.01, 0.01])
	# find x values for x_2 onwards
	for t in ts[2:]:
		# calculate sign of friction force
		v = (xs[-1] - xs[-2]) / dt
		F = f if v < 0 else -f if v > 0 else 0

		# compute next value of x from formula derived in 7b
		# then append this value to the xs array
		next_x = 2*xs[-1] - xs[-2] + dt ** 2 * (F - k * xs[-1]) / m
		xs = np.append(xs, next_x)

	plt.plot(ts, xs)

# compute and plot graphs for f=0 and f=0.025
compute_solution()
compute_solution(f=0.025)

plt.xlabel("t")
plt.ylabel("x")
plt.legend(("Analytical", "Numerical, f=0", "Numerical, f=0.025"), loc="right")
plt.show()