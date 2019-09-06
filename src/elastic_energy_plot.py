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

# noise level

plt.hlines(45, 0, time[-1])

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

# third pull
plt.axvline(90, alpha=transparency)
plt.text(90 + offset_from_indicator, bottom + text_spacing, 'third pull', rotation=90)

# fourth pull
plt.axvline(120, alpha=transparency)
plt.text(120 + offset_from_indicator, bottom + text_spacing, 'fourth pull', rotation=90)

# fifth pull
plt.axvline(150, alpha=transparency)
plt.text(150 + offset_from_indicator, bottom + text_spacing, 'fifth pull', rotation=90)

# sixth pull
plt.axvline(180, alpha=transparency)
plt.text(180 + offset_from_indicator, bottom + text_spacing, 'sixth pull', rotation=90)

# seventh pull
plt.axvline(210, alpha=transparency)
plt.text(210 + offset_from_indicator, bottom + text_spacing, 'seventh pull', rotation=90)

# eighth pull
plt.axvline(270, alpha=transparency)
plt.text(270 + offset_from_indicator, bottom + text_spacing, 'eighth pull', rotation=90)

plt.ylabel("elastic energy")
plt.xlabel("time [ps]")
plt.title("Elastic energy over time")
plt.show()
