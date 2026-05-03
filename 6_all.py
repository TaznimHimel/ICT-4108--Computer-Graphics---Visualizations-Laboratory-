import numpy as np
import matplotlib.pyplot as plt

# ----------------- Transformation Matrices ----------------- #

def get_translation_matrix(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

def get_scaling_matrix(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

def get_rotation_matrix(degrees):
    rad = np.radians(degrees)
    return np.array([[np.cos(rad), -np.sin(rad), 0],
                     [np.sin(rad),  np.cos(rad), 0],
                     [0, 0, 1]])

def get_shear_matrix(shx, shy):
    return np.array([[1, shx, 0],
                     [shy, 1, 0],
                     [0, 0, 1]])

def get_reflection_matrix(axis='x'):
    if axis == 'x':
        return np.array([[1, 0, 0],
                         [0, -1, 0],
                         [0, 0, 1]])
    elif axis == 'y':
        return np.array([[-1, 0, 0],
                         [0, 1, 0],
                         [0, 0, 1]])
    else:
        raise ValueError("Axis must be 'x' or 'y'")


# ----------------- Apply Transformation ----------------- #

def apply_transformation(points, matrix):
    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack([points, ones])
    transformed = (matrix @ points_h.T).T
    return transformed[:, :2]


# ----------------- Clean Plot ----------------- #

def plot_shape(ax, points, label, color):
    x = points[:, 0]
    y = points[:, 1]

    # 🔥 smooth clean line (no points)
    ax.plot(x, y, color=color, linewidth=3, label=label)
    ax.fill(x, y, color=color, alpha=0.25)

    # axes
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)

    ax.set_aspect("equal")
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(fontsize=10)


# ----------------- Option 1 ----------------- #

def run_all_transformations(shape):

    translated = apply_transformation(shape, get_translation_matrix(3, 2))
    scaled = apply_transformation(shape, get_scaling_matrix(1.5, 0.5))
    rotated = apply_transformation(shape, get_rotation_matrix(45))
    sheared = apply_transformation(shape, get_shear_matrix(1, 0.2))
    reflected_x = apply_transformation(shape, get_reflection_matrix("x"))
    # reflected_y = apply_transformation(shape, get_reflection_matrix("y"))  ❌ removed

    # 🔥 global axis scale
    all_points = np.vstack([
        shape, translated, scaled,
        rotated, sheared, reflected_x
    ])

    xmin, ymin = all_points.min(axis=0) - 1
    xmax, ymax = all_points.max(axis=0) + 1

    # 🔥 bigger figure
    fig, axes = plt.subplots(2, 3, figsize=(14, 10))
    axes = axes.flatten()

    data = [
        ("Original", shape, "#2c3e50"),
        ("Translation", translated, "#e74c3c"),
        ("Scaling", scaled, "#27ae60"),
        ("Rotation", rotated, "#2980b9"),
        ("Shearing", sheared, "#8e44ad"),
        ("Reflection (X)", reflected_x, "#f39c12"),
    ]

    for i, (title, pts, color) in enumerate(data):
        ax = axes[i]
        plot_shape(ax, pts, title, color)
        ax.set_title(title, fontsize=12, weight='bold')

        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

    plt.tight_layout()
    plt.show()


# ----------------- Option 2 ----------------- #

def combine_transformations():
    print("\nHow many transformations do you want to combine?")
    n = int(input("Enter number: "))

    final_matrix = np.eye(3)

    for i in range(n):
        print(f"\nTransformation {i+1}:")
        matrix = choose_transformation()
        final_matrix = matrix @ final_matrix

    return final_matrix


def choose_transformation():
    print("\n1. Translation")
    print("2. Scaling")
    print("3. Rotation")
    print("4. Shearing")
    print("5. Reflection")

    ch = int(input("Choose: "))

    if ch == 1:
        tx = float(input("tx: "))
        ty = float(input("ty: "))
        return get_translation_matrix(tx, ty)

    elif ch == 2:
        sx = float(input("sx: "))
        sy = float(input("sy: "))
        return get_scaling_matrix(sx, sy)

    elif ch == 3:
        angle = float(input("Angle: "))
        return get_rotation_matrix(angle)

    elif ch == 4:
        shx = float(input("shear x: "))
        shy = float(input("shear y: "))
        return get_shear_matrix(shx, shy)

    elif ch == 5:
        axis = input("Axis (x/y): ").lower()
        return get_reflection_matrix(axis)

    else:
        print("Invalid choice!")
        return np.eye(3)


def plot_shape_final(original, transformed):
    fig, ax = plt.subplots(figsize=(6, 6))

    orig = np.vstack([original, original[0]])
    trans = np.vstack([transformed, transformed[0]])

    ax.plot(orig[:, 0], orig[:, 1], 'k--', linewidth=2, label='Original')
    ax.plot(trans[:, 0], trans[:, 1], 'r-', linewidth=3, label='Transformed')

    ax.set_title("Combined Transformation", fontsize=12, weight='bold')
    ax.legend()
    ax.grid(True)
    ax.set_aspect('equal')

    plt.show()


# ----------------- MAIN ----------------- #

if __name__ == "__main__":

    shape = np.array([
        [1, 1],
        [3, 1],
        [3, 3],
        [2, 4],
        [1, 3],
        [1, 1]
    ])

    print("\n==== 2D Transformation Program ====")
    print("1. Show All Transformations")
    print("2. Combined Transformations")

    mode = int(input("Select mode: "))

    if mode == 1:
        run_all_transformations(shape)

    elif mode == 2:
        matrix = combine_transformations()
        result = apply_transformation(shape, matrix)
        plot_shape_final(shape, result)

    else:
        print("Invalid option")