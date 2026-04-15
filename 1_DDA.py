import matplotlib.pyplot as plt

def DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    # 🔹 1. Handle Zero Division Cas
    if steps == 0:
        plt.plot(x1, y1, 'ro')
        plt.text(x1, y1, f"({x1},{y1})")
        plt.title("DDA Line Drawing Algorithm (Single Point)")
        plt.grid(True)
        plt.show()
        return

    # Calculate increment values
    Xinc = dx / steps
    Yinc = dy / steps

    # Starting point
    x = x1
    y = y1

    x_points = []
    y_points = []

    # Generate points
    for i in range(steps + 1):
        x_rounded = round(x)
        y_rounded = round(y)
        x_points.append(x_rounded)
        y_points.append(y_rounded)

        x += Xinc
        y += Yinc

    # Plot the line
    plt.plot(x_points, y_points, 'ro-')

    # 🔹 2. Better Visualization
    plt.axis('equal')

    # 🔹 3. Add Labels to Points
    for i in range(len(x_points)):
        plt.text(x_points[i], y_points[i], f"({x_points[i]},{y_points[i]})")

    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True)
    plt.show()


# Input from user
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

DDA(x1, y1, x2, y2)