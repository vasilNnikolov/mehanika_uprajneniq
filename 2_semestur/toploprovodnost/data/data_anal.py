import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def stationary_condition():
    stationary_filepath = "./statzionarno.csv"
    stationary = pd.read_csv(stationary_filepath)

    stationary = stationary[stationary.columns[:3]]

    # graph showing stationary state has been reached
    # plt.figure(figsize=(16, 6))
    ax = sns.scatterplot(data=stationary, x='t, min', y='T_heat, C', color='red')
    sns.scatterplot(ax=ax, data=stationary, x='t, min', y='T_ohlad, C', color='blue')
    ax.axhline(55, color='red')
    ax.axhline(40.4, color='blue')

    ax.set_xlabel("t, min")
    ax.set_ylabel("T, C")

    ax.set_title("Достигане на стационарно състояние")

    ax.get_figure().savefig("graph_statz.png")
    plt.show()


def ohlajdane():
    ohlad_filepath = "./ohlajdane.csv"
    ohlajdane = pd.read_csv(ohlad_filepath)

    ohlajdane = ohlajdane[ohlajdane.columns[:3]]
    
    ax = sns.scatterplot(data=ohlajdane, x='t, s', y='T_ohlad, C')

    # fit poly
    N = 5
    coeffs = np.polyfit(ohlajdane['t, s'], ohlajdane['T_ohlad, C'], deg=N)

    xs = np.linspace(start=ohlajdane['t, s'].min(), stop=ohlajdane['t, s'].max(), num=100)
    ys = sum([coeffs[i]*xs**(N - i) for i in range(N + 1)]) 

    # plot poly
    sns.lineplot(x=xs, y=ys, color='red')

    ax.set_xlabel("t, s")
    ax.set_ylabel("T, C")

    ax.set_title("Температура на охладителя")
    
    plt.show()
    save = input("enter sth to save")
    if len(save) > 0:
        ax.get_figure().savefig("graph_statz.png")


ohlajdane()
