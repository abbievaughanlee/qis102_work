# hamming_weight.py
# calculate and display the Hamming Weight of 95,601

import numpy as np


# calculate the Hamming Weight of a given number
def hamming_weight(n):
    # initialize sum and set it to zero: this will be the hamming weight later
    sum = 0
    # convert the number to a string then iterate over each of its characters
    binary_str = np.binary_repr(n)
    # count the number of ones in the binary string
    for j in binary_str:
        if j == "1":
            sum += 1

    print(sum)


# calculate the hamming weight of 95,601
hamming_weight(95601)
