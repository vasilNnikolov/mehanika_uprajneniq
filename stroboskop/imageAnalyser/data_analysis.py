from os import EX_DATAERR, name
import pandas as pd

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
# vx_col = pd.Series([(xs[i + 1] - xs[i - 1])/(2*dt) for i in range(1, df.count()[0] - 1)], index=list(range(1, df.count()[0] - 1)))
# vx_col.at[0] = vx_col.at[1]
# vx_col.at[vx_col.size] = vx_col.at[vx_col.size - 1]
# df["V_x, cm/s"] = vx_col 

# vy_col = pd.Series([(ys[i + 1] - ys[i - 1])/(2*dt) for i in range(1, df.count()[0] - 1)], index=list(range(1, df.count()[0] - 1)))
# vy_col.at[0] = vy_col.at[1]
# vy_col.at[vy_col.size] = vy_col.at[vy_col.size - 1]
# df["V_y, cm/s"] = vy_col 

# add x and y velocities simultaneously
velocities = pd.Series([((positions[i + 1][0] - positions[i - 1][0]), 
                        (positions[i + 1][1] - positions[i - 1][1])) for i in range(1, df.count()[0] - 1)], 
                        index=list(range(1, df.count()[0] - 1)))

velocities = pd.Series([(v[0]/(2*dt), v[1]/(2*dt)) for v in velocities])
df["v, cm/s"] = velocities


print(df.head())
print(df.tail())

