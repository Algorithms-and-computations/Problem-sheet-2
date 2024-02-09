import numpy as np
import matplotlib.pyplot as plt

def potential(x):
    return pow(x, 2)/2 + pow(x,4)/4

step_size = 0.07
num_samples = 100000
T = 1  # Temperature

x_samples = []

x = 0
direction = +1

for _ in range(num_samples):
    xp = x + direction * np.random.uniform(0, step_size)
    dE = potential(xp) - potential(x)

    if dE < 0 or np.random.rand() < np.exp(- dE / T):

        x = xp
    else:
        direction *= -1

    x_samples.append(x)


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
