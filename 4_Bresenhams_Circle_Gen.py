import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

def bresenhams_circle(radius, xc=0, yc=0):

    if radius <= 0:
        print("Radius must be positive.")
        return

    x, y = 0, radius
    p = 3 - 2 * radius
    step = 1

    plt.figure(figsize=(8,8))

    # 🔵 Smooth circle reference
    theta = np.linspace(0, 2*np.pi, 400)
    cx = xc + radius * np.cos(theta)
    cy = yc + radius * np.sin(theta)
    plt.plot(cx, cy, color='white', linewidth=1.5, label="Actual Circle")

    while x <= y:

        # 🔹 Classification
        if p < 0:
            status = "Inside"
            color = 'green'
        elif p == 0:
            status = "On Circle"
            color = 'blue'
        else:
            status = "Outside"
            color = 'red'

        # 🔥 Use set → avoid duplicates
        symmetric_points = {
            ( x + xc,  y + yc),
            ( y + xc,  x + yc),
            (-x + xc,  y + yc),
            (-y + xc,  x + yc),
            (-x + xc, -y + yc),
            (-y + xc, -x + yc),
            ( x + xc, -y + yc),
            ( y + xc, -x + yc)
        }

        print(f"\nStep {step}: (x={x}, y={y}, p={p}) → {status}")
        print("Symmetric Points:")

        for i, pt in enumerate(symmetric_points):
            print(f"  P{i+1}: {pt}")

            plt.scatter(pt[0], pt[1],
                        color=color,
                        s=80,
                        edgecolors='white',
                        linewidth=0.7)

        # 🔹 Update
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1

        x += 1
        step += 1

    # 🔹 Center
    plt.scatter(xc, yc, color='yellow', s=130, label="Center")

    # 🔹 Axis limits (important for beauty)
    plt.xlim(xc - radius - 2, xc + radius + 2)
    plt.ylim(yc - radius - 2, yc + radius + 2)

    # 🔹 Legend
    plt.scatter([], [], color='green', label="Inside (p<0)")
    plt.scatter([], [], color='blue', label="On (p=0)")
    plt.scatter([], [], color='red', label="Outside (p>0)")

    plt.title("Bresenham's Circle (Final Exam Version)", fontsize=15)
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

bresenhams_circle(r, xc, yc)