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
            return "Accepted", x1, y1, x2, y2

        if out1 & out2:
            return "Rejected", x1, y1, x2, y2

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


# 🔹 Input
xmin = float(input("xmin: "))
ymin = float(input("ymin: "))
xmax = float(input("xmax: "))
ymax = float(input("ymax: "))

n = int(input("Number of lines: "))

lines = []
for i in range(n):
    print(f"\nLine {i+1}")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    lines.append((x1, y1, x2, y2))


# 🔹 Plot
plt.figure(figsize=(9,9))

# Window (thick)
plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin],
         color='black', linewidth=3)

# Expand limits for better spacing
margin_x = (xmax - xmin) * 0.4
margin_y = (ymax - ymin) * 0.4
plt.xlim(xmin - margin_x, xmax + margin_x)
plt.ylim(ymin - margin_y, ymax + margin_y)


# 🔹 Boundary Labels (BIG + CLEAR)
mid_x = (xmin + xmax)/2
mid_y = (ymin + ymax)/2

plt.text(mid_x, ymax + margin_y*0.3, "TOP", ha='center', fontsize=12, weight='bold')
plt.text(mid_x, ymin - margin_y*0.3, "BOTTOM", ha='center', fontsize=12, weight='bold')
plt.text(xmin - margin_x*0.3, mid_y, "LEFT", va='center', rotation=90, fontsize=12, weight='bold')
plt.text(xmax + margin_x*0.3, mid_y, "RIGHT", va='center', rotation=90, fontsize=12, weight='bold')


# 🔹 Region Codes (BOX STYLE)
def region_label(x, y, text, color='darkred'):
    plt.text(x, y, text,
             fontsize=10,
             ha='center',
             bbox=dict(facecolor='white', edgecolor=color, boxstyle='round,pad=0.3'))

offset_x = margin_x * 0.5
offset_y = margin_y * 0.5

# Top
region_label(mid_x, ymax + offset_y, "1000")
region_label(xmin - offset_x, ymax + offset_y, "1001")
region_label(xmax + offset_x, ymax + offset_y, "1010")

# Middle
region_label(xmin - offset_x, mid_y, "0001")
region_label(mid_x, mid_y, "0000", color='green')
region_label(xmax + offset_x, mid_y, "0010")

# Bottom
region_label(mid_x, ymin - offset_y, "0100")
region_label(xmin - offset_x, ymin - offset_y, "0101")
region_label(xmax + offset_x, ymin - offset_y, "0110")


# 🔹 Lines
colors = ['red','green','blue','magenta','cyan']

for i,(x1,y1,x2,y2) in enumerate(lines):
    color = colors[i % len(colors)]

    status, cx1, cy1, cx2, cy2 = cohen_sutherland(
        x1,y1,x2,y2,xmin,ymin,xmax,ymax
    )

    # Original
    plt.plot([x1,x2],[y1,y2],'--',color=color,alpha=0.5)

    # Points
    plt.scatter([x1,x2],[y1,y2],color=color,s=40)

    if status != "Rejected":
        # Clipped
        plt.plot([cx1,cx2],[cy1,cy2],color=color,linewidth=3)

        # Highlight intersection
        plt.scatter([cx1,cy1],[cy1,cy2])  # (ignore if typo earlier)
        plt.scatter([cx1,cx2],[cy1,cy2],color='yellow',edgecolor='black',s=80,zorder=5)


# 🔹 Final Styling
plt.title("Cohen–Sutherland Line Clipping\n(Enhanced Visualization)",
          fontsize=15, weight='bold')

plt.grid(True, linestyle='--', alpha=0.4)
plt.axis('equal')

plt.show()




# xmin: 10
# ymin: 10
# xmax: 30
# ymax: 30
# Number of lines: 5

# Line 1
# x1: 12
# y1: 15
# x2: 25
# y2: 28

# Line 2
# x1: 0
# y1: 0
# x2: 5
# y2: 5

# Line 3
# x1: 6
# y1: 6
# x2: 25
# y2: 25

# Line 4
# x1: 20
# y1: 40
# x2: 20
# y2: 0

# Line 5
# x1: 0
# y1: 20
# x2: 40
# y2: 20