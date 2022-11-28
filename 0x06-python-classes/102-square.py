#!/usr/bin/python3
"""
Compare2Square
"""


class Square:
    """ A class that defines a square"""


    def __init__(self, size=0):
        """instantiation with optional"""
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        return self.size ** 2

    def __eq__(self, other):
        """for comparator"""
        return self.size == other.size

    def __lt__(self, other):
        """for comparator"""
        return self.size < other.size

    def __le__(self, other):
        """for comparator"""
        return self.size <= other.size

    def __ne__(self, other):
        """for comparator"""
        return self.size != other.size

    def __gt__(self, other):
        """for comparator"""
        return self.size > other.size

    def __ge__(self, other):
        """for comparator"""
        return self.size >= other.size

    def __str__(self):
        """string"""
        return str(self.size)
