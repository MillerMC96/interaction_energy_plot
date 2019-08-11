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
N, bins, patches = plt.hist(energy, bins=n_bins, orientation="horizontal")

fracs = N / N.max()
norm = colors.Normalize(fracs.min(), fracs.max())
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)
plt.ylabel("energy [kJ/mol]")
plt.xlabel("frequency")
plt.title("energy distribution of " + sys.argv[1])
plt.show()
