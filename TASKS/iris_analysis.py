# iris_analysis.py
import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    # Read experiment data from data file
    file_name = "iris.csv"
    file_path = Path(__file__).parent / file_name
    data = np.genfromtxt(
        file_path, delimiter=",", dtype=None, encoding="utf-8", names=True
    )  # import data

    # plot
    plt.figure(Path(__file__).name)
    # iterate through the data and separate petal length and width based on the variety
    # "Setosa" length = 8, "Versicolor" length = 12, "Virginica" length = 11
    for i in range(0, len(data) - 1):
        if len(data[i][4]) == 8:
            plt.scatter(data[i][2], data[i][3], c="r")
        if len(data[i][4]) == 12:
            plt.scatter(data[i][2], data[i][3], c="g")
        if len(data[i][4]) == 11:
            plt.scatter(data[i][2], data[i][3], c="y")
    plt.xlabel("Petal Length (cm))")
    plt.ylabel("Petal Width (cm)")
    plt.grid("on")
    plt.title("Iris Analysis")
    # elements for legend
    l_elements = [
        plt.Line2D([0], [0], marker="o", color="r", label="Setosa"),
        plt.Line2D([0], [0], marker="o", color="g", label="Versicolor"),
        plt.Line2D([0], [0], marker="o", color="y", label="Virginica"),
    ]
    plt.legend(handles=l_elements)
    plt.show()


main()
