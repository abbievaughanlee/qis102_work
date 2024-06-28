# maxwell_boltzmann.py: 
# calculate and display the probability density function of the Maxwell-Boltzmann distribution
# display three PDFs using the different parameters 1, 2, and 5

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# PDF of maxwell boltzmann distribution
def pdf(x, a):
    # empty array to be later filled with y values
    to_return = []
    for i in x:  # maxwell-boltzmann pdf formula
        to_return.append(
            math.sqrt(2 / math.pi)
            * ((i**2) / (a**3) * math.exp(-(i**2) / (2 * (a**2))))
        )
    return to_return


# create graphs
def main():
    # x values
    x = np.arange(0, 20, 0.1)

    # different parameters
    a1 = 1
    a2 = 2
    a3 = 5

    plt.figure(Path(__file__).name)

    # plot three lines for each different parameter
    plt.plot(x, pdf(x, a1), c="r", label="a = 1")
    plt.plot(x, pdf(x, a2), c="b", label="a = 2")
    plt.plot(x, pdf(x, a3), c="g", label="a = 5")

    plt.title("PDF of the Maxwell-Boltzmann Distribution")
    plt.xlabel("x")
    plt.ylabel("PDF")
    plt.legend()  # show a legend for the different values of a
    plt.xlim(0, 10)  # ensure interval is set from 0 to 10 on the x-axis
    plt.show()


main()
