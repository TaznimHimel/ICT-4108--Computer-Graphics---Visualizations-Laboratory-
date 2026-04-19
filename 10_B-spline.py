import math
import matplotlib.pyplot as plt


def clamp_int(value, min_val, max_val, default):
    """Convert to int and clamp between min_val and max_val."""
    try:
        v = int(value)
        if v < min_val:
            return min_val
        if v > max_val:
            return max_val
        return v
    except:
        return default


def clamp_float(value, default):
    """Convert to float safely."""
    try:
        return float(value)
    except:
        return default


def generate_open_uniform_knot_vector(n, p):
    """
    n = number of control points - 1
    p = degree

    Total knots = n + p + 2  (m+1)
    Open uniform: first p+1 knots = 0, last p+1 knots = 1
    """
    m = n + p + 1  # last index of knot vector
    U = [0.0] * (p + 1)

    interior_count = (m + 1) - 2 * (p + 1)
    if interior_count > 0:
        for j in range(1, interior_count + 1):
            U.append(j / (interior_count + 1))

    U += [1.0] * (p + 1)
    return U


def N(i, p, u, U):
    """
    Cox–de Boor recursion for B-spline basis function N_{i,p}(u)
    """
    # base case
    if p == 0:
        # Important edge case at u=1.0
        if (U[i] <= u < U[i + 1]) or (math.isclose(u, U[-1]) and math.isclose(U[i + 1], U[-1])):
            return 1.0
        return 0.0

    denom1 = U[i + p] - U[i]
    denom2 = U[i + p + 1] - U[i + 1]

    term1 = 0.0
    term2 = 0.0

    if denom1 != 0:
        term1 = ((u - U[i]) / denom1) * N(i, p - 1, u, U)

    if denom2 != 0:
        term2 = ((U[i + p + 1] - u) / denom2) * N(i + 1, p - 1, u, U)

    return term1 + term2


def bspline_curve_points(control_points, degree, num_samples=200):
    """
    Returns curve points list using basis function summation:
    C(u) = sum N_{i,p}(u) * P_i
    """
    # Edge cases
    if not control_points:
        raise ValueError("No control points provided.")

    if num_samples < 2:
        raise ValueError("Number of samples must be >= 2.")

    n = len(control_points) - 1
    p = degree

    if p < 1:
        raise ValueError("Degree must be >= 1.")

    if p > n:
        raise ValueError(f"Degree p={p} cannot exceed n={n} (control points - 1).")

    U = generate_open_uniform_knot_vector(n, p)

    u_start = U[p]
    u_end = U[n + 1]  # end of valid domain

    curve = []
    for s in range(num_samples):
        # Parameter in [u_start, u_end]
        u = u_start + (u_end - u_start) * (s / (num_samples - 1))

        x = 0.0
        y = 0.0
        for i in range(n + 1):
            b = N(i, p, u, U)
            x += b * control_points[i][0]
            y += b * control_points[i][1]

        curve.append((x, y))

    return curve, U


def read_control_points():
    print("Enter control points (x y) one per line.")
    print("Type 'done' when finished.\nExample:")
    print("0 0\n1 2\n3 3\ndone\n")

    pts = []
    while True:
        line = input("Point: ").strip()

        if line.lower() in ("done", "end", "finish"):
            break

        parts = line.split()
        if len(parts) != 2:
            print(" Invalid format. Enter exactly: x y")
            continue

        x = clamp_float(parts[0], None)
        y = clamp_float(parts[1], None)
        if x is None or y is None:
            print(" Invalid numbers. Try again.")
            continue

        pts.append((x, y))

    return pts


def main():
    print("=" * 60)
    print(" B-SPLINE CURVE GENERATOR (User Input + Edge Cases)")
    print("=" * 60)

    control_points = read_control_points()

    if len(control_points) < 2:
        print("\n Need at least 2 control points to draw anything.")
        return

    max_degree = len(control_points) - 1

    deg_in = input(f"\nEnter degree p (1 to {max_degree}, recommended 3): ").strip()
    degree = clamp_int(deg_in, 1, max_degree, default=min(3, max_degree))

    samp_in = input("Enter number of samples/points on curve (>=2, recommended 200): ").strip()
    num_samples = clamp_int(samp_in, 2, 20000, default=200)

    try:
        curve, U = bspline_curve_points(control_points, degree, num_samples)

        # Plotting
        cx, cy = zip(*curve)
        px, py = zip(*control_points)

        plt.figure(figsize=(8, 6))
        plt.plot(px, py, 'o--', label="Control Polygon")
        plt.plot(cx, cy, '-', linewidth=2, label=f"B-spline Curve (degree={degree})")

        plt.title("B-spline Curve using Cox–de Boor recursion")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.legend()
        plt.axis("equal")
        plt.show()

        # Display knot vector
        print("\n Knot vector (open uniform):")
        print(U)

    except Exception as e:
        print("\n Error:", e)


if __name__ == "__main__":
    main()





# Point: 0 0
# Point: 1 3
# Point: 3 5
# Point: 6 4
# Point: 8 0
# Point: done

# Enter degree p (1 to 4, recommended 3): 3
# Enter number of samples/points on curve (>=2, recommended 200): 300




# Example Inputs
# 🔹 Example 1: Smooth B-Spline Curve (Best ⭐)
# Point: 0 0
# Point: 1 3
# Point: 3 5
# Point: 6 4
# Point: 8 0
# Point: done

# Enter degree p: 3
# Enter number of samples: 300

# 👉 Result:

# Smooth curve passing near control points
# Does NOT pass through all points (important!)
# 🔹 Example 2: Low Degree (Linear B-Spline)
# Points:
# 0 0
# 2 2
# 4 0
# done

# Degree: 1
# Samples: 100

# 👉 Result:

# Straight segments (like polyline)
# 🔹 Example 3: Quadratic Curve
# Points:
# 0 0
# 2 5
# 5 5
# 8 0
# done

# Degree: 2
# Samples: 200

# 👉 Result:

# Smooth curve (less smooth than cubic)
# 🔹 Example 4: High Degree (Max)
# Points:
# 0 0
# 2 3
# 4 5
# 6 4
# 8 2
# 10 0
# done

# Degree: 5
# Samples: 300

# 👉 Result:

# Very smooth curve
# More influence from all control points
# 🔹 Example 5: Edge Case (Too Few Points)
# Point: 1 1
# Point: done

# 👉 Output:

# Need at least 2 control points 