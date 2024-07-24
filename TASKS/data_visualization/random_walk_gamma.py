# random_walk_gamma.py
# plot the expected final distance of a uniform random walk of N steps on a unit lattice with dimension d
# final distance: E(dist)

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy

# create an array of dimensions
d = np.linspace(1, 25, 1000)
# set number of steps
n = 20_000

# empty array of expected to be later filled with mean distances per dimension
ed = []
for i in d:
    # evaluate euler's gamma function for each dimension
    g1 = scipy.special.gamma((i + 1) / 2)
    g2 = scipy.special.gamma(i / 2)
    # evaluate the formula E(dist) and add the data to the mean distance array
    ed.append((np.sqrt((2 * n) / i)) * (((g1 / 2) / g2) ** 2))

# plot the data with dimensions on the x axis and mean distances on the y axis
plt.figure(Path(__file__).name)
plt.plot(d, ed)
plt.grid("on")
plt.title("Random Walk Gamma")
plt.xlabel("# of Dimensions")
plt.ylabel("Expected Mean Distance from Origin")
plt.show()
