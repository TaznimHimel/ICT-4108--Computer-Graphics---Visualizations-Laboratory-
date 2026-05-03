import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

def midpoint_ellipse(a, b, xc, yc, ellipse_id):

    x = 0
    y = int(b)

    a2 = a * a
    b2 = b * b

    region1_pts = []
    region2_pts = []

    print(f"\n========== Ellipse {ellipse_id} ==========")

    step = 1

    # ---------------------------
    # REGION 1
    # ---------------------------
    print("🔵 REGION 1")
    p1 = b2 - (a2 * b) + (0.25 * a2)

    while (2 * b2 * x) < (2 * a2 * y):

        print(f"Step {step}: (x={x}, y={y}), p1={p1:.2f}")

        symmetric = {
            ( xc + x, yc + y),
            ( xc - x, yc + y),
            ( xc + x, yc - y),
            ( xc - x, yc - y)
        }

        print("  Symmetric Points:")
        for i, pt in enumerate(symmetric):
            print(f"   P{i+1}: {pt}")
            region1_pts.append(pt)

        if p1 < 0:
            x += 1
            p1 += 2 * b2 * x + b2
        else:
            x += 1
            y -= 1
            p1 += 2 * b2 * x - 2 * a2 * y + b2

        step += 1

    # ---------------------------
    # REGION 2
    # ---------------------------
    print("🟣 REGION 2")
    p2 = (b2 * (x + 0.5)**2) + (a2 * (y - 1)**2) - (a2 * b2)

    while y >= 0:

        print(f"Step {step}: (x={x}, y={y}), p2={p2:.2f}")

        symmetric = {
            ( xc + x, yc + y),
            ( xc - x, yc + y),
            ( xc + x, yc - y),
            ( xc - x, yc - y)
        }

        print("  Symmetric Points:")
        for i, pt in enumerate(symmetric):
            print(f"   P{i+1}: {pt}")
            region2_pts.append(pt)

        if p2 > 0:
            y -= 1
            p2 += -2 * a2 * y + a2
        else:
            x += 1
            y -= 1
            p2 += 2 * b2 * x - 2 * a2 * y + a2

        step += 1

    return region1_pts, region2_pts


def plot_ellipse(ax, a, b, xc, yc, r1, r2, title):

    # smooth ellipse
    theta = np.linspace(0, 2*np.pi, 400)
    ex = xc + a * np.cos(theta)
    ey = yc + b * np.sin(theta)

    ax.plot(ex, ey, color='white', linewidth=1.5)

    # region points
    for pt in r1:
        ax.scatter(pt[0], pt[1], color='cyan', s=20)
    for pt in r2:
        ax.scatter(pt[0], pt[1], color='orange', s=20)

    # axes
    ax.plot([xc - a, xc + a], [yc, yc], color='red', linewidth=1.5)
    ax.plot([xc, xc], [yc - b, yc + b], color='lime', linewidth=1.5)

    ax.scatter(xc, yc, color='yellow', s=60)

    ax.set_title(title)
    ax.set_aspect('equal')
    ax.grid(True)

    ax.set_xlim(xc - a - 2, xc + a + 2)
    ax.set_ylim(yc - b - 2, yc + b + 2)

    # legend (dummy)
    ax.scatter([], [], color='cyan', label="Region 1")
    ax.scatter([], [], color='orange', label="Region 2")
    ax.legend(fontsize=8)


# ============================
# 🔹 INPUT (4 Ellipses)
# ============================

ellipses = []
for i in range(4):
    print(f"\nEllipse {i+1}:")
    a = int(input("  Enter a: "))
    b = int(input("  Enter b: "))
    xc = int(input("  Center x: "))
    yc = int(input("  Center y: "))
    ellipses.append((a, b, xc, yc))

# ============================
# 🔹 SUBPLOT (2x2)
# ============================

fig, axs = plt.subplots(2, 2, figsize=(10,10))
axs = axs.flatten()

for i, (a, b, xc, yc) in enumerate(ellipses):
    r1, r2 = midpoint_ellipse(a, b, xc, yc, i+1)
    plot_ellipse(axs[i], a, b, xc, yc, r1, r2,
                 f"Ellipse {i+1} (a={a}, b={b})")

plt.tight_layout()
plt.show()

# Ellipse 1:
# a = 8
# b = 5
# xc = 0
# yc = 0

# Ellipse 2:
# a = 6
# b = 6
# xc = 0
# yc = 0

# Ellipse 3:
# a = 10
# b = 3
# xc = 2
# yc = 2

# Ellipse 4:
# a = 5
# b = 9
# xc = -2
# yc = -2