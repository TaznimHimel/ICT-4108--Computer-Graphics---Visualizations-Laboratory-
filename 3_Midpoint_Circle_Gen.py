import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

def midpoint_circle(radius, xc=0, yc=0):

    if radius <= 0:
        print("Radius must be positive.")
        return

    x, y = 0, radius
    p = 1 - radius
    step = 1

    plt.figure(figsize=(8,8))

    # 🔵 Smooth circle (reference)
    theta = np.linspace(0, 2*np.pi, 400)
    cx = xc + radius * np.cos(theta)
    cy = yc + radius * np.sin(theta)
    plt.plot(cx, cy, color='white', linewidth=1.5, label="Actual Circle")

    while x <= y:

        # 🔹 Classification + Color
        if p < 0:
            status = "Inside"
            color = 'green'
        elif p == 0:
            status = "On Circle"
            color = 'blue'
        else:
            status = "Outside"
            color = 'red'

        symmetric_points = [
            ( x + xc,  y + yc),
            ( y + xc,  x + yc),
            (-x + xc,  y + yc),
            (-y + xc,  x + yc),
            (-x + xc, -y + yc),
            (-y + xc, -x + yc),
            ( x + xc, -y + yc),
            ( y + xc, -x + yc)
        ]

        # 🔥 Terminal Output
        print(f"\nStep {step}: (x={x}, y={y}, p={p}) → {status}")
        print("8 Symmetric Points:")

        for i, pt in enumerate(symmetric_points):
            print(f"  P{i+1}: {pt}")

            plt.scatter(pt[0], pt[1],
                        color=color,
                        s=70,
                        edgecolors='white')

        # 🔹 Update
        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1

        x += 1
        step += 1

    # 🔹 Center
    plt.scatter(xc, yc, color='yellow', s=120, label="Center")

    # 🔹 Legend
    plt.scatter([], [], color='green', label="Inside (p<0)")
    plt.scatter([], [], color='blue', label="On (p=0)")
    plt.scatter([], [], color='red', label="Outside (p>0)")

    plt.title("Midpoint Circle (Final Clean Version)", fontsize=14)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.axis("equal")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()

    plt.show()


# 🔹 Run
r = int(input("Enter radius: "))
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))

midpoint_circle(r, xc, yc)