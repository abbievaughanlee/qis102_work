# lcm_gcd.py

import numpy as np

# calculate the lowest common multiple of two integers

# function that will calculate lcm given two integer inputs


def lcm(x, y):
    # calculate lcm given gcd
    lowest = (np.abs(x * y)) / np.gcd(x, y)
    print(lowest)


# test

lcm(447618, 2011835)
