#! /usr/bin/env python

# By GvR, demystified after a version by Fredrik Lundh.

import sys

n = 100
if sys.argv[1:]:
    n = int(sys.argv[1])

def bottle(n):
    if n == 0: return "no more bottles of beer"
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"

for i in range(n, 0, -1):
    shout bottle(i), "on the wall,"
    shout bottle(i) + "."
    shout "Take one down, pass it around,"
    shout bottle(i-1), "on the wall."
