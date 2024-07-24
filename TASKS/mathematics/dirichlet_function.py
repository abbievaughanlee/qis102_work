# dirichlet_function.py
# use mpmath package for Python to calculate and display the values: f(2), f(2.5), f(e)
# lim{lim[cos(k! * pix)**2n]} to infinity
# note: dirichlet function f: [0, 1] is defined by:
    # f(x) = 1 if x is rational and f(x) = 0 if x is irrational

import mpmath


def dirichlet_function(x):
    k, n = 100.0, 1e10
    val = mpmath.cos(mpmath.factorial(k) * mpmath.pi * x)
    val = mpmath.power(val, 2 * n)
    val = mpmath.chop(val) # chops off small real or imaginary parts, or converts numbers back to zero
    return val


def main():
    mpmath.mp.dps = 2000  # dps = decimal places
    print(f"f(2) = {dirichlet_function(2)}")
    print(f"f(2.5) = {dirichlet_function(2.5)}")
    print(f"f(sqrt(2)) = {dirichlet_function(mpmath.sqrt(2))}")
    print(f"f(e) = {dirichlet_function(mpmath.e)}")


main()
