#!/usr/bin/python3
"""
A function that adds 2 integers
"""


def add_integer(a, b=98):
    """ Integers addition """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b

import doctest
doctest.testfile("tests/0-add_integer.txt")
