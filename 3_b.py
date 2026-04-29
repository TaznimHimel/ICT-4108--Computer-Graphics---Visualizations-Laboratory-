import matplotlib.pyplot as plt
import numpy as np
from math import comb


# 🔹 B-spline basis (Cox–de Boor)
def N(i, p, u, U):
    if p == 0:
        return 1.0 if U[i] <= u < U[i+1] else 0.0

    left = 0
    right = 0

    if U[i+p] != U[i]:
        left = (u - U[i]) / (U[i+p] - U[i]) * N(i, p-1, u, U)

    if U[i+p+1] != U[i+1]:
        right = (U[i+p+1] - u) / (U[i+p+1] - U[i+1]) * N(i+1, p-1, u, U)

    return left + right


# 🔹 Knot vector
def knot_vector(n, p):
    U = [0]*(p+1)
    for i in range(1, n-p+1):
        U.append(i/(n-p+1))
    U += [1]*(p+1)
    return U


# 🔹 B-spline curve
def bspline(control_points, p):
    n = len(control_points) - 1
    U = knot_vector(n, p)

    curve_x = []
    curve_y = []

    for u in np.linspace(U[p], U[n+1], 200):
        x = 0
        y = 0
        for i in range(n+1):
            b = N(i, p, u, U)
            x += b * control_points[i][0]
            y += b * control_points[i][1]

        curve_x.append(x)
        curve_y.append(y)

    return curve_x, curve_y


# 🔹 MAIN
n = int(input("Number of control points: "))

points = []
for i in range(n):
    x = float(input(f"x{i}: "))
    y = float(input(f"y{i}: "))
    points.append((x, y))

p = int(input("Enter degree: "))

cx, cy = bspline(points, p)

px, py = zip(*points)

plt.plot(px, py, 'ro--', label="Control Polygon")
plt.plot(cx, cy, 'b-', linewidth=2, label="B-spline Curve")

plt.title("B-Spline Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.axis("equal")
plt.show()