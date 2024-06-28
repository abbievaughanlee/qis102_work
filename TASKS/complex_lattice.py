# complex_lattice.py
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# complex function
def f(x, y):
    return [x**2 - y**2 - y + 1, 2 * x * y + x]


def main():
    real_z_abs = np.arange(-4, 4, 0.01)  # array of possible real values
    imag_z = np.arange(0, 2, 0.01)  # array of possible imaginary values

    z_range = []  # soon to be an array of all possible complex values to be inputted to the function
    for i in real_z_abs:
        for j in imag_z:
            z_range.append([i, j])

    z = []  # array to store the entire complex part of each output
    z_imag = []  # array to store the imaginary part of each output
    z_real = []  # array to store the real part of each output
    # create z range of only integer values
    real_int = np.arange(-4, 4, 1)
    imag_int = np.arange(0, 2, 1)
    z_range2 = []
    for i in real_int:
        for j in imag_int:
            z_range2.append([i, j])
    # iterate through the array of z inputs and append f(z) to the z output array
    for i in z_range:
        func = f(i[0], i[1])
        z.append(func)
        z_imag.append(func[1])
        z_real.append(func[0])

    # calculate which values fall within the desired range
    z_in_range = []
    # store real and imaginary parts separately for plotting ease
    zir_real = []
    zir_imag = []
    gaussian_integers = 0
    # iterate through the range and check for the desired values: update sum accordingly
    for i in z_range2:
        x = i[0]
        y = i[1]
        func = f(i[0], i[1])
        if func[0] <= 10 and func[1] <= 10:
            z_in_range.append(i)
            zir_real.append(x)
            zir_imag.append(y)
            gaussian_integers += 1
    print(
        f"There are {gaussian_integers} Gaussian Integers that satisfy the constraint: |Re(f(z))| <= 10 and |Im(f(z))| <= 10"
    )
    # plot results
    plt.figure(Path(__file__).name)

    plt.scatter(z_real, z_imag, c=z_real, cmap="copper")

    # plot the in range points:
    plt.scatter(
        zir_real, zir_imag, c="r", label="|Re(f(z))| <= 10 and |Im(f(z))| <= 10"
    )

    plt.gca().set_aspect("equal")  # aspect ratio equal
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.legend()
    plt.title(r"$f(z) = z^2 + iz + 1$")

    plt.show()


main()
