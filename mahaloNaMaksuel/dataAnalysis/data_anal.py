import pandas as pd



df_0 = pd.read_csv("maksuelData.csv")
df = df_0.iloc[:10]

constants = df_0.iloc[13:19]
print(constants)
print(df)