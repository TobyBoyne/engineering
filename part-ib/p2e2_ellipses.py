import numpy as np
import matplotlib.pyplot as plt


sigma = np.array([0.03, 0.28, 0.51, 0.65, 0.70, 0.80, 0.90, 0.95])
tau =	np.array([0.56, 0.54, 0.48, 0.43, 0.41, 0.33, 0.25, 0.16])

t = np.linspace(0, 1/2*np.pi, 100)

fig, ax = plt.subplots()


ax.plot(np.cos(t), np.sin(t) * 1/2)
ax.plot(np.cos(t), np.sin(t) * 1/np.sqrt(3))
ax.plot(sigma, tau, 'x-')

ax.legend(('Tresca', 'von Mises', 'Experimental'))
plt.show()