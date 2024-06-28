# archimedes_spiral.py
# calculate and display the arc length of an archimedes spiral with r = 0 as it rotates from 0<=0<=8pi
# using pyplot, make a graph of the entire spiral

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy

# create array of r and theta values (r = theta)
r = np.arange(0, 8 * np.pi, 0.1)


# calculate integrand for arc_length
def integrand(r):
    return np.sqrt(1 + r**2)


# find arc length
def find_arc_length(a):
    return (scipy.integrate.quad(integrand, 0, a))[0]


def main():
    print(find_arc_length(8 * np.pi))

    # plot the spiral in polar coordinates

    plt.figure(Path(__file__).name)
    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.plot(r, r)
    ax.set_rmax(8 * np.pi)
    ax.grid(True)
    ax.set_title("Archimedes Spiral")

    plt.show()


main()
