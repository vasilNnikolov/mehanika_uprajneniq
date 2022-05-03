import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stationary_filepath = "./statzionarno.csv"
stationary = pd.read_csv(stationary_filepath)

stationary = stationary[stationary.columns[:3]]

# graph showing stationary state has been reached
plt.figure(figsize=(16, 6))
sns.scatterplot(data=stationary, x='t, min', y='T_heat, C', color='red')
sns.scatterplot(data=stationary, x='t, min', y='T_ohlad, C', color='blue')
plt.show()
