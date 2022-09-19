#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle
"""


class Rectangle:
    """String representation"""

    def __init__(self, width=0, height=0):
        """initializing a new Rectangle
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set for the width"""

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
        """Get/set for the height"""

        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""

        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""

        if self.__width and self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """str"""

        total = ""
        if self.__width and self.__height == 0:
            return total
        for i in range(self.__height):
            total += "#" * self.__width
            if i != self.__height - 1:
                total += "\n"
        return total
