import control as ctr
import numpy as np
import matplotlib.pyplot as plt

H = 1121.
m = 200
kp = 0.091
T = 1
Td = 2

num = H * kp * np.array([Td, 1.])
den = m * np.array([T, 1, 0, 0])

G = ctr.tf(num, den)

fig1, ax = plt.subplots()
mag, phase, omega = ctr.nyquist(G,[0.01,1000])


t = np.linspace(0, 2*np.pi, 100)
ax.plot(np.cos(t), np.sin(t))


fig2 = plt.figure()
ws = np.geomspace(0.01,100,50)
mag, phase, omega = ctr.bode(G, ws)

zero_db = np.argmin(abs(np.log10(mag)))
for ax in fig2.axes:
	ax.axvline(ws[zero_db], color='tab:orange')

print(ws[zero_db])
print(phase[zero_db])
plt.show()
