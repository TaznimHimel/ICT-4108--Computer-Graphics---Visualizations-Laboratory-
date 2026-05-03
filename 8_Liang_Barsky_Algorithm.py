import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    dx = x1 - x0
    dy = y1 - y0

    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]

    tE, tL = 0.0, 1.0

    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return None
        else:
            t = qi / pi
            if pi < 0:
                tE = max(tE, t)
            else:
                tL = min(tL, t)

        if tE > tL:
            return None

    cx0 = x0 + tE * dx
    cy0 = y0 + tE * dy
    cx1 = x0 + tL * dx
    cy1 = y0 + tL * dy

    return cx0, cy0, cx1, cy1


def main():
    print("Liang–Barsky Line Clipping\n")

    xmin = float(input("xmin: "))
    ymin = float(input("ymin: "))
    xmax = float(input("xmax: "))
    ymax = float(input("ymax: "))

    n = int(input("\nNumber of lines: "))
    if n <= 0:
        print("Invalid number of lines!")
        return

    lines = []
    for i in range(n):
        print(f"\nLine {i+1}")
        x0 = float(input("x0: "))
        y0 = float(input("y0: "))
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))

        clipped = liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax)

        if clipped:
            print("Accepted")
        else:
            print("Rejected")

        lines.append((x0, y0, x1, y1, clipped))

    # 🔹 Plot
    fig, ax = plt.subplots(figsize=(7, 7))

    # Window
    ax.add_patch(Rectangle((xmin, ymin), xmax-xmin, ymax-ymin,
                           fill=False, linewidth=2, edgecolor='black', label="Clipping Window"))

    colors = ['r', 'g', 'b', 'm', 'c', 'y']

    for i, (x0, y0, x1, y1, clipped) in enumerate(lines):
        color = colors[i % len(colors)]

        # Original line
        ax.plot([x0, x1], [y0, y1],
                linestyle='--', color=color,
                label="Original Line" if i == 0 else "")

        # Clipped line
        if clipped:
            cx0, cy0, cx1, cy1 = clipped
            ax.plot([cx0, cx1], [cy0, cy1],
                    color=color, linewidth=3,
                    label="Clipped Line" if i == 0 else "")
        else:
            # Rejected line marker
            ax.plot([], [], color=color, linestyle='--',
                    label="Rejected Line" if i == 0 else "")

    # 🔥 Remove duplicate labels
    handles, labels = ax.get_legend_handles_labels()
    unique = dict(zip(labels, handles))
    ax.legend(unique.values(), unique.keys(), loc='upper right')

    ax.set_title("Liang–Barsky Line Clipping")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid(True)
    ax.set_aspect("equal")

    plt.show()


if __name__ == "__main__":
    main()



# xmin: 1
# ymin: 1
# xmax: 8
# ymax: 6

# Number of lines: 6

# Line 1
# x0: 2
# y0: 2
# x1: 6
# y1: 5
# Accepted

# Line 2
# x0: 9
# y0: 7
# x1: 12
# y1: 10
# Rejected

# Line 3
# x0: -2
# y0: 3
# x1: 5
# y1: 3
# Accepted

# Line 4
# x0: 4
# y0: 4
# x1: 10
# y1: 4
# Accepted

# Line 5
# x0: 2
# y0: 3
# x1: 7
# y1: 3
# Accepted

# Line 6
# x0: 2
# y0: 7
# x1: 7
# y1: 7
# Rejected