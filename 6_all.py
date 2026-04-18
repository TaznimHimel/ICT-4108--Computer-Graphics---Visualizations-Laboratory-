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


# ----------------- Plot Function ----------------- #

def plot_shape(original, transformed, title="Transformation"):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Close shapes
    orig = np.vstack([original, original[0]])
    trans = np.vstack([transformed, transformed[0]])

    # Plot
    ax.plot(orig[:, 0], orig[:, 1], 'k--', label='Original')
    ax.plot(trans[:, 0], trans[:, 1], 'b-', linewidth=2, label='Transformed')
    ax.fill(trans[:, 0], trans[:, 1], alpha=0.2)

    # 🔹 Labels for points
    for (x, y) in original:
        ax.text(x, y, f"({x},{y})", color='gray', fontsize=8)

    for (x, y) in transformed:
        ax.text(x, y, f"({x:.1f},{y:.1f})", color='blue', fontsize=8)

    # Axes & grid
    ax.axhline(0)
    ax.axvline(0)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_aspect('equal')

    ax.set_title(title)
    ax.legend()

    plt.show()


# ----------------- Input Helpers ----------------- #

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except:
            print("Invalid input!")

def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Invalid input!")


# ----------------- Combine Transformations 🔥 ----------------- #

def combine_transformations():
    print("\nHow many transformations do you want to combine?")
    n = input_int("Enter number: ")

    final_matrix = np.eye(3)

    for i in range(n):
        print(f"\nTransformation {i+1}:")
        matrix = choose_transformation(single=True)
        final_matrix = matrix @ final_matrix

    return final_matrix


# ----------------- Menu ----------------- #

def choose_transformation(single=False):
    print("\n1. Translation")
    print("2. Scaling")
    print("3. Rotation")
    print("4. Shearing")
    print("5. Reflection")

    ch = input_int("Choose: ")

    if ch == 1:
        tx = input_float("tx: ")
        ty = input_float("ty: ")
        return get_translation_matrix(tx, ty)

    elif ch == 2:
        sx = input_float("sx: ")
        sy = input_float("sy: ")
        return get_scaling_matrix(sx, sy)

    elif ch == 3:
        angle = input_float("Angle: ")
        return get_rotation_matrix(angle)

    elif ch == 4:
        shx = input_float("shear x: ")
        shy = input_float("shear y: ")
        return get_shear_matrix(shx, shy)

    elif ch == 5:
        axis = input("Axis (x/y): ").lower()
        return get_reflection_matrix(axis)

    else:
        print("Invalid choice!")
        return np.eye(3)


# ----------------- MAIN ----------------- #

if __name__ == "__main__":
    try:
        # Default shape (house)
        shape = np.array([
            [1, 1],
            [3, 1],
            [3, 3],
            [2, 4],
            [1, 3]
        ])

        print("\n==== 2D Transformation Program ====")
        print("1. Single Transformation")
        print("2. Combined Transformations")

        mode = input_int("Select mode: ")

        if mode == 1:
            matrix = choose_transformation()
            title = "Single Transformation"

        elif mode == 2:
            matrix = combine_transformations()
            title = "Combined Transformations"

        else:
            print("Invalid option")
            exit()

        result = apply_transformation(shape, matrix)
        plot_shape(shape, result, title)

    except Exception as e:
        print("Error:", e)



# Example Usage:
# ==== 2D Transformation Program ====
# 1. Single Transformation
# 2. Combined Transformations 🔥

# Select mode: 1

# 1. Translation
# 2. Scaling
# 3. Rotation
# 4. Shearing
# 5. Reflection

# Choose: 1
# tx: 2
# ty: 3





# Example 2: Single Transformation (Rotation)
# Select mode: 1
# Choose: 3
# Angle: 45

# 👉 Result:

# Shape rotates 45° counter-clockwise





# Example 5: Combined Transformations (BEST)
# Select mode: 2

# How many transformations do you want to combine?
# Enter number: 2

# Transformation 1:
# Choose: 3
# Angle: 45

# Transformation 2:
# Choose: 1
# tx: 2
# ty: 3

# 👉 Result:

# Shape rotates 45°
# Then moves (2,3)