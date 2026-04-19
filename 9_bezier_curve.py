import math
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Safe Input Helpers
# -----------------------------
def safe_float(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if min_val is not None and v < min_val:
                print(f" Must be >= {min_val}")
                continue
            if max_val is not None and v > max_val:
                print(f" Must be <= {max_val}")
                continue
            if not math.isfinite(v):
                print(" Must be finite.")
                continue
            return v
        except ValueError:
            print(" Please enter a valid number.")


def safe_yes_no(prompt):
    while True:
        s = input(prompt + " (y/n): ").strip().lower()
        if s in ("y", "yes"):
            return True
        if s in ("n", "no"):
            return False
        print(" Enter y/n.")


def read_point(name):
    while True:
        s = input(f"{name} (x y): ").strip()
        parts = s.replace(",", " ").split()
        if len(parts) != 2:
            print(" Enter two numbers like: 100 200")
            continue
        try:
            x, y = float(parts[0]), float(parts[1])
            if not (math.isfinite(x) and math.isfinite(y)):
                print(" Coordinates must be finite.")
                continue
            return (x, y)
        except ValueError:
            print(" Invalid input. Try again.")


# -----------------------------
# Math Functions
# -----------------------------
def bernstein(n, i, t):
    """B_i^n(t) = C(n,i) * (1-t)^(n-i) * t^i"""
    t = float(np.clip(t, 0.0, 1.0))
    return math.comb(n, i) * ((1 - t) ** (n - i)) * (t ** i)


def bezier_point(control_points, t):
    """P(t) = Σ B_i^n(t) * P_i"""
    n = len(control_points) - 1
    x, y = 0.0, 0.0
    for i, (px, py) in enumerate(control_points):
        b = bernstein(n, i, t)
        x += b * px
        y += b * py
    return x, y


def sample_curve(control_points, step):
    """Sample Bezier curve points in [0,1]"""
    if step <= 0:
        raise ValueError("Step must be > 0")
    if step > 1:
        ts = np.array([0.0, 1.0])
    else:
        ts = np.arange(0.0, 1.0 + 1e-12, step)
        if ts[-1] < 1.0:
            ts = np.append(ts, 1.0)

    pts = np.array([bezier_point(control_points, t) for t in ts], dtype=float)
    return pts


def degenerate_case(points):
    unique = set(points)
    if len(unique) == 1:
        return "ALL_SAME"
    if len(unique) == 2:
        return "TWO_UNIQUE"
    return "NORMAL"


# -----------------------------
# Main: One Graph, 3 Curves
# -----------------------------
def main():
    print("======================================================")
    print("Bezier Curves (Linear + Quadratic + Cubic) One Graph")
    print("Using Bernstein / Blending Functions")
    print("======================================================\n")

    # Input points
    print(" Input Control Points")
    print("We will use 4 points total:")
    print("Linear uses:    P0, P1")
    print("Quadratic uses: P0, P1, P2")
    print("Cubic uses:     P0, P1, P2, P3\n")

    P0 = read_point("P0")
    P1 = read_point("P1")
    P2 = read_point("P2")
    P3 = read_point("P3")

    step = safe_float("\nEnter step size Δt (recommended 0.001 to 0.02): ", min_val=1e-6, max_val=1.0)
    show_grid = safe_yes_no("Show grid?")
    show_polygons = safe_yes_no("Show control polygons?")

    # Build control point lists
    linear_pts = [P0, P1]
    quad_pts = [P0, P1, P2]
    cubic_pts = [P0, P1, P2, P3]

    # Edge case messages
    print("\ Checking edge cases...")
    for name, pts in [("Linear", linear_pts), ("Quadratic", quad_pts), ("Cubic", cubic_pts)]:
        case = degenerate_case(pts)
        if case == "ALL_SAME":
            print(f"  - {name}: All control points identical → curve collapses to a point.")
        elif case == "TWO_UNIQUE" and len(pts) > 2:
            print(f"  - {name}: Only two unique points → curve may behave like a line.")
        else:
            print(f"  - {name}: OK")

    # Sample curves
    try:
        L = sample_curve(linear_pts, step)
        Q = sample_curve(quad_pts, step)
        C = sample_curve(cubic_pts, step)
    except Exception as e:
        print(f" Sampling failed: {e}")
        return

    # Plot
    plt.figure(figsize=(11, 7))
    plt.title("Linear, Quadratic & Cubic Bezier Curves (Blending Functions)")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Draw the curves (different styles)
    plt.plot(L[:, 0], L[:, 1], linewidth=2, label="Linear (Degree 1)")
    plt.plot(Q[:, 0], Q[:, 1], linewidth=2, label="Quadratic (Degree 2)")
    plt.plot(C[:, 0], C[:, 1], linewidth=2, label="Cubic (Degree 3)")

    # Control polygons (optional)
    if show_polygons:
        # P0->P1 (linear)
        lp = np.array(linear_pts, dtype=float)
        plt.plot(lp[:, 0], lp[:, 1], marker="o", linestyle="--", linewidth=1, label="Control Polygon (Linear)")

        # P0->P1->P2 (quadratic)
        qp = np.array(quad_pts, dtype=float)
        plt.plot(qp[:, 0], qp[:, 1], marker="o", linestyle="--", linewidth=1, label="Control Polygon (Quadratic)")

        # P0->P1->P2->P3 (cubic)
        cp = np.array(cubic_pts, dtype=float)
        plt.plot(cp[:, 0], cp[:, 1], marker="o", linestyle="--", linewidth=1, label="Control Polygon (Cubic)")

    # Label control points
    for i, p in enumerate([P0, P1, P2, P3]):
        plt.scatter(p[0], p[1])
        plt.text(p[0], p[1], f"  P{i}", fontsize=10)

    if show_grid:
        plt.grid(True)

    plt.legend()
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()



# 🔹 Example 1: Basic Smooth Curve (Recommended ⭐)
# P0 (x y): 0 0
# P1 (x y): 2 5
# P2 (x y): 5 5
# P3 (x y): 7 0

# Enter step size Δt: 0.01
# Show grid? y
# Show control polygons? y

# 👉 Result:

# Linear → straight line
# Quadratic → curved line
# Cubic → smooth S-like curve

# 🔹 Example 2: Straight Line Case
# P0: 0 0
# P1: 2 2
# P2: 4 4
# P3: 6 6

# Δt: 0.01
# Grid: y
# Polygons: y

# 👉 Result:

# All curves become straight line
# ✔ Because all points are collinear
# 🔹 Example 3: Curve Bending Downward
# P0: 0 0
# P1: 3 -5
# P2: 6 -5
# P3: 9 0

# Δt: 0.01
# Grid: y
# Polygons: y

# 👉 Result:

# Curve bends downward
# 🔹 Example 4: Sharp Curve
# P0: 0 0
# P1: 0 10
# P2: 10 10
# P3: 10 0

# Δt: 0.005
# Grid: y
# Polygons: y

# 👉 Result:

# Strong curved shape (almost rectangular arc)