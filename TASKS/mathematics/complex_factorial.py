# complex_factorial.py
# calculate the factorial of i

import numpy as np
import scipy

i = complex(0, 1)

# integrate the real part of the gamma function
gamma_i_real = scipy.integrate.quad(
    lambda x: np.exp(-x) * (np.cos(np.log(x))), 0, np.inf
)[0]
# integrate the imaginary part of the gamma function
gamma_i_imag = scipy.integrate.quad(
    lambda x: np.exp(-x) * (np.sin(np.log(x))), 0, np.inf
)[0]
 # return the real and imaginary parts as a complex number
print(f"i! = {gamma_i_real} + {gamma_i_imag}i")
