import pandas as pd
import numpy as np
from uncertainties import ufloat

df: pd.DataFrame = pd.read_csv("data.csv")

print(df.columns)

delta_manometer = 0.2

h_1 = ufloat(df["H1"].mean(), (delta_manometer**2 + 1/2*(3.1824*df["H1"].std())**2)**0.5)
h_2 = ufloat(df["H2"].mean(), (delta_manometer**2 + 1/2*(3.1824*df["H2"].std())**2)**0.5)

gamma = h_1/(h_1 - h_2) 

print(gamma)

