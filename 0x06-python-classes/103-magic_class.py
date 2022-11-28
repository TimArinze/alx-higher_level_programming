#!/usr/bin/python3
import math
"""
The python class MagicClass does same with the python bytecode
"""

class MagicClass:
    """Magic class"""

    def __init__(self, radius=0):
        """instantiation"""
        self.radius = radius

    @property
    def radius(self):
        """getter"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """setter"""
        if type(value) is not int and type(value) is not float:
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """area"""
        return math.pi * (self.radius ** 2)

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self.radius
