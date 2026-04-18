import matplotlib.pyplot as plt

# ---------------- Cohen–Sutherland Constants ---------------- #

INSIDE = 0
LEFT   = 1
RIGHT  = 2
BOTTOM = 4
TOP    = 8


# ---------------- Utility Input Functions ---------------- #

def input_float(prompt, default=None):
    """
    Safely read a float from the user.
    If the user just presses Enter and a default is given, return the default.
    Keeps asking until a valid float is entered.
    """
    while True:
        text = input(prompt)
        if text.strip() == "":
            if default is not None:
                return default
            else:
                print("Please enter a number.")
                continue
        try:
            return float(text)
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def input_yes_no(prompt, default="y"):
    """
    Simple yes/no input with default option.
    """
    while True:
        text = input(prompt).strip().lower()
        if text == "" and default is not None:
            return default.lower() == "y"
        if text in ["y", "yes"]:
            return True
        if text in ["n", "no"]:
            return False
        print("Please answer with 'y' or 'n'.")
        

# ---------------- Cohen–Sutherland Core Functions ---------------- #

def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP
    return code


def cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    """
    Perform Cohen–Sutherland line clipping.
    Returns (accept, x1c, y1c, x2c, y2c)
    If accept is False, the line is completely outside or invalid.
    """
    # Degenerate case: both endpoints same
    if x1 == x2 and y1 == y2:
        # Just check if the point itself is inside
        code = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
        if code == INSIDE:
            return True, x1, y1, x2, y2
        else:
            return False, x1, y1, x2, y2

    outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
    outcode2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)
    accept = False

    while True:
        # Trivial accept
        if outcode1 == 0 and outcode2 == 0:
            accept = True
            break

        # Trivial reject
        if (outcode1 & outcode2) != 0:
            break

        # Pick an endpoint that is outside the window
        outcode_out = outcode1 if outcode1 != 0 else outcode2

        x = y = None

        # Now find intersection with relevant boundary
        # Be careful about division by zero

        if outcode_out & TOP:  # above window: y = ymax
            dy = (y2 - y1)
            if dy == 0:
                # Line is horizontal; can't intersect top
                return False, x1, y1, x2, y2
            x = x1 + (x2 - x1) * (ymax - y1) / dy
            y = ymax

        elif outcode_out & BOTTOM:  # below window: y = ymin
            dy = (y2 - y1)
            if dy == 0:
                # Line is horizontal; can't intersect bottom
                return False, x1, y1, x2, y2
            x = x1 + (x2 - x1) * (ymin - y1) / dy
            y = ymin

        elif outcode_out & RIGHT:  # right of window: x = xmax
            dx = (x2 - x1)
            if dx == 0:
                # Line is vertical; can't intersect right side properly
                return False, x1, y1, x2, y2
            y = y1 + (y2 - y1) * (xmax - x1) / dx
            x = xmax

        elif outcode_out & LEFT:  # left of window: x = xmin
            dx = (x2 - x1)
            if dx == 0:
                # Line is vertical; can't intersect left side properly
                return False, x1, y1, x2, y2
            y = y1 + (y2 - y1) * (xmin - x1) / dx
            x = xmin

        # If something went wrong
        if x is None or y is None:
            return False, x1, y1, x2, y2

        # Replace the outside point with the intersection point
        if outcode_out == outcode1:
            x1, y1 = x, y
            outcode1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
        else:
            x2, y2 = x, y
            outcode2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)

    return accept, x1, y1, x2, y2


# ---------------- Plotting Function ---------------- #

def plot_clipping(x1, y1, x2, y2, xmin, ymin, xmax, ymax, accept, cx1, cy1, cx2, cy2):
    plt.figure(figsize=(7, 7))

    # Draw clipping window
    plt.plot(
        [xmin, xmax, xmax, xmin, xmin],
        [ymin, ymin, ymax, ymax, ymin],
        label="Clipping Window"
    )

    # Original line (dashed)
    plt.plot([x1, x2], [y1, y2], linestyle="--", label="Original Line")

    # Clipped line (if accepted)
    if accept:
        plt.plot([cx1, cx2], [cy1, cy2], linewidth=2, label="Clipped Line")
    else:
        plt.text(
            xmin, ymax + (ymax - ymin) * 0.1,
            "Line Rejected",
            fontsize=12
        )

    # Make axes a bit larger than window for clarity
    x_margin = (xmax - xmin) * 0.5 if xmax != xmin else 10
    y_margin = (ymax - ymin) * 0.5 if ymax != ymin else 10

    plt.xlim(min(xmin, x1, x2) - x_margin, max(xmax, x1, x2) + x_margin)
    plt.ylim(min(ymin, y1, y2) - y_margin, max(ymax, y1, y2) + y_margin)

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Cohen–Sutherland Line Clipping (User Input Demo)")
    plt.legend()
    plt.grid(True)
    plt.show()


# ---------------- Main Program ---------------- #

def main():
    print("=== Cohen–Sutherland Line Clipping (with User Input) ===")
    print("Press Enter to use the default value shown in [brackets].\n")

    # Default window
    default_xmin, default_ymin = 10.0, 10.0
    default_xmax, default_ymax = 30.0, 30.0

    # Default line
    default_x1, default_y1 = 5.0, 5.0
    default_x2, default_y2 = 40.0, 25.0

    while True:
        print("\n--- Enter Clipping Window Coordinates ---")
        xmin = input_float(f"xmin [{default_xmin}]: ", default_xmin)
        ymin = input_float(f"ymin [{default_ymin}]: ", default_ymin)
        xmax = input_float(f"xmax [{default_xmax}]: ", default_xmax)
        ymax = input_float(f"ymax [{default_ymax}]: ", default_ymax)

        # Validate window
        if xmin >= xmax or ymin >= ymax:
            print(" Invalid window! Must have xmin < xmax and ymin < ymax.")
            print("Please re-enter the window coordinates.")
            continue

        print("\n--- Enter Line Endpoints ---")
        x1 = input_float(f"x1 [{default_x1}]: ", default_x1)
        y1 = input_float(f"y1 [{default_y1}]: ", default_y1)
        x2 = input_float(f"x2 [{default_x2}]: ", default_x2)
        y2 = input_float(f"y2 [{default_y2}]: ", default_y2)

        # Perform clipping
        accept, cx1, cy1, cx2, cy2 = cohen_sutherland_clip(
            x1, y1, x2, y2, xmin, ymin, xmax, ymax
        )

        if accept:
            print("\n Line accepted after clipping:")
            print(f"   From ({cx1:.2f}, {cy1:.2f}) to ({cx2:.2f}, {cy2:.2f})")
        else:
            print("\n Line rejected (completely outside or invalid case).")

        # Show plot
        plot_clipping(x1, y1, x2, y2, xmin, ymin, xmax, ymax, accept, cx1, cy1, cx2, cy2)

        # Ask if user wants another test
        again = input_yes_no("Do you want to try another line/window? [Y/n]: ", default="y")
        if not again:
            print("Exiting. Goodbye!")
            break


if __name__ == "__main__":
    main()


# --- Enter Clipping Window Coordinates ---
# xmin [10.0]:
# ymin [10.0]: 
# xmax [30.0]: 
# ymax [30.0]: 

# --- Enter Line Endpoints ---
# x1 [5.0]: 15
# y1 [5.0]: 40
# x2 [40.0]: 25
# y2 [25.0]: 50

# ❌ Line rejected (completely outside or invalid case).




# Example 2: Completely Inside Line
# xmin: 10
# ymin: 10
# xmax: 30
# ymax: 30

# x1: 12
# y1: 15
# x2: 25
# y2: 28

# 👉 Result:

# ✅ Line accepted after clipping:
# From (12.00, 15.00) to (25.00, 28.00)

# ✔ No clipping needed, line is fully inside the window.