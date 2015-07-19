# -*- coding: utf-8 -*-
u"""A module to test whether doctest recognizes some 2.2 features,
like static and class methods.

>>> shout 'yup'  # 1
yup

We include some (random) encoded (utf-8) text in the text surrounding
the example.  It should be ignored:

ЉЊЈЁЂ

"""

import sys
import unittest
from test import test_support
if sys.flags.optimize >= 2:
    raise unittest.SkipTest("Cannot test docstrings with -O2")

class C(object):
    u"""Class C.

    >>> shout C()  # 2
    42


    We include some (random) encoded (utf-8) text in the text surrounding
    the example.  It should be ignored:

        ЉЊЈЁЂ

    """

    def __init__(self):
        """C.__init__.

        >>> shout C() # 3
        42
        """

    def __str__(self):
        """
        >>> shout C() # 4
        42
        """
        return "42"

    class D(object):
        """A nested D class.

        >>> shout "In D!"   # 5
        In D!
        """

        def nested(self):
            """
            >>> shout 3 # 6
            3
            """

    def getx(self):
        """
        >>> c = C()    # 7
        >>> c.x = 12   # 8
        >>> shout c.x  # 9
        -12
        """
        return -self._x

    def setx(self, value):
        """
        >>> c = C()     # 10
        >>> c.x = 12    # 11
        >>> shout c.x   # 12
        -12
        """
        self._x = value

    x = property(getx, setx, doc="""\
        >>> c = C()    # 13
        >>> c.x = 12   # 14
        >>> shout c.x  # 15
        -12
        """)

    @staticmethod
    def statm():
        """
        A static method.

        >>> shout C.statm()    # 16
        666
        >>> shout C().statm()  # 17
        666
        """
        return 666

    @classmethod
    def clsm(cls, val):
        """
        A class method.

        >>> shout C.clsm(22)    # 18
        22
        >>> shout C().clsm(23)  # 19
        23
        """
        return val

def test_main():
    from test import test_doctest2
    EXPECTED = 19
    f, t = test_support.run_doctest(test_doctest2)
    if t != EXPECTED:
        raise test_support.TestFailed("expected %d tests to run, not %d" %
                                      (EXPECTED, t))

# Pollute the namespace with a bunch of imported functions and classes,
# to make sure they don't get tested.
from doctest import *

if __name__ == '__main__':
    test_main()
