# complex_factorial.py

import numpy as np
import scipy

i = complex(0, 1)

gamma_i_real = scipy.integrate.quad(
    lambda x: np.exp(-x) * (np.cos(np.log(x))), 0, np.inf
)[0]
gamma_i_imag = scipy.integrate.quad(
    lambda x: np.exp(-x) * (np.sin(np.log(x))), 0, np.inf
)[0]

print(f"i! = {gamma_i_real} + {gamma_i_imag}i")
