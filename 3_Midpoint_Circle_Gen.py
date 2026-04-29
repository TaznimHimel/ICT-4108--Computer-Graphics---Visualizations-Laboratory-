import matplotlib.pyplot as plt

def midpoint_circle(radius, xc=0, yc=0):

    if radius <= 0:
        print("Radius must be positive.")
        return

    x, y = 0, radius
    p = 1 - radius
    step = 1

    # 🎨 Colors for 8 octants
    colors = ['red', 'orange', 'green', 'blue',
              'purple', 'brown', 'pink', 'cyan']

    plt.figure(figsize=(6,6))

    while x <= y:

        symmetric_points = [
            ( x + xc,  y + yc),   # 1
            ( y + xc,  x + yc),   # 2
            (-x + xc,  y + yc),   # 3
            (-y + xc,  x + yc),   # 4
            (-x + xc, -y + yc),   # 5
            (-y + xc, -x + yc),   # 6
            ( x + xc, -y + yc),   # 7
            ( y + xc, -x + yc)    # 8
        ]

        print(f"\nStep {step}: (x={x}, y={y}, p={p})")
        print("8 Symmetric Points:")

        for i, pt in enumerate(symmetric_points):
            print(f"  P{i+1}: {pt}")

            # 🔹 Plot each point with different color
            plt.scatter(pt[0], pt[1], color=colors[i])

            # 🔹 Label each point
            plt.text(pt[0], pt[1], f"{pt}", fontsize=7)

        # Update decision parameter
        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1

        x += 1
        step += 1

    # Center
    plt.scatter(xc, yc, color='black', s=60, label="Center")

    plt.title(f"Midpoint Circle (Step-wise Octants)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.axis("equal")
    plt.grid(True)

    plt.show()


# Run
r = int(input("Enter radius: "))
xc = int(input("Enter center x: "))
yc = int(input("Enter center y: "))

midpoint_circle(r, xc, yc)