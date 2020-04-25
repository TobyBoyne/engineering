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

# Create subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.set_title('Original Signal')
ax2.set_title('Fourier Transform')
ax3.set_title('Filtered Fourier Transform')
ax4.set_title('Output Signal')
fig.tight_layout(pad=3.0)

# Plot signal
ax1.plot(t, x, label= "original")
ax1.set_xlabel('time (seconds)')
ax1.set_ylabel('signal')

# Perform discrete Fourier transform (real signal)
xf = np.fft.fft(x)

# Create frequency axis for plotting
freq = np.linspace(0.0, fs/2, len(xf))

ax2.semilogy(freq, np.abs(xf))
ax2.set_xlabel('frequency (Hz)')
ax2.set_ylabel('$\hat{x}$')

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
ax3.semilogy(freq, np.abs(xf_filtered))
ax3.set_xlabel('frequency (Hz)')
ax3.set_ylabel('$\hat{x}$')

# ---
# Perform inverse transform on filtered signal
x_filtered = np.abs(np.fft.ifft(xf_filtered))

# Plot signal
ax4.plot(x_filtered, label="filtered", alpha = .5)
ax4.set_xlabel('Time (seconds)')
ax4.set_ylabel('signal')
ax4.legend()



scipy.io.wavfile.write("sounds/comp-E2Q6-speechfiltered.wav", fs, x_filtered)

plt.show()