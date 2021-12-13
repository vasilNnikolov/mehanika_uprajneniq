from os import EX_DATAERR, name
import pandas as pd
import numpy as np

df = pd.read_csv("curved_line.csv", names = ["x, px", "y, px"])

start, end = tuple(df.iloc[0]), tuple(df.iloc[1])

pixels_per_cm = (((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5)/10

df = df.iloc[2:, :].reset_index()

df["x, cm"] = [x/pixels_per_cm for x in df["x, px"]]
df["y, cm"] = [y/pixels_per_cm for y in df["y, px"]]

# get velocities
dt = 1/100 # frequency was 1000 hz

xs, ys = df["x, cm"].tolist(), df["y, cm"].tolist()
positions = [(x, y) for x, y in zip(xs, ys)] 
print(df.head())

# add x and y velocities simultaneously
velocities = [(np.array(positions[i + 1]) - np.array(positions[i - 1]))/(2*dt) for i in range(1, df.count()[0] - 1)]

velocities = pd.Series(velocities, index=list(range(1, df.count()[0] - 1)))
velocities.at[0] = velocities.at[1]
velocities.at[df.count()[0] - 1] = velocities.at[df.count()[0] - 2]

df["v, cm/s"] = velocities

accelerations = [(np.array(velocities.at[i + 1]) - np.array(velocities.at[i - 1]))/(2*dt) for i in range(1, df.count()[0] - 1)]

accelerations = pd.Series(accelerations, index=list(range(1, df.count()[0] - 1)))
accelerations.at[0] = accelerations.at[1]
accelerations.at[df.count()[0] - 1] = accelerations.at[df.count()[0] - 2]

df["a, cm/s^2"] = accelerations



