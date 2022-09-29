#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Rectangle"""

    def __init__(self, width, height, name, value):
        Base.__init__(self)
        self.__width = width
        self.__height = height
        integer_validator(width
