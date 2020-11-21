import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

D = np.log10(np.array([100., 20., 5.]))
dT = np.log10(np.array([2.5, 50., 667.]))



steels = np.array([
	[0.30, 0.80, 0.50, 0.20, 0.55],
	[0.40, 0.60, 1.20, 0.30, 1.50],
	[0.36, 0.70, 1.50, 0.25, 1.50],
	[0.41, 0.85, 0.50, 0.25, 0.55],
	[0.40, 0.60, 0.65, 0.55, 2.55]
])


log_CCR = 4.3 - 3.27 * steels[:, 0] - steels[:, 1:].sum(axis=-1) / 1.6
print(log_CCR)
print(10 ** log_CCR)




m, c = np.polyfit(D, dT, 1)
ax.plot(D, dT, 'x-')
print(m, c)
xs = np.array([0, np.log10(5)])
ax.plot(xs, c + m * xs, '--')
ax.grid()
ax.set_xlabel('$\log_{10}(D)$')
ax.set_ylabel(r'$\log_{10}(\frac{dT}{dt})$')

ax.legend(('Experimental Points', f'$y={m:.2f}x+{c:.2f}$'))

plt.show()