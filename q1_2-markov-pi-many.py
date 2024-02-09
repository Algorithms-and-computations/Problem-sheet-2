import numpy as np
import matplotlib.pyplot as plt

def markov_pi(N, step_size):
    N_hits = 0
    x = 1
    y = 1

    # Generating all the random numbers at once with NumPy will be a bit faster
    random_numbers_x = np.random.uniform(-step_size, step_size, N)
    random_numbers_y = np.random.uniform(-step_size, step_size, N)

    for i in range(N):
        dx = random_numbers_x[i]
        dy = random_numbers_y[i]

        if abs(x + dx) < 1 and abs(y + dy) < 1:
            x += dx
            y += dy

        if x*x + y*y < 1:
            N_hits += 1


    fraction = N_hits / N * 4

    return fraction



N_runs = 100
N = 10000  # Throws per run

step_sizes = np.arange(0.05, 3.5, 0.1)
stdevs = []

for step_size in step_sizes:
    run_outputs = np.array([markov_pi(N, step_size) - np.pi for _ in range(N_runs)])

    # This sdev will decrease with increasing N. N_runs does not change it at all.
    stdev = np.std(run_outputs)

    stdevs.append(stdev)

plt.plot(step_sizes, stdevs)
plt.xlabel("Step size")
plt.ylabel("stdev(pi - 3.141...)")
plt.show()
