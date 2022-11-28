#!/usr/bin/python3

"""
The python class MagicClass does same with the python bytecode
"""

import math


class MagicClass:
    """Magic class"""

    def __init__(self, radius=0):
        """instantiation"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """area"""
        return math.pi * (self.__radius ** 2)

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self.__radius
