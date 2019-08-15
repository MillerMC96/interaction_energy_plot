import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

fp = open(sys.argv[1], 'r')

# x and y axes
time = []
energy = []

# reading input
while fp:
    line = fp.readline()
    if line:
        x, y = line.split()
        time.append(float(x))
        energy.append(float(y))
    else:
        break

#plot parameters

spacing = 100
top = max(energy) + spacing
bottom = min(energy) - spacing

plt.plot(time, energy, linewidth=1)

plt.ylim([bottom, top])

#pull indicators

transparency = 0.7
text_spacing = 20
offset_from_indicator = 0.2

#first pull
plt.axvline(0, alpha=transparency) 
plt.text(0 + offset_from_indicator, bottom + text_spacing, 'first pull', rotation=90)

#second pull
plt.axvline(60, alpha=transparency)
plt.text(60 + offset_from_indicator, bottom + text_spacing, 'second pull', rotation=90)

#third pull
plt.axvline(90, alpha=transparency)
plt.text(90 + offset_from_indicator, bottom + text_spacing, 'third pull', rotation=90)

#fourth pull
plt.axvline(120, alpha=transparency)
plt.text(120 + offset_from_indicator, bottom + text_spacing, 'fourth pull', rotation=90)

#fifth pull
plt.axvline(150, alpha=transparency)
plt.text(150 + offset_from_indicator, bottom + text_spacing, 'fifth pull', rotation=90)

#sixth pull
plt.axvline(180, alpha=transparency)
plt.text(180 + offset_from_indicator, bottom + text_spacing, 'sixth pull', rotation=90)

#seventh pull
plt.axvline(210, alpha=transparency)
plt.text(210 + offset_from_indicator, bottom + text_spacing, 'seventh pull', rotation=90)

#eighth pull
plt.axvline(270, alpha=transparency)
plt.text(270 + offset_from_indicator, bottom + text_spacing, 'eighth pull', rotation=90)

plt.ylabel("energy [kJ/mol]")
plt.xlabel("time [ps]")
plt.title(sys.argv[1])
plt.show()
