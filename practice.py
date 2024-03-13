import numpy as np
import matplotlib.pyplot as plt

T = 2
omega = np.logspace(-2, 2, 1000)
magnitude_response = 1 / np.sqrt(1 + 4 * (omega**2))
phase_response = -np.arctan(2 * omega)
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(omega, magnitude_response)
plt.title('Magnitude Frequency Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude')
plt.subplot(2, 1, 2)
plt.semilogx(omega, phase_response)
plt.title('Phase Frequency Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (radians)')
plt.tight_layout()
plt.show()