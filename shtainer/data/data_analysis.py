import matplotlib.pyplot as plt
import numpy as np

Ts = [1.805, 2.72, 3.3, 4.256, 4.808]
Ls = [0, 2.45, 3.417, 5.07, 5.87]

t_squared = [t**2 for t in Ts]
l_squared = [l**2 for l in Ls]
plt.scatter(l_squared, t_squared)

a, b = np.polyfit(l_squared, t_squared, 1) # y= ax + b
xs = np.linspace(min(l_squared), max(l_squared), num=100)
plt.plot(xs, a*xs + b, "r")

plt.xlabel("$L^2, cm^2$", fontsize=13)
plt.ylabel("$T^2, s^2$", fontsize=13)
plt.show()