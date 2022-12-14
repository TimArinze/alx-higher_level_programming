#!/usr/bin/python3
"""
A function that returns True if the object is an instance
of a class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """ Only sub class of"""

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
