import matplotlib.pyplot as plt

INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8


def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code


def cohen_sutherland(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    out1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
    out2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)

    while True:
        if out1 == 0 and out2 == 0:
            return True, x1, y1, x2, y2

        if out1 & out2:
            return False, x1, y1, x2, y2

        out = out1 if out1 != 0 else out2

        if out & TOP:
            x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
            y = ymax
        elif out & BOTTOM:
            x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
            y = ymin
        elif out & RIGHT:
            y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            x = xmax
        elif out & LEFT:
            y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
            x = xmin

        if out == out1:
            x1, y1 = x, y
            out1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            out2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)


# 🔹 Main
xmin = float(input("xmin: "))
ymin = float(input("ymin: "))
xmax = float(input("xmax: "))
ymax = float(input("ymax: "))

n = int(input("Number of lines: "))
if n <= 0:
    print("Invalid number of lines!")
    exit()

lines = []
for i in range(n):
    print(f"\nLine {i+1}")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    lines.append((x1, y1, x2, y2))


# 🔹 Plot
plt.figure(figsize=(7,7))

# Window
plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin],
         'k-', label="Window")

colors = ['r', 'g', 'b', 'm', 'c', 'y']

for i, (x1, y1, x2, y2) in enumerate(lines):
    color = colors[i % len(colors)]

    accept, cx1, cy1, cx2, cy2 = cohen_sutherland(
        x1, y1, x2, y2, xmin, ymin, xmax, ymax
    )

    # Original
    plt.plot([x1,x2],[y1,y2], linestyle='--', color=color)

    # Clipped
    if accept:
        plt.plot([cx1,cx2],[cy1,cy2], color=color, linewidth=2)
    else:
        print(f"Line {i+1} rejected")


plt.title("Cohen–Sutherland Line Clipping")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()






# Example Input:
# xmin: 10
# ymin: 10
# xmax: 30
# ymax: 30

# How many lines? 4

# Line 1 → Completely inside
# (12,15) → (25,28)

# Line 2 → Completely outside
# (0,0) → (5,5)

# Line 3 → Partially inside
# (5,5) → (25,25)

# Line 4 → Crossing window
# (20,40) → (20,0)