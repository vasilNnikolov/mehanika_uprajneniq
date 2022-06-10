import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from uncertainties import ufloat

def graph():

    preamble = """\\usepackage[T2A]{fontenc}
    \\usepackage[utf8]{inputenc}
    \\usepackage[bulgarian]{babel}
    \\usepackage[]{siunitx}"""
    LaTeX = {
        "text.usetex": True,
        "font.family": "serif",
        "text.latex.preamble": preamble
    }
    plt.rcParams.update(LaTeX)

    # очевидно това е размера на шрифта без значение какъв е той
    plt.rcParams["font.size"] = 20


    df: pd.DataFrame = pd.read_csv("data.csv")

    best_fit_line, cov_matrix = np.polyfit(df['t'], df['h'], deg=1, cov=True)

    print(best_fit_line)
    xs = np.linspace(df['t'].min(), df['t'].max(), 100)
    ys = best_fit_line[0]*xs + best_fit_line[1]
    sns.scatterplot(data=df, x='t', y='h')
    sns.lineplot(x=xs, y=ys)
    plt.xlabel("T, C")

    plt.ylabel("H, mm")
    a = ufloat(best_fit_line[0], cov_matrix[0, 0])
    print(a)
    plt.show()

def compute():
    a = ufloat(7.5, 1.5)/1000
    R = ufloat(1.5, 0.08)/1000
    V_0 = ufloat(65.3 - 25, 0.1)/(1000*789)
    lambda_0 = ufloat(10**(-10), 0)

    l = (np.pi*R**2*a + lambda_0)/V_0
    print(1000*l.nominal_value, 2*l.std_dev/l.nominal_value*100)

if __name__ == "__main__":
    compute()

