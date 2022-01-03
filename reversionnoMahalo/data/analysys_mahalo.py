import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./mahaloData.csv")

df.drop(df.columns[3:], axis=1, inplace=True)

plt.plot(df["l, cm"], df["T1, s"])
plt.plot(df["l, cm"], df["T2, s"])

plt.plot(47.05, 1.3643, "ro")

plt.xlabel("Дължина между тежестите, см")
plt.ylabel("Период, с")

plt.show()

