# euler's constant.py
# use scipy to numerically estimate euler's constant
# then use pyplot to superimpose a line graph of y + ln(x) on top of a step plot  of the first 50 harmonic numbers

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy


# integrand function
def integrand(x):
    return np.log(np.log(1 / x))


# evaluate Euler's constant
Euler = (-1) * scipy.integrate.quad(integrand, 0, 1)[0]


# function to graph
def f(x):
    return Euler + np.log(x)


# harmonic numbers
harmonic = []
x = []
sum = 0
for i in range(1, 50):
    sum += 1 / i
    harmonic.append(sum)
    x.append(i)  # ensure that x and harmonic have the same dimension for plotting

print(Euler)

# plot line graph and harmonic numbers:

plt.figure(Path(__file__).name)
plt.plot(x, f(x), c="r", label="gamma + ln(x)")
plt.step(x, harmonic, c="b", label="Harmonic Numbers")
plt.legend()
plt.title("Euler's Constant")
plt.show()
