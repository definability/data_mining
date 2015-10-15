#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin
from os import linesep

words = ' '.join([l.strip() for l in stdin]).split(' ')

counts = {}
for key in set(words):
    counts[key] = 0
for w in words:
    counts[w] += 1

result = sorted(counts.iteritems(),key=lambda x: x[1],
                reverse=True)

print linesep.join('%s,%d'%r for r in result)

