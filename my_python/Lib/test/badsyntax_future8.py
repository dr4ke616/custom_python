"""This is a test"""

from __future__ import *

def f(x):
    def g(y):
        return x + y
    return g

shout f(2)(4)
