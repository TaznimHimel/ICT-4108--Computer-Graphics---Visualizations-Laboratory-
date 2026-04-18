import matplotlib.pyplot as plt

def midpoint_ellipse(a, b, xc=0, yc=0):

    # 🔹 Validation
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive.")
    
    x = 0
    y = int(b)

    a2 = a * a
    b2 = b * b

    points = set()  # 🔹 remove duplicates

    print("\n--- Midpoint Ellipse Output ---")

    # ---------------------------
    # REGION 1
    # ---------------------------
    p1 = b2 - (a2 * b) + (0.25 * a2)

    while (2 * b2 * x) < (2 * a2 * y):
        print(f"(x={x}, y={y}), p1={p1:.2f}")

        # 4-way symmetry
        symmetric = [
            ( xc + x, yc + y),
            ( xc - x, yc + y),
            ( xc + x, yc - y),
            ( xc - x, yc - y)
        ]

        for pt in symmetric:
            points.add(pt)

        if p1 < 0:
            x += 1
            p1 += 2 * b2 * x + b2
        else:
            x += 1
            y -= 1
            p1 += 2 * b2 * x - 2 * a2 * y + b2

    # ---------------------------
    # REGION 2
    # ---------------------------
    p2 = (b2 * (x + 0.5)**2) + (a2 * (y - 1)**2) - (a2 * b2)

    while y >= 0:
        print(f"(x={x}, y={y}), p2={p2:.2f}")

        symmetric = [
            ( xc + x, yc + y),
            ( xc - x, yc + y),
            ( xc + x, yc - y),
            ( xc - x, yc - y)
        ]

        for pt in symmetric:
            points.add(pt)

        if p2 > 0:
            y -= 1
            p2 += -2 * a2 * y + a2
        else:
            x += 1
            y -= 1
            p2 += 2 * b2 * x - 2 * a2 * y + a2

    return list(points)


# ==============================
#        MAIN PROGRAM
# ==============================
try:
    a = float(input("Enter semi-major axis (a): "))
    b = float(input("Enter semi-minor axis (b): "))

    if a > 1000 or b > 1000:
        raise ValueError("Use values below 1000")

    points = midpoint_ellipse(a, b, xc=0, yc=0)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys)

    # 🔹 Center point
    plt.scatter(0, 0, label="Center (0,0)")

    # 🔹 Labels (optional)
    for (x, y) in points:
        plt.text(x, y, f"({int(x)},{int(y)})", fontsize=6)

    # 🔹 Better visualization
    plt.axis("equal")
    plt.title(f"Midpoint Ellipse (a={a}, b={b})")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.legend()

    plt.show()

except Exception as e:
    print("Error:", e)


# Enter semi-major axis (a): 8
# Enter semi-minor axis (b): 5