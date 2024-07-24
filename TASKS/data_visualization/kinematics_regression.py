# kinematics_regression.py
# calculate and display the constant acceleration and initial velocity of a moving particle
# The times (s) and total distances traveled (m) by the particle are provided in kinematics_regression.csv
# Plot the values in the data file and draw an appropriate smooth curve through them
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def fit_quadratic(x, y):
    # Reshape vector x to become matrix x
    x = x[:, np.newaxis]
    transformer = PolynomialFeatures(degree=2, include_bias=False)
    transformer.fit(x)
    # The matrix x2 will have two columns:
    # 1) the original x values and 2) the x**2 values
    x2 = np.array(transformer.transform(x))
    model = LinearRegression().fit(x2, y)
    a = model.coef_[1]
    b = model.coef_[0]
    c = model.intercept_
    return a, b, c


def main():
    # Read experiment data from data file
    file_name = "kinematics_regression.csv"
    file_path = Path(__file__).parent / file_name
    data = np.genfromtxt(file_path, delimiter=",")
    # time in s, distance traveled (m)
    time, distance = data.T
    # remove the labels at the top of the data:
    t = time[1:]
    d = distance[1:]
    x = np.linspace(t[0], t[len(t) - 1], 1000)
    # calculate acceleration:

    dt = t[len(t) - 1] - t[0]  # change in time
    dv = ((d[len(d) - 1] - d[len(d) - 2]) / (t[len(t) - 1]) - t[len(t) - 2]) - (
        (d[1] - d[0]) / t[1] - t[0]
    )  # change in velocity
    a = dv / dt

    v0 = a - (1 / 2) * (a) * (
        dt
    )  # kinematics eqn for initial velocity given change in time and acceleration

    print(f"Acceleration = {a:.2f} m/s^2")
    print(f"Initial Velocity  = {v0:,.2f} m/s")

    # plot the data
    plt.figure(Path(__file__).name)
    plt.scatter(t, d)
    a, b, c = fit_quadratic(t, d)
    plt.plot(x, a * x**2 + b * x + c, label="Quadratic", c="r")

    plt.title(
        "Particle Trajectory\n"
        f"Acceleration = {a:.2f}m/s^2, "
        f"Initial Velocity  = {v0:,.2f}m/s"
    )
    plt.xlabel("Time (s)")
    plt.ylabel("Distance Traveled (m)")
    plt.grid("on")
    plt.show()


main()
