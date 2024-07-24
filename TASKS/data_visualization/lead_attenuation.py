# lead_attenuation.py
# compute and plot the estimated attenuation factor of a lead shield as a function of incident photon 
# energy (MeV). Display the file data as a scatter plot and use cubic spline interpolation to draw
# a smooth curve passing through those discrete points. Based on the interpolation function, calculate
# the attenuation coefficient for a photon with 4.65 MeV energy. Having that value, calculate the percent
# of photons passing through a lead shield that is 2cm thick.

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d


def main():
    file_name = "lead_attenuation.csv"  # calls text file
    file_path = Path(__file__).parent / file_name

    samples = np.genfromtxt(
        file_path, delimiter=","
    )  # generate from text file separated by a comma
    energy, attenuation = samples.T  # transpose data so that it is two rows

    min_energy, max_energy = (
        np.min(energy),
        np.max(energy),
    )  # find min and max values of energy and create linspace
    energy_est = np.linspace(min_energy, max_energy, 1000)

    # interp1d() returns an "interpolation object" which  can then act as a callable function that is vector aware
    attenuation_f = interp1d(energy, attenuation, kind="cubic")
    attenuation_est = attenuation_f(energy_est)

    # calculate the attenuation coefficient for a photon with 4.65 MeV energy:
    photon = np.interp(4.65, energy_est, attenuation_est)

    # calculate the percent of photons passing through a lead shield that is 2cm thick ( ratio of photons emerged vs photons hitting the shied - N0)
    percent_emit = np.exp((-1) * photon * 2)
    percent_format = round(100 * percent_emit, 2)
    # print results:
    print(f"Attenuation coefficient for 4.65 MeV: {photon}")
    print(
        f"percent of photons passing through a 2cm thick lead shield: {percent_format} %"
    )
    # plot the data
    plt.figure(Path(__file__).name)
    plt.scatter(
        energy, attenuation, zorder=3
    )  # zorder: want data points to be on top of everything
    # plot y on a semi log scale
    plt.semilogy(energy_est, attenuation_est)

    plt.xlabel("Photon's Energy (MeV) ")
    plt.ylabel("Lead Shield's Attenuation Factor")
    plt.title("LEAD ATTENUATION COEFFICIENT")

    plt.show()


main()
