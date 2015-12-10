#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin, argv
from os import linesep
from math import log


def get_count(words):
    tfs = {}
    for key in set(words):
        tfs[key] = 0
    for w in words:
        tfs[w] += 1
    return tfs

def group_n_grams(words, n):
    if n < 2:
        return words
    return [' '.join(w for w in words[i:i+n]) for i in range(len(words)-n)]

if __name__ == '__main__':
    n_grams_length = 1
    min_freq = 0

    if len(argv) > 1:
        n_grams_length = int(argv[1])
    if len(argv) > 2:
        min_freq = float(argv[2])

    texts = ([l.strip().split(' ') for l in stdin])
    names = map(lambda text: text[0], texts)
    texts = map(lambda text: set(group_n_grams(text[1:], n_grams_length)), texts)

    texts_set = set()
    for text in texts:
        texts_set = texts_set.union(text)

    min_freq *= len(texts)

    idf = {}
    for word in texts_set:
        idf[word] = 0


    for text in texts:
        for word in text:
            idf[word] += 1

    result = [(word, float(idf[word])/len(texts)) for word in texts_set if idf[word] >= min_freq]
    result = sorted(result, key=lambda x: x[1], reverse=True)
    print '# -*- coding: utf-8 -*-'
    print 'stop_list={',
    print (','+linesep).join('"%s":%f'%r for r in result),
    print '}'
    print ''

