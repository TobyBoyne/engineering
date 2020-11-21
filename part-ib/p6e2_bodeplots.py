import matplotlib.pyplot as plt
import numpy as np

# amplitude
fig, ax = plt.subplots()

ax.semilogx()
ax.set_ylim(100, -150)
ax.set_xlim(1e-2, 1e3)
ax.grid()
ax.grid(which='minor', axis='x')

ax.set_ylabel('gain in dB')
ax.set_xlabel('frequency (rad/s)')

# plt.show()


# xs = np.logspace(-1, 6, 500)
#
# all_ys = np.repeat(xs, 4).reshape(-1, 4)
# all_ys[:, 0] = 0
# all_ys[:, 1] = 20 * np.log10(xs/300)
# all_ys[:, 2] = - 20 * np.log10(np.abs(1 + (1j/300) * xs))
# all_ys[:, 3] = - 20 * np.log10(np.abs(1 + (1j/22000) * xs))
# plt.plot(np.log10(xs), all_ys)
#
#
#
#
# G_amp = np.sum(all_ys, axis=-1)
# plt.plot(np.log10(xs), G_amp, linewidth = 5, alpha=0.5)
#
#
# plt.show()
#
#
#
# angles = np.repeat(xs, 4).reshape(-1, 4)
# angles[:, 0] = 0
# angles[:, 1] = np.angle(xs * 1j / 300)
# angles[:, 2] = - np.angle(1 + (1j/300) * xs)
# angles[:, 3] = - np.angle(1 + (1j/22000) * xs)
#
# plt.plot(np.log10(xs), angles)
# G_angle = np.sum(angles, axis=-1)
# plt.plot(np.log10(xs), G_angle, linewidth = 5)
#
# plt.show()