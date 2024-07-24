# hydrogen_spectrum.py

# calculate and display the wavelengths for the Pfund and Humphreys high energy spectral series of Hydrogen
# use both the Rydberg and Bohr formulas


# constants:
e_charge = 1.602e-19
e_mass = 9.109e-31
permittivity = 8.854e-12
h_plank = 6.626e-34
speed_light = 2.998e8
rydberg_constant = 1.0967757e7
e_0 = pow(e_charge, 4) * e_mass / (8 * pow(permittivity, 2) * pow(h_plank, 2))


# bohr function: (initial, final) = range of initial states, n = final state (dependent on the series)
def bohr(n, initial, final):
    final_orbit = n
    for init_orbit in range(initial, final + 1):
        # Initial energy level
        e_i = -e_0 / pow(init_orbit, 2)
        # Final energy level
        e_f = -e_0 / pow(final_orbit, 2)
        # Formula for waveLength in nanometers
        wave_length = h_plank * speed_light / (e_i - e_f) * 1e9
        print(f"\t{init_orbit:>2} -> {final_orbit:>2}{wave_length:8.0f} nm")


# rydberg function using rydberg's formula: (initial, final) = range of initial states, n = final state (dependent on the series)
def rydberg(n, initial, final):
    k = n
    # iterate through the initial states and calculate the wavelength at each value
    for j in range(initial, final + 1):
        wave_length = 1 / (rydberg_constant * (1 / pow(k, 2) - 1 / pow(j, 2))) * 1e9
        print(f"\t{j:>2} -> {k:>2}{wave_length:8.0f} nm")


# call all calculations and ensure that they are the same for each series
# pfund: higher energy states (6, 7, 8, 9, 10) to n = 5
# humphreys: higher energy states (7, 8, 9, 10, 11) to n = 6 energy states
def main():
    print(f"Pfund as calculated by Bohr: {bohr(5, 6, 10)}")
    print(f"Pfund as calculated by Rydberg: {rydberg(5, 6, 10)}")
    print(f"Humphreys as calculated by Bohr: {bohr(6, 7, 11)}")
    print(f"Humphreys as calculated by Rydberg: {rydberg(6, 7, 11)}")


main()
