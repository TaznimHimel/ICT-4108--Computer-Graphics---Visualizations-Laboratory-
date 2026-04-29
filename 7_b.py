import numpy as np
import matplotlib.pyplot as plt
from math import comb


# 🔹 Input degree
n = int(input("Enter number of control points: ")) - 1

t = np.linspace(0, 1, 100)

plt.figure(figsize=(6, 6))

# 🔹 Plot each Bernstein polynomial
for i in range(n + 1):
    B = comb(n, i) * (t**i) * ((1 - t)**(n - i))
    plt.plot(t, B, label=f"B{i},{n}(t)")

plt.title("Bezier Blending Functions (Bernstein Polynomials)")
plt.xlabel("t")
plt.ylabel("B(t)")
plt.legend()
plt.grid(True)
plt.show()