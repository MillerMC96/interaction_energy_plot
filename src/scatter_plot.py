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

plt.plot(time, energy, linewidth=1)

#pull indicators

#first pull
plt.axvline(0)
plt.text(0.1, -100, 'first pull', rotation=90)

#second pull
plt.axvline(60)
plt.text(60.1, -100, 'second pull', rotation=90)

#third pull
plt.axvline(90)
plt.text(90.1, -100, 'third pull', rotation=90)

#fourth pull
plt.axvline(120)
plt.text(120.1, -100, 'fourth pull', rotation=90)

#fifth pull
plt.axvline(150)
plt.text(150.1, -100, 'fifth pull', rotation=90)

#sixth pull
plt.axvline(180)
plt.text(180.1, -100, 'sixth pull', rotation=90)

#seventh pull
plt.axvline(210)
plt.text(210.1, -100, 'seventh pull', rotation=90)

#eighth pull
plt.axvline(270)
plt.text(270.1, -200, 'eighth pull', rotation=90)

plt.ylabel("energy [kJ/mol]")
plt.xlabel("time [ps]")
plt.title(sys.argv[1])
plt.show()
