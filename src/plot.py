import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

fp = open('../txt/LJ-SR-bottleneck-bottleneck', 'r')

time = []
energy = []

n_bins = 50

while fp:
    line = fp.readline()
    if line:
        x, y = line.split()
        time.append(float(x))
        energy.append(float(y))
    else:
        break
plt.hist(energy, bins=n_bins, orientation="horizontal")
plt.ylabel("energy [kJ/mol]")
plt.xlabel("frequency")
plt.title("energy distribution for bottleneck")
plt.show()
