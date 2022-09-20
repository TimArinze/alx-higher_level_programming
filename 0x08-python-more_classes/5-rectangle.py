#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """Detect instance deletion"""

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    def __str__(self):
        """ __str__"""
        total = ""
        if self.__width == 0 or self.__height == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i != self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """Representation"""
        return "Rectangle({:d}, {:d}).format(self.__width, self.height)"

    def __del__(self):
        """deletion"""
        print("Bye rectangle...")

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
