import matplotlib.pyplot as plt

def midpoint_circle(radius, xc=0, yc=0):

    # 🔹 Validate radius
    if radius <= 0:
        print("Error: Radius must be a positive number.")
        return

    x, y = 0, radius
    p = 3 - 2 * radius

    points = set()  # 🔹 remove duplicates

    print(f"\n--- Midpoint Circle Algorithm Output ---")
    print(f"Center: ({xc}, {yc})")
    print(f"Radius: {radius}")
    print("\n  x\t  y\t  p-value\tDecision")

    while x <= y:
        decision = "E" if p < 0 else "SE"
        print(f"{x:3d}\t{y:3d}\t{p:8.2f}\t{decision}")

        # 🔹 8-way symmetry
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

        for pt in symmetric_points:
            points.add(pt)

        # 🔹 Update decision parameter (integer version)
        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1

        x += 1

    # Convert set → list
    points = list(points)

    # Separate coordinates
    xs = [pt[0] for pt in points]
    ys = [pt[1] for pt in points]

    # 🔹 Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys)

    # 🔹 Center point
    plt.scatter(xc, yc, label=f"Center ({xc},{yc})")

    # 🔹 Add labels (optional but useful)
    for (x, y) in points:
        plt.text(x, y, f"({x},{y})", fontsize=7)

    # 🔹 Better visualization
    plt.axis("equal")
    plt.title(f"Midpoint Circle (Integer) r={radius}, center=({xc},{yc})")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()

    plt.show()


# ---- Main Execution ----
try:
    r = int(input("Enter radius: "))
    xc = int(input("Enter X-coordinate of center: "))
    yc = int(input("Enter Y-coordinate of center: "))

    midpoint_circle(r, xc, yc)

except ValueError:
    print("Invalid input. Please enter integer values only.")
except Exception as e:
    print(f"Unexpected error: {e}")


# Enter radius: 6
# Enter X-coordinate of center: 0
# Enter Y-coordinate of center: 0