# solve4x4.py

import numpy as np

coeffs = np.array([[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]])
vals = np.array([5, 16, 22, 15])

sol = np.linalg.solve(coeffs, vals)

print(f"x0 = {sol[0]}")
print(f"x1 = {sol[1]}")
print(f"x2 = {sol[2]}")
print(f"x3 = {sol[3]}")
