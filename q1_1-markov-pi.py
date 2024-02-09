import numpy as np

N_hits = 0
x = 0
y = 0
N = 1000000

step_size = 0.1

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
print("Estimate of pi = %f" % fraction)
