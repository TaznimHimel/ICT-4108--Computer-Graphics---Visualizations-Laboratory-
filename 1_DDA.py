import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    if steps == 0:
        return [x1], [y1]

    Xinc = dx / steps
    Yinc = dy / steps

    x = x1
    y = y1

    x_points = []
    y_points = []

    for i in range(steps + 1):
        x_points.append(x)   # smooth line (no rounding)
        y_points.append(y)
        x += Xinc
        y += Yinc

    return x_points, y_points


# 🔹 Take input for 4 lines
lines = []
for i in range(4):
    print(f"\nLine {i+1}:")
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    title = input("Enter title (e.g., slope < 1): ")

    lines.append((x1, y1, x2, y2, title))


# 🔹 Create 2x2 subplot window
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

for i, (x1, y1, x2, y2, title) in enumerate(lines):
    ax = axes[i // 2][i % 2]

    x_pts, y_pts = DDA(x1, y1, x2, y2)

    ax.plot(x_pts, y_pts, marker='o')
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.axis('equal')

    # Optional: label endpoints
    ax.text(x1, y1, f"({x1},{y1})")
    ax.text(x2, y2, f"({x2},{y2})")


plt.tight_layout()
plt.show()