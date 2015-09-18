#!/usr/bin/python

from sys import stdin
from matplotlib import pyplot

frequencies = [int(n) for l in stdin for n in l.strip().split(' ')]

pyplot.plot(frequencies, 'ro')

ax = pyplot.subplot()
#ax.set_yscale('log')
ax.set_xscale('log')

pyplot.show()

