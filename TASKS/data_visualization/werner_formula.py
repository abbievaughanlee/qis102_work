# werner_formula.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3 * np.pi, 3 * np.pi, 6 * np.pi / 100)
f = np.sin(0.8 * x)
f2 = np.sin(0.5 * x)
f3 = f * f2
f4 = (np.cos(0.3 * x) - np.cos(1.3 * x)) / 2
plt.figure(Path(__file__).name)
plt.title("Werner Formula")
plt.plot(x, f, c="r", label=r"$sin(\frac{4}{5}x)$")
plt.plot(x, f2, c="b", label=r"$sin(\frac{1}{2}x)$")
plt.plot(x, f3, c="g", label=r"$f_1(x) * f_2(x)$")
plt.plot(
    x,
    f4,
    marker="o",
    c="0.8",
    ls="None",
    label=r"$\frac{cos(\frac{3}{10}x) - cos(\frac{13}{10}x)}{2}$",
)

plt.legend()


plt.show()
