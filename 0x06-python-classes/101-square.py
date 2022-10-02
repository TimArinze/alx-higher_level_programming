#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """ Print Square instance """

    def __init__(self, size=0, position=(0, 0)):
        """instantiation"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter and setter"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter and setter"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Area"""
        self.area ** 2

    def __str__(self):
        """__str__"""
        total = ""
        if self.size == 0:
            return total
        for k in range(self.position[1]):
            total += "\n"
        for i in range(self.size):
            total += (" " * self.position[0] + "#" * self.size)
            if i != self.__size - 1:
                total += "\n"
        return total
