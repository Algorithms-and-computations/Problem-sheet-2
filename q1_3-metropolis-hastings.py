import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle

def sample_triangle(delta):
    # Square
    # x = np.random.uniform(-1, 1) * delta
    # y = np.random.uniform(-1, 1) * delta
    # return x, y

    # I am lazy to implement equilaterial triangle, so using a right angled triangle:
    #
    #     *
    #    **
    #   ***
    #  ****
    # *****

    # Rejection sample this
    while True:
        x = np.random.uniform(-2, 1)
        y = np.random.uniform(-1, 2)
        if y <= x + 1:
            return x * delta, y * delta

def A(x, y, xp, yp, delta):
    # Square
    # return 1 if (abs(x-xp)/delta <=1 and abs(y-yp)/delta <= 1) else 0

    dx = (xp - x) / delta
    dy = (yp - y) / delta

    return 1 if (dx <= 1 and dx >= -2 and dy <= 2 and dy >= -1 and dy <= dx + 1) else 0


def plot_sampling_of_triangle():
    xs = []
    ys = []
    xs_inside = []
    ys_inside = []

    for i in range(10000):
        x, y = sample_triangle(1)
        if A(x, y, 0, 0, 1) == 1:
            xs.append(x)
            ys.append(y)
        else:
            xs_inside.append(x)
            ys_inside.append(y)


    plt.scatter(xs, ys, color='red')
    plt.scatter(xs_inside, ys_inside, color='blue')
    plt.axis('equal')
    plt.title("Sampling triangle from A(x, x'). Red has A(x', x) = 1 also")
    plt.show()

# Just to show it works
plot_sampling_of_triangle()


N = 100000
x = 1
y = 1
delta = 0.8
N_hits = 0

xs = []
ys = []

accepted_dxs = []
accepted_dys = []

for i in range(N):
    # Propose and a priori move
    # (This is sampled with the probability A(x,y, x', y') )
    dx, dy = sample_triangle(delta)

    # x' and y'
    xp = x + dx
    yp = y + dy

    # Check whether to accept. pi(x, y) and pi(x', y')
    # pi_xy = 1 if (abs(x) <= 1 and abs(y) <= 1) else 0
    # assert pi_xy == 1, "pi_xy should always be zero, as we should start in a valid configuration"

    pi_xpyp = 1 if (abs(xp) <= 1 and abs(yp) <= 1) else 0

    A_xp_x = A(xp, yp, x, y, delta)

    # A_x_xp = A(x, y, xp, yp, delta)
    # assert A_x_xp == 1, "A_x_xp should always be 1, as we just sampled it"

    # Should always be 1, assuming we sample correctly
    # (Calculating manuallly sometimes gives the wrong answer because floating point errors)
    # A_x_xp = 1

    # Should in principle normalise A(...), but since dividing one by another,
    #  it doesn't matter here

    # Since A is a constant, the acceptance probability (eqn 2.12)
    #  reduces to 1 if pi_xpyp and A are both 1, otherwise it's zero.
    #  We will always have pi_xy being 1 (because always start in a valid configuration)
    #  And A_x_xp being 1 (because we sample the triangle correctly)

    if pi_xpyp == 1 and A_xp_x == 1:
        x = xp
        y = yp

        accepted_dxs.append(dx)
        accepted_dys.append(dy)

    if x*x + y*y < 1:
        N_hits += 1

    xs.append(x)
    ys.append(y)

fraction = N_hits / N * 4
print("pi = %f" % fraction)
plt.scatter(xs, ys)
plt.axis('equal')
circle = Circle((0, 0), 1, color='red', fill=False)
square = Rectangle((-1, -1), 2, 2, color='red', fill=False)
ax = plt.gca()
ax.add_patch(circle)
ax.add_patch(square)
plt.title("Uniform sampling of pi(x,y)")
plt.show()

plt.scatter(accepted_dxs, accepted_dys)
plt.axis('equal')
plt.title("dx and dy")
plt.show()
