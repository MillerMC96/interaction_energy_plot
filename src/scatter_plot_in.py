import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

index = 1
argc = len(sys.argv)
files = []

while index < argc:
    files.append(open(sys.argv[index], 'r'))
    index += 1

energies = list()
times = list()

for fp in files:
    
    # x and y axes
    time = list()
    energy = list()
    
    # reading input
    while fp:
        line = fp.readline()
        if line:
            x, y = line.split()
            time.append(float(x))
            energy.append(float(y))
        else:
            break
    times.append(time)
    energies.append(energy)

# plotting

i = 0
while i < argc - 1:
    plt.plot(times[i], energies[i], linewidth=1, label=sys.argv[i + 1])
    i += 1

plt.legend(loc='best')

# plot parameters

spacing = 100
top = np.amax(energies) + spacing
bottom = np.amin(energies) - spacing
plt.ylim([bottom, top])

# pull indicators

transparency = 0.7
text_spacing = 20
offset_from_indicator = 0.2

# first pull
plt.axvline(0, alpha=transparency) 
plt.text(0 + offset_from_indicator, bottom + text_spacing, 'first pull', rotation=90)

# second pull
plt.axvline(60, alpha=transparency)
plt.text(60 + offset_from_indicator, bottom + text_spacing, 'second pull', rotation=90)

plt.ylabel("energy [kJ/mol]")
plt.xlabel("time [ps]")
plt.title("Lennard-Jones Potentials over time")
plt.show()
