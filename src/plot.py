import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors
from matplotlib.ticker import PercentFormatter

fp = open('../txt/LJ-SR-bottleneck-bottleneck', 'r')
while fp:
    line = fp.readline()
    if line:
        x, y = line.split()
        print(x, y)
    else:
        break


