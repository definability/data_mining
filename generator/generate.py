#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint
#from T3d import synthesis
from data4d import synthesis

def get_next(start):
    item = synthesis[start]
    limit = sum(f for w, f in item.items())
    r = randint(0, limit)
    for w, f in item.items():
        r -= f
        if r <= 0:
            return w

def generate_text(start, words):
    text = ' '.join(start)
    for i in range(words):
        start = start[1:]+(get_next(start),)
        text += ' ' + start[-1]
    return text


def display(text):
    print '. '.join(t.strip().decode('utf8').capitalize() for t in text.split('.'))

