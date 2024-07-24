# mc_exp_dist.py
# uses Monte Carlo estimation to calculate the probability an event will occur within one hour of an
# exponential distribution having a rate parameter of 90 minutes

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import float64, vectorize


# halton function
@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def main():
    dots = 50_000

    # range [0, 1] x [0, 2]
    x = (1 - halton(np.arange(dots), 2)) * 1
    y = (1 - halton(np.arange(dots), 3)) * 2

    d = y - 1.5 * np.exp(-1.5 * x)  # exponential distribution function to be integrated

    # calculate points that fall under the exponential distribution function
    x_in = x[d <= 0.0]
    y_in = y[d <= 0.0]
    x_out = x[d > 0.0]
    y_out = y[d > 0.0]

    act = 1 - np.exp(-1.5)
    # [0, 1] x [0, 2] = 2 (area)
    est = (
        np.count_nonzero(d <= 0.0) / dots * 2
    )  # estimation (ratio of dots under curve to all dots)
    err = np.abs((est - act) / act)  # percent error

    # display data
    print(f"dots = {dots:,}")
    print(f"act = {act:.6f}")
    print(f"est = {est:.6f}")
    print(f"err = {err:.5%}")

    # plot data
    plt.figure(Path(__file__).name)
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
    plt.title("Exponential Distribution with Rate Parameter = 1.5h")
    plt.xlabel("time (hours)")
    plt.ylabel("y")
    plt.show()


main()
