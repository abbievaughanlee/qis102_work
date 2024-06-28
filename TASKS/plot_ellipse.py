# plot_ellipse.py
# note: cartesian form: (x/a)^2 + (y/b)^2 = 1

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# calculate the points on the perimeter of the ellipse
# major (x) axis length
x_length = 100
# minor (y) axis length
y_length = 50
# create an interval from 0 to 2pi
t = np.linspace(0, 2 * np.pi, 1000)
# find the radius at each theta
r = (x_length * y_length) / np.sqrt(
    (x_length * np.sin(t)) ** 2 + (y_length * np.cos(t)) ** 2
)
# convert to cartesian coordinates
x = r * np.cos(t)
y = r * np.sin(t)

# plot the ellipse
plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.grid("on")
plt.gca().set_aspect("equal")
plt.xlabel("x")
plt.ylabel("y")
# ensure that the -50 and 50 lines are labeled
plt.yticks(np.arange(-60, 60, 10))
plt.title("Ellipse")
plt.show()
