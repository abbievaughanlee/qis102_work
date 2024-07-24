# benfords_law.py
# demonstrate the Law of Anomalous Numbers
# calculate the probability of each digit (1 to 9) appearing as the most (far left) significant digit in 100_000 random integers
# random integers in range (1, 1000000) inclusive, raised to the 100th power
# create a histogram


from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# create an array of 100_000 numbers randomly generated from 1 to 1_000_000, raised to 100th power
nums = []
for _ in range(1, 100_001):
    nums.append((np.random.randint(1, 1_000_001)) ** 100)


# calculate most significant digit of a number
def sig(n):
    n_string = str(n)
    first_char = n_string[0]
    return int(first_char)


# iterate through the array and check for each digit appearing as the most significant digit
probs = []
for i in range(1, 10):
    j = 0
    for n in nums:
        if sig(n) == i:
            j += 1
    p = j / 100_000
    # add the probability as a percentage to probs array
    probs.append(p * 100)


# plot data
plt.figure(Path(__file__).name)
# bar chart made out of two arrays
plt.bar(np.arange(1, 10), probs)
plt.title("BENFORD'S LAW")
plt.xlabel("DIGIT")
plt.ylabel("PROBABILITY (%)")
plt.show()
