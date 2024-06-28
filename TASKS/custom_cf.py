# custom_cf.py

# display the standard continued fraction for each of the 10 real numbers expressed by the formula given

import math

MAX_TERMS = 7


# normalize the continued fraction
def normalize_cf(cf):
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf


# encode the continued fraction of a given number x
def encode_cf(x):
    # define cf as a list of integers
    cf: list[int] = []
    while len(cf) < MAX_TERMS:
        # append floor(x) to the cf list
        cf.append(int(x))
        # set x to x - floor(x)
        x = x - int(x)
        # if x == 0 end the encoding
        if x < 1e-11:
            break
        # set x to 1/x and continue looping
        x = 1 / x
    return normalize_cf(cf)


# function for x
def fx(n) -> int:
    x = (1 + math.sqrt((4 * (n**2)) - (4 * n) + 5)) / 2
    return x  # type: ignore


# return the standard cf for each of the assigned real numbers
def main():
    # evaluate x at each integer 0-9 and calculate the cf for each value
    for i in range(0, 10):
        print(f"Number: {fx(i)}, Standard continued fraction: {encode_cf(fx(i))}")


main()
