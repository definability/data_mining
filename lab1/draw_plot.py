#!/usr/bin/python

from sys import stdin
from os import linesep
from matplotlib import pyplot

import numpy
from scipy import optimize

frequencies = [int(n) for l in stdin for n in l.strip().split(' ')]

print linesep.join('%d'%f for f in frequencies)

pyplot.plot(frequencies, 'ro')

ax = pyplot.subplot()
#ax.set_yscale('log')
ax.set_xscale('log')

pyplot.show()

