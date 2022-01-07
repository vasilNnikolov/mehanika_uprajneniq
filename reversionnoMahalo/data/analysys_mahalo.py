import pandas as pd
import matplotlib.pyplot as plt
import uncertainties
import math
from uncertainties.core import ufloat

def main():
    df = pd.read_csv("./mahaloData.csv")

    df.drop(df.columns[3:], axis=1, inplace=True)

    plt.plot(df["l, cm"], df["T1, s"])
    plt.plot(df["l, cm"], df["T2, s"])

    plt.plot(47.05, 1.3643, "ro")

    plt.xlabel("Дължина между тежестите, см")
    plt.ylabel("Период, с")

    plt.show()

def get_uncertainty():
    T = ufloat(1.3653, 0.001)
    l = ufloat(46.314, 0.002)
    l = l/100
    print(l)
    g = 4*(math.pi)**2*l/T**2
    print(g)

if __name__ == "__main__":
    get_uncertainty()

