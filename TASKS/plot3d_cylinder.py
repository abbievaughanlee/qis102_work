# plot3d_cylinder.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

radius, height = 10, 50

u = np.linspace(0, height, 30)  # Vertical location
v = np.linspace(0, 2 * np.pi, 30)  # Horizontal circular slice

u, v = np.meshgrid(u, v)  # create a grid of all coordinate points
# convert to cartesian coordinates for plotting
x = radius * np.cos(v)
y = radius * np.sin(v)
z = u

plt.figure(Path(__file__).name)
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z, color="red")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-height, height)
ax.set_ylim(-height, height)
ax.set_zlim(0, height)
plt.show()
