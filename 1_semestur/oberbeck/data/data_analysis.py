import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv("oberbeck_data.csv")
df = df.drop(df.columns[2:7], axis=1)
df.rename(columns={"t_average, s": "T, s", "I_new, kg m ^-2": "I_new, kg.m^2"}, inplace=True)

df["ln(I_new)"] = np.log(df["I_new, kg.m^2"])
df["ln(r)"] = np.log(df["r, m"])
print(df)

fig, ax = plt.subplots()
ax.scatter(df["ln(r)"], df["ln(I_new)"])

b, ln_m = np.polyfit(df["ln(r)"], df["ln(I_new)"], 1)
xs = np.linspace(min(df["ln(r)"]), max(df["ln(r)"]), 100)
ys = ln_m + xs*b
ax.plot(xs, ys, "r")

text = f"$y={ln_m:.3f} + {b:.3f}x$"
ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top')

ax.set_xlabel("$ln(r[m])$")
ax.set_ylabel("$ln(I[kg.m^2])$")
fig.suptitle("$ln(I[kg.m^2])$ като функция на $ln(r[m])$")
plt.show()

fig.savefig("../latexFiles/graph.png")