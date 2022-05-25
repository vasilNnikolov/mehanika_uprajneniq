import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from uncertainties import ufloat

data = pd.DataFrame(pd.read_csv("surface_tension.csv"))
print(type(data))

data = data.iloc[1:10, :7].astype(float)

rho = ufloat(997, 0.1)
g = ufloat(9.81, 0.01)
R = ufloat(0.563, 0.001) * 1/2000 
col_lengths = data.notnull().sum()

average = {key: data[key].mean()/1000 for key in data.columns}
print(average)
errors = {key: (1/1000**2 + (data[key].std()/1000)**2/col_lengths[key])**0.5  for key in data.columns}
coeffs = {key: rho*g*R*ufloat(average[key], errors[key])/2 for key in data.columns}

for col in data.columns:
    print(f"{col}: sf coeff is {coeffs[col].nominal_value} pm {coeffs[col].std_dev/coeffs[col].nominal_value*100:.2f}")
