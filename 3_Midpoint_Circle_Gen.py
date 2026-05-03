import matplotlib.pyplot as plt
import numpy as np

# 🔥 সুন্দর look এর জন্য
plt.style.use('seaborn-v0_8')
plt.style.use('dark_background')

def midpoint_circle(radius, xc=0, yc=0):

    if radius <= 0:
        print("Radius must be positive.")
        return

    x, y = 0, radius
    p = 1 - radius
    step = 1

    colors = ['red', 'orange', 'green', 'blue',
              'purple', 'brown', 'pink', 'cyan']

    plt.figure(figsize=(7,7))

    # 🔵 smooth circle boundary (visual beauty)
    theta = np.linspace(0, 2*np.pi, 400)
    cx = xc + radius * np.cos(theta)
    cy = yc + radius * np.sin(theta)
    plt.plot(cx, cy, color='white', linewidth=1.5, label="Actual Circle")

    while x <= y:

        # 🔹 Classification
        if p < 0:
            status = "Inside"
        elif p == 0:
            status = "On Circle"
        else:
            status = "Outside"

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

        # 🔥 Terminal output
        print(f"\nStep {step}: (x={x}, y={y}, p={p}) → {status}")
        print("8 Symmetric Points:")

        for i, pt in enumerate(symmetric_points):
            print(f"  P{i+1}: {pt}")

            # plot (same logic, just cleaner)
            plt.scatter(pt[0], pt[1],
                        color=colors[i],
                        s=60,
                        alpha=0.9)

        # 🔹 Update
        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1

        x += 1
        step += 1

    # Center
    plt.scatter(xc, yc, color='yellow', s=100, label="Center")

    # 🔹 Legend (classification meaning)
    plt.scatter([], [], color='green', label="Inside (p<0)")
    plt.scatter([], [], color='blue', label="On (p=0)")
    plt.scatter([], [], color='red', label="Outside (p>0)")

    plt.title("Midpoint Circle (Beautiful + Classified)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.grid(True, linestyle='--', alpha=0.4)

    plt.legend()
    plt.show()


# 🔹 Run
r = int(input("Enter radius: "))
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))

midpoint_circle(r, xc, yc)