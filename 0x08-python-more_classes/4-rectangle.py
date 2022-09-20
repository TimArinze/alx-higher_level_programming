#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by 3-rectangle
"""


class Rectangle:
    """ Eval is magic """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ Return the perimeter of the rectangle."""
        total = ""
        if self.__width and self.__height == 0:
            return total
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i != self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """Get/set the width of the Rectangle"""
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
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width and self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
