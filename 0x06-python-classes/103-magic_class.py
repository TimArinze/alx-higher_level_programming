#!/usr/bin/python3
import math
"""
The python class MagicClass does same with the python bytecode
"""

class MagicClass:
    """Magic class"""

    def __init__(self, radius):
        """instantiation"""
        self.radius = radius

    @property
    def radius(self):
        """getter"""
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """setter"""
        if type(radius) is not int:
            raise TypeError("radius must be a number")
        elif type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """area"""
        return 2 * math.pi * (self.radius ** 2)

    def circumference(self):
        """circumference"""
        return 2 * math.pi * self.radius
