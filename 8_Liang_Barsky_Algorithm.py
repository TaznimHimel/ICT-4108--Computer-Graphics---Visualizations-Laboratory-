import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def liang_barsky_clip(x0, y0, x1, y1, xmin, ymin, xmax, ymax, eps=1e-12):
    if xmin > xmax:
        xmin, xmax = xmax, xmin
    if ymin > ymax:
        ymin, ymax = ymax, ymin

    dx = x1 - x0
    dy = y1 - y0

    if abs(dx) < eps and abs(dy) < eps:
        if xmin - eps <= x0 <= xmax + eps and ymin - eps <= y0 <= ymax + eps:
            return (x0, y0, x1, y1)
        return None

    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    tE, tL = 0.0, 1.0

    for pi, qi in zip(p, q):
        if abs(pi) < eps:
            if qi < 0:
                return None
            continue

        r = qi / pi

        if pi < 0:
            tE = max(tE, r)
        else:
            tL = min(tL, r)

        if tE - tL > eps:
            return None

    cx0 = x0 + tE * dx
    cy0 = y0 + tE * dy
    cx1 = x0 + tL * dx
    cy1 = y0 + tL * dy

    return (cx0, cy0, cx1, cy1)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val > 0:
                return val
            print("Enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter an integer.")


def plot_multiple_lines(lines, xmin, ymin, xmax, ymax):
    if xmin > xmax:
        xmin, xmax = xmax, xmin
    if ymin > ymax:
        ymin, ymax = ymax, ymin

    fig, ax = plt.subplots()

    rect = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                     fill=False, linewidth=2)
    ax.add_patch(rect)

    for idx, (x0, y0, x1, y1, clipped) in enumerate(lines, start=1):
        ax.plot([x0, x1], [y0, y1], linestyle="--", linewidth=1.5,
                label=f"Original L{idx}")

        if clipped is not None:
            cx0, cy0, cx1, cy1 = clipped
            ax.plot([cx0, cx1], [cy0, cy1], linewidth=3,
                    label=f"Clipped L{idx}")

    ax.set_aspect("equal", adjustable="box")
    ax.grid(True)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Liang–Barsky Line Clipping (Multiple Lines)")
    ax.legend()
    plt.show()


def main():
    print("Liang–Barsky Line Clipping (Multiple Lines)\n")

    print("Enter clipping window coordinates:")
    xmin = get_float("xmin: ")
    ymin = get_float("ymin: ")
    xmax = get_float("xmax: ")
    ymax = get_float("ymax: ")

    n = get_positive_int("\nNumber of lines: ")

    lines = []

    for i in range(1, n + 1):
        print(f"\nLine {i} endpoints:")
        x0 = get_float("x0: ")
        y0 = get_float("y0: ")
        x1 = get_float("x1: ")
        y1 = get_float("y1: ")

        clipped = liang_barsky_clip(x0, y0, x1, y1, xmin, ymin, xmax, ymax)

        if clipped is None:
            print("Rejected: outside clipping window.")
        else:
            cx0, cy0, cx1, cy1 = clipped
            print("Accepted.")
            print(f"Clipped endpoints: ({cx0:.4f}, {cy0:.4f}) to ({cx1:.4f}, {cy1:.4f})")

        lines.append((x0, y0, x1, y1, clipped))

    plot_multiple_lines(lines, xmin, ymin, xmax, ymax)


if __name__ == "__main__":
    main()



# Example Input:
# xmin: 0
# ymin: 0
# xmax: 8
# ymax: 6

# Number of lines: 2

# x0: -2
# y0: 3
# x1: 10
# y1: 3

# x0: 1
# y0: 1
# x1: 7
# y1: 5




# Example Input:

# xmin: 4
# ymin: 3
# xmax: 10
# ymax: 7

# Number of lines: 4

# x0: 2
# y0: 2
# x1: 12
# y1: 8

# x0: 1
# y0: 9
# x1: 12
# y1: 9

# x0: 5
# y0: 4
# x1: 9
# y1: 6

# x0: 7
# y0: 1
# x1: 7
# y1: 10
