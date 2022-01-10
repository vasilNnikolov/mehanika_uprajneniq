import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def zadacha_1():
    df = pd.read_csv("amZad1.csv")
    print(df)
    # df.drop(columns=df.iloc[:, 0:5], axis=1, inplace=True)
    df.drop([10, 11], inplace=True)
    df["t^2, s^2"] = (df["t, s"].map(lambda x: float(x)))**2
    df["L, m"] = df["L, m"].map(lambda x: float(x))
    print(df)
    xs = df["t^2, s^2"]
    ys = 2*df["L, m"]
    plt.scatter(xs, ys)
    a, _ = curve_fit(lambda x, a: a*x, xs, ys)
    print(a[0])
    plt.plot(xs, a[0]*xs, "r")

    plt.xlabel("$t^2, s^2$", fontsize=15)
    plt.ylabel("$2L, m$", fontsize=15)
    plt.show()

def zadacha_2():
    df = pd.read_csv("amZad2.csv")
    M = 118.87/2000
    L, h = 0.2, 0.2
    df["g, ms^-2"] = (2*M+df["m, kg"])*L**2/(2*df["m, kg"]*h*df["t, s"]**2)
    print(df)
    xs = 1/df["m, kg"]
    ys = df["g, ms^-2"]
    plt.scatter(xs, ys)
    a, b = np.polyfit(xs, ys, deg=1)
    plt.plot(xs, a*xs+b, "r")
    print(b)
    plt.xlabel("$1/m, kg^{-1}$", fontsize=15)
    plt.ylabel("$g, ms^{-2}$", fontsize=15)
    plt.show()




if __name__ == "__main__":
    zadacha_2()