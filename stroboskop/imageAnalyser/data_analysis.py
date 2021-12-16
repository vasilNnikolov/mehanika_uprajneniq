from PIL import Image
from matplotlib.figure import Figure
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from sklearn import linear_model
from sklearn.linear_model import LinearRegression

from main import resize_image

def create_data_frame(filename):
    df = pd.read_csv(filename, names = ["x, px", "y, px"])

    start, end = tuple(df.iloc[0]), tuple(df.iloc[1])

    pixels_per_cm = (((start[0] - end[0])**2 + (start[1] - end[1])**2)**0.5)/10

    df = df.iloc[2:, :].reset_index()

    df["x, cm"] = [x/pixels_per_cm for x in df["x, px"]]
    df["y, cm"] = [y/pixels_per_cm for y in df["y, px"]]


    # get velocities
    dt = 1/100 # frequency was 1000 hz

    df["time, s"] = [i*dt for i in range(df.count()[0])]

    xs, ys = df["x, cm"].tolist(), df["y, cm"].tolist()
    positions = [(x, y) for x, y in zip(xs, ys)] 

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

    return df


def add_velocity_to_image():
    df_curved = create_data_frame("curved_line.csv") 
    data_frames = [df_curved]

    image, new_size = resize_image(Image.open("strob_image_2.jpg"), 2000)
    image_as_array = np.array(image)
    velocity_scaling_constant = 0.2
    acceleration_scaling_constant = 0.025

    for df in data_frames:
        xs, ys = df["x, px"], df["y, px"]
        vs = df["v, cm/s"]
        accelerations = df["a, cm/s^2"]

        for (p, v, a) in zip(zip(xs, ys), vs, accelerations):
            arrow_start = tuple(map(int, np.array(p)*2000/800))

            velocity_end = tuple(map(int, arrow_start + velocity_scaling_constant*v))
            acceleration_end = tuple(map(int, arrow_start + acceleration_scaling_constant*a))

            image_as_array = cv2.arrowedLine(image_as_array, arrow_start, velocity_end, (255, 0, 0), 2)
            image_as_array = cv2.arrowedLine(image_as_array, arrow_start, acceleration_end, (0, 255, 0), 2)
            
            # point_radius = 2 
            # image_as_array = cv2.circle(image_as_array, arrow_start, point_radius, (0, 0, 0), point_radius)

    image = Image.fromarray(image_as_array)
    image.show()
    image.save("curved_line_velocity_acceleration.jpg")

def make_velocity_acceleration_plots():
    df_line_1 = create_data_frame("straight_line_104g.csv") 
    df_line_2 = create_data_frame("straight_line_154g.csv") 
    data_frames = [df_line_1, df_line_2]
    colors = ["red", "green"]

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

    fig.text(0.5, 0.04, "Time, s", ha="center", va="center")
    fig.text(0.04, 0.5, "Velocity, cm/s", ha="center", va="center", rotation="vertical")
 
    ax1.set_title("Velocity for 104 g") 
    ax2.set_title("Velocity for 154 g") 

    fig.tight_layout(pad=3)
    for df, axis in zip(data_frames, (ax1, ax2)):
        xs, ys = df["x, px"], df["y, px"]
        vs = df["v, cm/s"]
        velocity_magnitudes = [np.sqrt(v.dot(v)) for v in vs]
        accelerations = df["a, cm/s^2"]
        acceleration_magnitudes = [np.sqrt(a.dot(a)) for a in accelerations]
        t = df["time, s"]

        lin_regressor = LinearRegression()
        reshaped_t = np.array(t).reshape(-1, 1)
        reshaped_vs = np.array(velocity_magnitudes).reshape(-1, 1)
        print(reshaped_vs.shape, reshaped_t.shape)
        print(reshaped_t)
        lin_regressor.fit(reshaped_t, reshaped_vs)
        y_predicted = lin_regressor.predict(t)
        axis.plot(t, velocity_magnitudes)
        axis.plot(t, y_predicted, color="red")


    plt.show()


if __name__ == "__main__":
    make_velocity_acceleration_plots()