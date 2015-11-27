#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin, argv
from os import linesep
from math import log
from stoplist import stop_list


def get_count(words):
    tfs = {}
    for key in set(words):
        tfs[key] = 0
    for w in words:
        tfs[w] += 1
    return tfs

def group_n_grams(words, n):
    if n < 2:
        return [w for w in words if w not in stop_list]
    return [' '.join(w for w in words[i:i+n]) for i in range(len(words)-n) if words[i] not in stop_list and words[i+n-1] not in stop_list]

if __name__ == '__main__':
    n_grams_length = 1

    if len(argv) > 1:
        n_grams_length = int(argv[1])

    texts = ([l.strip().split(' ') for l in stdin])
    names = map(lambda text: text[0], texts)
    texts = map(lambda text: group_n_grams(text[1:], n_grams_length), texts)


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
            tf_idfs[i][word] = tf[word] * idf[word] / len(tf)

    result = [(names[i], word, tf_idf[word]) for i, tf_idf in enumerate(tf_idfs) for word in tf_idf]
    result = sorted(result, key=lambda x: x[2], reverse=True)
    print linesep.join('%s,%s,%f'%(r) for r in result)

