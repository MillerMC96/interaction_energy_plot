import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

fp = open(sys.argv[1], 'r')

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
plt.plot(energy)
plt.ylabel("energy [kJ/mol]")
plt.xlabel("frame")
plt.title(sys.argv[1])
plt.show()
