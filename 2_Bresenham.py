import matplotlib.pyplot as plt
import numpy as np


def bresenham_slope_based(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx == 0 and dy == 0:
        return [(x1, y1)]

    if dy <= dx:
        p = 2 * dy - dx
        x, y = x1, y1

        for _ in range(dx + 1):
            points.append((x, y))
            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy
            x += sx
    else:
        p = 2 * dx - dy
        x, y = x1, y1

        for _ in range(dy + 1):
            points.append((x, y))
            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx
            y += sy

    return points


# 🔹 Function to calculate slope text
def get_slope_info(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    if dx == 0:
        return "m = ∞ (vertical)"
    
    m = dy / dx

    if m == 1:
        return f"m = 1"
    elif m > 1:
        return f"m = {m:.2f} (>1)"
    elif 0 < m < 1:
        return f"m = {m:.2f} (<1)"
    elif m < 0:
        return f"m = {m:.2f} (negative)"
    else:
        return f"m = {m:.2f}"


# 🔹 MAIN
n = int(input("How many lines do you want to draw? "))

lines = []
for i in range(n):
    print(f"\nLine {i+1}:")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    lines.append((x1, y1, x2, y2))


# 🔹 Subplot setup
cols = 2
rows = (n + cols - 1) // cols

fig, axes = plt.subplots(rows, cols, figsize=(10, 5 * rows))
axes = np.array(axes).ravel()


# 🔹 Plot
for i, (x1, y1, x2, y2) in enumerate(lines):
    ax = axes[i]

    points = bresenham_slope_based(x1, y1, x2, y2)
    xs, ys = zip(*points)

    slope_text = get_slope_info(x1, y1, x2, y2)

    ax.plot(xs, ys, marker='o')
    ax.set_title(f"Line {i+1}\n{slope_text}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.axis("equal")

    # Label points
    for (x, y) in points:
        ax.text(x, y, f"({x},{y})", fontsize=8)

    # 🔹 Show slope inside graph (top-left corner)
    ax.text(0.05, 0.9, slope_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='top')


# 🔹 Remove unused plots
for j in range(len(lines), len(axes)):
    fig.delaxes(axes[j])


plt.tight_layout()
plt.show()





# How many lines do you want to draw? 4

# Line 1:
# Enter x1: 0
# Enter y1: 0
# Enter x2: 6
# Enter y2: 6

# Line 2:
# Enter x1: 0
# Enter y1: 6
# Enter x2: 6
# Enter y2: 0

# Line 3:
# Enter x1: 3
# Enter y1: 0
# Enter x2: 3
# Enter y2: 6

# Line 4:
# Enter x1: 0
# Enter y1: 3
# Enter x2: 6
# Enter y2: 3