import numpy as np
import matplotlib.pyplot as plt
from math import comb


# 🔹 Bezier function
def bezier_curve(control_points, num_points=100):
    n = len(control_points) - 1
    t_values = np.linspace(0, 1, num_points)

    curve = []

    for t in t_values:
        x, y = 0, 0
        for i in range(n + 1):
            bernstein = comb(n, i) * (t**i) * ((1 - t)**(n - i))
            x += bernstein * control_points[i][0]
            y += bernstein * control_points[i][1]
        curve.append((x, y))

    return np.array(curve)


# 🔹 Input control points
n = int(input("Enter number of control points: "))
control_points = []

for i in range(n):
    x = float(input(f"Enter x{i}: "))
    y = float(input(f"Enter y{i}: "))
    control_points.append((x, y))

control_points = np.array(control_points)

# 🔹 Generate curve
curve = bezier_curve(control_points)

# 🔹 Plot
plt.figure(figsize=(6, 6))

# Control polygon
plt.plot(control_points[:, 0], control_points[:, 1], 'ro--', label="Control Polygon")

# Bezier curve
plt.plot(curve[:, 0], curve[:, 1], 'b-', linewidth=2, label="Bezier Curve")

# Labels
for (x, y) in control_points:
    plt.text(x, y, f"({x},{y})")

plt.title("Bezier Curve")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()


# Enter number of control points: 4
# (0,0), (1,3), (3,3), (4,0)