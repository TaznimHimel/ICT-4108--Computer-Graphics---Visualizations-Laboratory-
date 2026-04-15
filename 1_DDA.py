import matplotlib.pyplot as plt
def DDA(x1,y1,x2,y2):
    dx =x2-x1
    dy =y2-y1
    steps = int(max(abs(dx), abs(dy)))

    # Calculate increment values
    Xinc = dx / steps
    Yinc = dy / steps

    # Starting point
    x = x1
    y = y1

    # Draw the line points
    x_points = []
    y_points = []

    for i in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += Xinc
        y += Yinc

    # Plot the line
    plt.plot(x_points, y_points, 'ro-')
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True)
    plt.show()


# Example: You can change these values
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

DDA(x1, y1, x2, y2)

# x1 = 2, y1 = 3
# x2 = 10, y2 = 8
