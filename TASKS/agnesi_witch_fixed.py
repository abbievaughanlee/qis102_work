# agnesi_witch.py
# express maria agnesi's witch function f(x) using the simplified equation where a = 1/2
# plot the actual function as well as different versions of the power series (each having a different number of terms)

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# power series of agnesi's function
def power(x, n):  # n: number of terms, x: array of x values
    to_return = np.zeros_like(x)  # creates an array of zeros with the same shape as x
    for i in range(
        n
    ):  # runs through the number of terms and adjusts each value accordingly
        to_return += ((-1) ** i) * (x ** (2 * i))  # power series formula
    return to_return


def main():
    # plot f(x)
    x = np.arange(-1.5, 1.5, 0.01)
    agnesi_simplified = 1 / (x**2 + 1)  # agnesi's simplified function

    # plot each version of the power series
    p2 = power(x, 2)
    p3 = power(x, 3)
    p4 = power(x, 4)
    p5 = power(x, 5)
    p6 = power(x, 6)
    p7 = power(x, 7)

    plt.figure(Path(__file__).name)

    plt.plot(x, agnesi_simplified, c="b", label="exact")

    plt.plot(x, p2, c="orange", label="2 terms")
    plt.plot(x, p3, c="g", label="3 terms")
    plt.plot(x, p4, c="r", label="4 terms")
    plt.plot(x, p5, c="purple", label="5 terms")
    plt.plot(x, p6, c="saddlebrown", label="6 terms")
    plt.plot(x, p7, c="pink", label="7 terms")
    plt.grid("True")

    plt.title("Runge's Phenomenon (Witch of Agnesi)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-1.7, 1.7)
    plt.legend()

    plt.show()


main()

# """ The formula for the power series of Agnesi's Witch is of the form:
# sum from n= 0 to n ((-x**2)**n)
# This is a problematic formula because as n tends towards infinity, the derivative of the power series
# does too. I.e the slope become virtually vertical and the graph diverges as we approach
# x = -1 or x = 1.
# This is a perfect demonstration of Runge's Phenomenon. According to Wikipedia, Runge's Phenomenon is "a
# problem of oscillation at the edges of an interval that occurs when using polynomial interpolation
# with polynomials of high degree over a set of equispaced interpolation points." Runge's Phenomenon results
# in the limit as n tends towards infinity of the supremum from [-1, 1] of the absolute value of the function
# minus its power series (of degree n) is infinity. This basically means that the maximum difference between
# the function and its power series within a given interval is infinity (i.e the power series diverges)...
# Which is exactly what is happening in the Agnesi Witch graph."
