import matplotlib.pyplot as plt


# 🔹 Bresenham Algorithm
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


# 🔹 Draw All Lines in One Plot
def draw_all_lines(lines):
    fig, ax = plt.subplots(figsize=(8, 8))

    all_x, all_y = [], []

    for i, (x1, y1, x2, y2) in enumerate(lines):
        points = bresenham_slope_based(x1, y1, x2, y2)
        xs, ys = zip(*points)

        color = plt.cm.tab10(i % 10)

        # Plot line
        ax.plot(xs, ys, marker='o', color=color, label=f"Line {i+1}")

        # Mark start/end
        ax.scatter(x1, y1, color='green', marker='s', s=80)
        ax.scatter(x2, y2, color='red', marker='X', s=80)

        # Collect bounds
        all_x.extend(xs)
        all_y.extend(ys)

        # Label points (optional, can clutter)
        for (x, y) in points:
            ax.text(x, y, f"({x},{y})", fontsize=7)

    # Grid setup (pixel style)
    ax.set_xticks(range(min(all_x) - 1, max(all_x) + 2))
    ax.set_yticks(range(min(all_y) - 1, max(all_y) + 2))
    ax.grid(True)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Multiple Lines (Bresenham) - Single Figure")
    ax.set_aspect('equal', adjustable='box')

    ax.legend()
    plt.tight_layout()
    plt.show()


# 🔹 MAIN
if __name__ == "__main__":
    n = int(input("How many lines? "))

    lines = []
    for i in range(n):
        print(f"\nLine {i+1}:")
        x1 = int(input("x1: "))
        y1 = int(input("y1: "))
        x2 = int(input("x2: "))
        y2 = int(input("y2: "))
        lines.append((x1, y1, x2, y2))

    draw_all_lines(lines)




#     How many lines? 4

# Line 1:
# x1: 0
# y1: 0
# x2: 6
# y2: 6

# Line 2:
# x1: 0
# y1: 6
# x2: 6
# y2: 0

# Line 3:
# x1: 3
# y1: 0
# x2: 3
# y2: 6

# Line 4:
# x1: 0
# y1: 3
# x2: 6
# y2: 3