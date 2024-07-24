# rlc_circuit.py
# plot the current over time flowing through an RLC circuit that maintains a constant DC voltage

from pathlib import Path

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def model(t, y, R, L, C):
    # let i2 represent the derivative of i
    i = y[0]  # = i(t)
    i2 = y[1]  # = d(i)/dt

    return [i2, (-i / (L * C)) - (R / L) * i2]


def main():
    # Set simulation constants
    R = 0.1
    L = 0.01
    C = 0.01

    # Set Initial Conditions
    i_0 = 1.0
    time_initial = 0
    time_final = 1

    # Solve eqn for I(t)
    sol = solve_ivp(
        model,
        (time_initial, time_final),
        [i_0, 0],
        max_step=0.001,
        args=(R, L, C),
    )

    # plot
    plt.figure(Path(__file__).name)
    plt.plot(sol.t, sol.y[0], color="blue", lw=2)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Current (Amps)")
    plt.title("LCR Circuit")
    plt.grid("True")
    plt.show()


main()
