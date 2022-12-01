#!/usr/bin/python3
"""
Compare rectangles
"""


class Rectangle:
    """ Compare Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialiazation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @width.setter
    def height(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """str"""
        total = ""
        if self.__width == 0 or self.__height == 0:
            return total
        for i in range(self.__height):
            total += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                total += "\n"
        return total

    def __repr__(self):
        """representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """comparing instances"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """square"""
        return Rectangle(size, size)
