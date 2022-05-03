import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
