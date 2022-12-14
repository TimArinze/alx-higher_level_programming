#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
by: (based on 1-rectangle.py)
"""


class Rectangle:
    """ Area and Perimeter """

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
    Calculate area of Rectangle
    """
    def area(self):
        """Area of the rectangle"""
        return self.width * self.height

    """
    Calculate perimeter
    """
    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.width and self.height == 0:
            return 0

        return (self.width + self.height) * 2
