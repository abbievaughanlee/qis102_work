# plot3d_complex_sine.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator


# function that computes the absolute value of the sin of a complex number
def f(c):
    return abs(np.sin(c))


def main():
    real = np.linspace(-2.5, 2.5, 100)  # range of real parts of the complex numbers
    imag = np.linspace(-1, 1, 100)  # range of imaginary parts
    real, imag = np.meshgrid(
        real, imag
    )  # grid of real and imaginary points (plotting is to be done in complex plane)

    c = np.vectorize(complex)(
        real, imag
    )  # array of complex numbers to be plotted by using the real and imaginary parts
    z = f(c)

    plt.figure(Path(__file__).name)
    ax = plt.axes(projection="3d")

    surf = ax.plot_surface(real, imag, z, cmap="coolwarm", lw=0, antialiased=False)
    plt.colorbar(surf, ax=ax, shrink=0.5)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter("{x:.02f}")
    ax.set_xlabel("real")
    ax.set_ylabel("imaginary")
    ax.set_zlabel("z")
    plt.show()


main()
