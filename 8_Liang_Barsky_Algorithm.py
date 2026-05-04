import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D


def classify_line(x0, y0, x1, y1, xmin, ymin, xmax, ymax, clipped):
    inside0 = xmin <= x0 <= xmax and ymin <= y0 <= ymax
    inside1 = xmin <= x1 <= xmax and ymin <= y1 <= ymax

    if inside0 and inside1:
        return "Trivially Accepted"
    if clipped is None:
        return "Trivially Rejected"
    return "Partially Accepted (Crossing Window)"


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

    xmin, ymin, xmax, ymax = map(float, input("Enter window (xmin ymin xmax ymax): ").split())

    n = int(input("Number of lines: "))
    lines = []

    for i in range(n):
        print(f"\nLine {i+1} (format: x0 y0 x1 y1)")
        x0, y0, x1, y1 = map(float, input().split())

        clipped = liang_barsky(x0, y0, x1, y1, xmin, ymin, xmax, ymax)
        category = classify_line(x0, y0, x1, y1, xmin, ymin, xmax, ymax, clipped)

        print(f"Result: {category}")
        lines.append((x0, y0, x1, y1, clipped, category))

    # 🔹 SIDE-BY-SIDE PLOT
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(14, 7))

    # Window
    ax.add_patch(Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                           fill=False, linewidth=2, edgecolor='black'))
    ax2.add_patch(Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                            fill=False, linewidth=2, edgecolor='black'))

    colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'cyan']

    for i, (x0, y0, x1, y1, clipped, category) in enumerate(lines):
        color = colors[i % len(colors)]

        # ---------- LEFT (ORIGINAL) ----------
        ax.plot([x0, x1], [y0, y1], linestyle='--', color=color, linewidth=1)

        midx = (x0 + x1) / 2
        midy = (y0 + y1) / 2

        if category == "Trivially Accepted":
            ax.plot([x0, x1], [y0, y1], color=color, linewidth=3)
            label = "TA"

        elif category == "Trivially Rejected":
            label = "TR"

        else:
            cx0, cy0, cx1, cy1 = clipped
            ax.plot([cx0, cx1], [cy0, cy1], color=color, linewidth=3)
            label = "PA"

        ax.text(midx, midy, label,
                fontsize=9, color='black',
                ha='center',
                bbox=dict(facecolor=color, alpha=0.3, edgecolor='none'))

        # ---------- RIGHT (ONLY INSIDE) ----------
        if category == "Trivially Accepted":
            ax2.plot([x0, x1], [y0, y1], color=color, linewidth=3)

        elif category == "Partially Accepted (Crossing Window)":
            cx0, cy0, cx1, cy1 = clipped
            ax2.plot([cx0, cx1], [cy0, cy1], color=color, linewidth=3)

    # Legend only on left
    legend_elements = [
        Line2D([0], [0], color='black', lw=2, linestyle='--', label='Original Line'),
        Line2D([0], [0], color='black', lw=3, label='Clipped (Visible) Part'),
        Line2D([0], [0], color='none', label='TA: Trivially Accepted'),
        Line2D([0], [0], color='none', label='TR: Trivially Rejected'),
        Line2D([0], [0], color='none', label='PA: Partially Accepted')
    ]

    ax.legend(handles=legend_elements, loc='upper left', frameon=True)

    # Titles
    ax.set_title("Original Output")
    ax2.set_title("Only Inside (Clipped Lines)")

    # Common settings
    for a in [ax, ax2]:
        a.set_xlabel("X-axis")
        a.set_ylabel("Y-axis")
        a.grid(True)
        a.set_aspect("equal")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()


# Enter window (xmin ymin xmax ymax): 2 2 10 10
# Number of lines: 8

# Line 1 (format: x0 y0 x1 y1)
# 3 3 8 8

# Line 2 (format: x0 y0 x1 y1)
# 0 0 5 5

# Line 3 (format: x0 y0 x1 y1)
# 12 12 15 15

# Line 4 (format: x0 y0 x1 y1)
# 0 5 15 5

# Line 5 (format: x0 y0 x1 y1)
# 5 0 5 15

# Line 6 (format: x0 y0 x1 y1)
# 2 2 10 10

# Line 7 (format: x0 y0 x1 y1)
# 2 8 10 8

# Line 8 (format: x0 y0 x1 y1)
# -5 6 15 6