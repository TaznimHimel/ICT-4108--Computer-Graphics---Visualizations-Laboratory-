import tkinter as tk

# Create window
root = tk.Tk()
root.title("Text Styles Demo")
root.geometry("600x400")

# Different text styles
tk.Label(root, text="Small Text - Red",
         fg="red",
         font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="Medium Text - Blue",
         fg="blue",
         font=("Times New Roman", 16)).pack(pady=5)

tk.Label(root, text="Large Bold Text - Green",
         fg="green",
         font=("Helvetica", 24, "bold")).pack(pady=5)

tk.Label(root, text="Italic Text - Purple",
         fg="purple",
         font=("Courier", 18, "italic")).pack(pady=5)

tk.Label(root, text="Bold Italic - Orange",
         fg="orange",
         font=("Verdana", 20, "bold italic")).pack(pady=5)

# Run program
root.mainloop()









# # Another
# import matplotlib.pyplot as plt

# plt.figure(figsize=(10, 8))

# plt.text(0.1, 0.9, "Default Font Text", fontsize=14)
# plt.text(0.1, 0.8, "Bold Text", fontsize=16, fontweight="bold")
# plt.text(0.1, 0.7, "Italic Text", fontsize=16, fontstyle="italic")
# plt.text(0.1, 0.6, "Large Red Text", fontsize=22, color="red")
# plt.text(0.1, 0.5, "Green Text", fontsize=18, color="green")
# plt.text(0.1, 0.4, "Blue Bold Text", fontsize=18, color="blue", fontweight="bold")

# plt.text(0.7, 0.5, "Vertical Text", fontsize=16, rotation=90, color="purple")

# plt.title("Creating Various Types of Texts and Fonts", fontsize=16, fontweight="bold")
# plt.xlim(0, 1)
# plt.ylim(0, 1)
# plt.axis("off")

# plt.show()