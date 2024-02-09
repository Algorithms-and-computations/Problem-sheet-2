import numpy as np
import matplotlib.pyplot as plt

def potential(x):
    return pow(x, 2)/2 + pow(x,4)/4

x = 0
direction = +1
t = 0
step_size = 0.001
num_samples = 10000 / step_size
T = 1  # Temperature

x_samples = []

while len(x_samples) < num_samples:
    # Relies on being able to invert the potential!
    x_ev = direction * np.sqrt(-1 + np.sqrt(1 - 4 * T * np.log(np.random.rand())))
    t_ev = int((abs(x_ev - x) / step_size))
    for t in range(t+1, t+t_ev+1):
        if len(x_samples) >= num_samples:
            break

        x = x + direction * step_size
        x_samples.append(x)

    t = t+t_ev
    direction *= -1

#
# Hisogram, and normalise the maximum height to be 1
counts, bin_edges = np.histogram(x_samples, bins=50)
counts_normalized = counts / counts.max()
bin_widths = np.diff(bin_edges)
plt.bar(bin_edges[:-1], counts_normalized, width=bin_widths, edgecolor='black', align='edge')

x_range = np.linspace(min(x_samples), max(x_samples), 100)
expected = [np.exp(- potential(x) / T) for x in x_range]
plt.plot(x_range, expected, color='red')

plt.xlabel("x")
plt.ylabel("boltzmann weight")

plt.show()
