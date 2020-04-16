import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile
filename = "sounds/comp-E2Q6-speech.wav"

# Read frequency and data array for sound track
fs, x = scipy.io.wavfile.read(filename)
print(f"fs = {fs} Hz")

# If we have a stero track (left and right channels), take just the first channel
if len(x.shape) > 1:
    x = x[:, 0]


# Time points (0 to T, with T*fs points)
t = np.linspace(0, len(x)/fs, len(x), endpoint=False)

# Plot signal
plt.plot(t, x, label= "original")
plt.xlabel('time (seconds)')
plt.ylabel('signal')
# plt.show()

# Perform discrete Fourier transform (real signal)
xf = np.fft.fft(x)

# Create frequency axis for plotting
freq = np.linspace(0.0, fs/2, len(xf))

# plt.semilogy(freq, np.abs(xf))
# plt.xlabel('frequency (Hz)')
# plt.ylabel('$\hat{x}$')
# plt.show()

# ---

# Create copy og transformed signal
xf_filtered = xf.copy()

# Cut-off frequencies (Hz)
cutoff_freq_low = 20
cutoff_freq_high = 2000

# Cut-off indices in transform array
n_cut_low = int(2*cutoff_freq_low*len(xf_filtered)/fs)
n_cut_high = int(2*cutoff_freq_high*len(xf_filtered)/fs)

# Remove low and high frequencies
xf_filtered[:n_cut_low] = 0.0
xf_filtered[n_cut_high:] = 0.0

# Plot filtered transform
# plt.semilogy(freq, np.abs(xf_filtered))
# plt.xlabel('frequency (Hz)')
# plt.ylabel('$\hat{x}$')
# plt.show()

# ---
# Perform inverse transform on filtered signal
x_filtered = np.abs(np.fft.ifft(xf_filtered))

# Plot signal
plt.plot(x_filtered, label="filtered", alpha = .5)
plt.xlabel('Time (seconds)')
plt.ylabel('signal')
plt.legend()
plt.show()

scipy.io.wavfile.write("sounds/comp-E2Q6-speechfiltered.wav", fs, x_filtered)

# winsound.PlaySound("sounds/comp-E2Q6-speechfiltered.wav", winsound.SND_FILENAME)