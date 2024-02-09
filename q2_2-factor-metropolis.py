import numpy as np
import matplotlib.pyplot as plt

def potential_x2(x):
    return pow(x, 2)/2

def potential_x4(x):
    return pow(x,4)/4


x = 0
steps = 1000000
step_size = 0.1
T = 1  # Temperature

x_samples = []

for i in range(steps):
    xp = x + np.random.uniform(-step_size, step_size)

    dE_2 = potential_x2(xp) - potential_x2(x)

    # (Factorised) Metropolis condition
    if dE_2 < 0 or np.random.rand() < np.exp(- dE_2 / T):
        # Only have to evaluate this if the quadratic part is accepted
        dE_4 = potential_x4(xp) - potential_x4(x)
        if dE_4 < 0 or np.random.rand() < np.exp(- dE_4 / T):
            x = xp

    x_samples.append(x)

# Hisogram, and normalise the maximum height to be 1
counts, bin_edges = np.histogram(x_samples, bins=50)
counts_normalized = counts / counts.max()
bin_widths = np.diff(bin_edges)
plt.bar(bin_edges[:-1], counts_normalized, width=bin_widths, edgecolor='black', align='edge')

x_range = np.linspace(min(x_samples), max(x_samples), 100)
expected = [np.exp(- (potential_x2(x) + potential_x4(x)) / T) for x in x_range]
plt.plot(x_range, expected, color='red')

plt.xlabel("x")
plt.ylabel("boltzmann weight")

plt.show()
