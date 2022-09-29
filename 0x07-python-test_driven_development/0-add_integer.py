#!/usr/bin/python3
"""
A function that adds 2 integers
"""


def add_integer(a, b=98):
    """ Integers addition """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be integer")
    elif type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod("tests/0-add_integer.txt")
