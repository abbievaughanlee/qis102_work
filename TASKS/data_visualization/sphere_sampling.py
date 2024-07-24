# sphere_sampling.py
# surface area sampling

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Create random samples within the sphere
n = 15000
u = np.random.rand(n)
v = np.random.rand(n)

# theta and thi randomly generated from their cumulative density functions:
theta = 2 * np.pi * u
thi = np.arccos(2 * v - 1)

# Spherical to Cartesian coordinate conversion

x = np.sin(thi) * np.cos(theta)
y = np.sin(thi) * np.sin(theta)
z = np.cos(thi)


plt.figure(Path(__file__).name, figsize=(10, 8))
ax = plt.axes(projection="3d")
ax.view_init(azim=-72, elev=48)
ax.scatter(x, y, z, s=0.5)
ax.set_title("Uniform Sphere Surface Sampling")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_aspect("equal")
plt.tight_layout()
plt.show()
