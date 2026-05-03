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


# ----------------- Default Transformations (Option 1) ----------------- #

def get_default_transformations():
    return [
        ("Translation (2,2)", get_translation_matrix(2, 2)),
        ("Scaling (1.5,1.5)", get_scaling_matrix(1.5, 1.5)),
        ("Rotation (45°)", get_rotation_matrix(45)),
        ("Shearing (1,0)", get_shear_matrix(1, 0)),
        ("Reflection (x-axis)", get_reflection_matrix('x')),
        # ("Reflection (y-axis)", get_reflection_matrix('y'))
    ]


def apply_with_labels(points, transformations):
    steps = [("Original", points)]
    current = points

    for name, matrix in transformations:
        current = apply_transformation(current, matrix)
        steps.append((name, current))

    return steps


# ----------------- Subplot Visualization ----------------- #

def plot_all_transformations_subplots(steps):
    n = len(steps)
    cols = 3
    rows = int(np.ceil(n / cols))

    fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))
    axes = axes.flatten()

    for i, (name, shape) in enumerate(steps):
        ax = axes[i]
        closed = np.vstack([shape, shape[0]])

        if i == 0:
            ax.plot(closed[:, 0], closed[:, 1], 'k--')
        else:
            ax.plot(closed[:, 0], closed[:, 1], 'b-', linewidth=2)

        # 🔥 ADD THIS LINE (points visible)
        ax.scatter(shape[:, 0], shape[:, 1], s=40)

        # Label points
        for (x, y) in shape:
            ax.text(x, y, f"({x:.1f},{y:.1f})", fontsize=8)

        ax.set_title(name)
        ax.axhline(0)
        ax.axvline(0)
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.set_aspect('equal')

    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()


# ----------------- Combined Transformation ----------------- #

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


# ----------------- Final Plot ----------------- #

def plot_shape(original, transformed, title="Transformation"):
    fig, ax = plt.subplots(figsize=(6, 6))

    orig = np.vstack([original, original[0]])
    trans = np.vstack([transformed, transformed[0]])

    ax.plot(orig[:, 0], orig[:, 1], 'k--', label='Original')
    ax.plot(trans[:, 0], trans[:, 1], 'r-', linewidth=2, label='Transformed')

    ax.set_title(title)
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
        [1, 3]
    ])

    print("\n==== 2D Transformation Program ====")
    print("1. Show All Transformations (Subplots)")
    print("2. Combined Transformations")

    mode = int(input("Select mode: "))

    if mode == 1:
        transformations = get_default_transformations()
        steps = apply_with_labels(shape, transformations)
        plot_all_transformations_subplots(steps)

    elif mode == 2:
        matrix = combine_transformations()
        result = apply_transformation(shape, matrix)
        plot_shape(shape, result, "Combined Transformation")

    else:
        print("Invalid option")