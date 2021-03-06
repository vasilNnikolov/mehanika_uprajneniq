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
    from scipy import optimize
    from uncertainties import ufloat
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
    sns.lineplot(ax=ax, x=xs, y=ys, color='red')

    # calculate derivative at T_2 = 40.4 C

    T_2 = 40.4
    def poly(t):
        return sum([coeffs[i]*t**(N - i) for i in range(N + 1)]) - T_2

    sol = optimize.root(poly, 150)
    x = sol.x[0]

    print(f"x = {x}")
    ax.axhline(T_2, color='green', linewidth=1)
    
    derivative = sum([i*coeffs[N - i]*x**(i - 1) for i in range(1, N + 1)])
    
    print(f"the derivative at T_2 is dT/dt = {derivative}")
    
    ys_tangent = T_2 + derivative*(xs - x) 
    sns.lineplot(ax=ax, x=xs, y=ys_tangent, color='green', linewidth=1)

    ax.set_xlabel("t, s")
    ax.set_ylabel("T, C")

    ax.set_title("Температура на охладителя")
    
    plt.show()
    save = input("enter sth to save")
    if len(save) > 0:
        ax.get_figure().savefig("graph_statz.png")

    # get final result
    dTdt = ufloat(-derivative, -0.01*derivative)
    m = ufloat(865, 2.5)/1000
    c = 389
    R = ufloat(129.9, 0.1)/2000
    h = ufloat(7.6, 0.1)/2000

    T_2 = ufloat(40.4, 0.1)
    T_1 = ufloat(55, 0.1)

    k = dTdt*m*c*h*(R**2 + 2*np.pi*R*h)/((T_1 - T_2)*(2*R**2 + 2*np.pi*R*h)*np.pi*R**2)
    
    print(f"k is {k.nominal_value} pm {100*k.std_dev/k.nominal_value:.2f}%")


ohlajdane()
