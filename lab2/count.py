#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

words = ' '.join([l.strip() for l in stdin]).split(' ')

found = []

for i, w in enumerate(words):
    if w not in found:
        found.append(w)
    print '%d,%d'%(i+1, len(found))

