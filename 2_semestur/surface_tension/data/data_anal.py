import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from uncertainties import ufloat

data = pd.DataFrame(pd.read_csv("surface_tension.csv"))
print(type(data))

data = data.iloc[1:10, :7].astype(float)

print(data)
rho = ufloat(997, 0.1)
g = ufloat(9.81, 0.01)
R = ufloat(0.563, 0.001) * 1/2000 
col_lengths = data.notnull().sum()

print(data.dtypes)
average = {key: data[key].mean()/1000 for key in data.columns}
print(average)
errors = {key: (1 + (data[key].std())**2/col_lengths[key])**0.5  for key in data.columns}
coeffs = {key: rho*g*R*ufloat(average[key], errors[key])/2 for key in data.columns}

print(coeffs)
