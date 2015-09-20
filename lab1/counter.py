#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

words = sorted(' '.join([l.strip() for l in stdin]).split(' '))

counts = {}

for key in set(words):
    counts[key] = 0
for w in words:
    counts[w] += 1

print ' '.join(map(str, sorted(counts.values(), reverse=True)))

