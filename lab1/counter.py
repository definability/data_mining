#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin
from os import linesep

words = ' '.join([l.strip() for l in stdin]).split(' ')

print linesep.join(map(str, sorted(map(words.count, set(words)), reverse=True)))

