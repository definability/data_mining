#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin, argv
from os import linesep


def get_count(words):
    tfs = {}
    for key in set(words):
        tfs[key] = 0
    for w in words:
        tfs[w] += 1
    return tfs

def group_n_grams(words, n):
    if n < 2:
        return [(w,) for w in words]
    return [tuple(words[i:i+n]) for i in range(len(words)-n)]

if __name__ == '__main__':
    n_grams_length = 1

    if len(argv) > 1:
        n_grams_length = int(argv[1])

    text_words = ' '.join(sum([l.split(' ') for l in stdin], [])).strip().split(' ')
    words = list(set(text_words))
    print 'words =', words
    words_d = dict(zip(words, range(len(words))))
    texts = group_n_grams([words_d[word] for word in text_words], n_grams_length)

    tfs = get_count(texts)

    result = [(word, tfs[word]) for word in tfs]
    result = sorted(result, key=lambda x: x[1], reverse=True)
    #print 'words =', result.keys()
    #print ''
    synthesis = {}
    for r in result:
        start = tuple(r[0][:-1])
        tail = r[0][-1]
        if start not in synthesis:
            synthesis[start] = {}
        synthesis[start][tail] = r[1]
    print 'synthesis =', synthesis.items()
    #print 'synthesis = {'
    #print linesep.join("    %s: %s,"%(r, synthesis[r]) for r in synthesis)
    #print '}'
    print ''

