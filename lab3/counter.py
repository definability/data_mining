#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin
from os import linesep
from math import log

def get_count(words):
    tfs = {}
    for key in set(words):
        tfs[key] = 0
    for w in words:
        tfs[w] += 1
    return tfs

texts = ([l.strip().split(' ') for l in stdin])
names = map(lambda text: text[0], texts)
texts = map(lambda text: text[1:], texts)

tfs = map(get_count, texts)

idf = {}
for word in set(sum(texts, [])):
    idf[word] = 0

for tf in tfs:
    for word in tf:
        idf[word] += 1

logN = log(len(texts))
for word in idf:
    idf[word] = logN - log(idf[word])


tf_idfs = []
for i, tf in enumerate(tfs):
    tf_idfs.append({})
    for word in tf:
        tf_idfs[i][word] = float(tf[word] * idf[word]) / len(tf)

#result = sorted(counts.iteritems(),key=lambda x: x[1],
#                reverse=True)

print linesep.join('%s,%s,%f'%(names[i], word, tf_idf[word])
                    for i, tf_idf in enumerate(tf_idfs) for word in tf_idf)

