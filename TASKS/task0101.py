# task 01

import numpy as np


def f(x):
    s1 = (0.5) * np.sin(np.pi * (x + 1.5)) + 0.5
    s2 = np.sin(np.pi * (x + 1.5))
    if x == 0:
        return 0
    return s2 * (2 * x) / (x**2 - (s1 * ((x * (x - 1)) / 2)))


# check to make sure that sequence repeats
for i in range(1, 15):
    print((f(i)))

# calculate sum
sum = 0
for i in range(0, 1001):
    sum += f(i)

print(sum)
print(f(-2.7))
# sum =  6.79, f(2.7) = -0.9547
