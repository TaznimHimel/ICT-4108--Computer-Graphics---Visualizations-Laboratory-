import matplotlib.pyplot as plt

def bresenham_slope_based(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    # 🔹 1. Handle Same Point Case
    if dx == 0 and dy == 0:
        print("Single point detected.")
        return [(x1, y1)]

    m = dy / dx if dx != 0 else float('inf')

    if m != float('inf'):
        print(f"Slope (m) = {m:.2f}")
    else:
        print("Slope (m) = ∞ (vertical line)")

    # CASE 1: slope ≤ 1
    if dy <= dx:
        p = 2 * dy - dx
        print(f"Initial decision parameter (p0) = {p}")

        x, y = x1, y1

        for i in range(dx + 1):
            points.append((x, y))
            print(f"Point {i+1}: ({x}, {y}), p = {p}")

            if p >= 0:
                y += sy
                p += 2 * (dy - dx)
            else:
                p += 2 * dy

            x += sx

    # CASE 2: slope > 1
    else:
        p = 2 * dx - dy
        print(f"Initial decision parameter (p0) = {p}")

        x, y = x1, y1

        for i in range(dy + 1):
            points.append((x, y))
            print(f"Point {i+1}: ({x}, {y}), p = {p}")

            if p >= 0:
                x += sx
                p += 2 * (dx - dy)
            else:
                p += 2 * dx

            y += sy

    return points


def main():
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    points = bresenham_slope_based(x1, y1, x2, y2)

    print("\nGenerated Points:")
    for p in points:
        print(p)

    xs, ys = zip(*points)

    plt.figure(figsize=(6, 6))
    plt.plot(xs, ys, marker='o')

    # 🔹 2. Better Visualization
    plt.axis("equal")

    # 🔹 3. Add Labels to Points
    for (x, y) in points:
        plt.text(x, y, f"({x},{y})")

    plt.title(f"Bresenham Line: ({x1},{y1}) → ({x2},{y2})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, linestyle='--', linewidth=0.5)

    plt.show()


if __name__ == "__main__":
    main()


# Enter x1: 2
# Enter y1: 3
# Enter x2: 10
# Enter y2: 6


# Enter x1: 2
# Enter y1: 2
# Enter x2: 5
# Enter y2: 10