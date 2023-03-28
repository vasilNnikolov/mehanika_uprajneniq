import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def problem_1():
    data = pd.read_csv("data_1.csv")
    print(data.columns)
    concentration, angle = data["concentration"], data["angle"]
    plt.scatter(concentration, angle)
    a, b = np.polyfit(concentration, angle, deg=1)
    xs = np.linspace(start=0, stop=15, num=5)
    ys = a * xs + b
    print(a, b)
    plt.plot(xs, ys, color="red")

    plt.xlabel("Концентрация, %")
    plt.ylabel("Ъгъл, градуси")
    plt.show()


def problem_2():
    data = pd.read_csv("data_2.csv")
    print(data.columns)
    angle = data["angle_plus"] - data["angle_minus"]
    current = data["I"]
    plt.scatter(current, angle)
    a, b = np.polyfit(current, angle, deg=1)
    xs = np.linspace(start=6, stop=16, num=5)
    ys = a * xs + b
    print(a, b)
    plt.plot(xs, ys, color="red")

    plt.xlabel("Ток, А")
    plt.ylabel("Ъгъл, градуси")
    plt.show()


if __name__ == "__main__":
    problem_2()
