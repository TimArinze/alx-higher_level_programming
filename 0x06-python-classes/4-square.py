#!/usr/bin/python3
""" Access and update """


class Square:
    """ A class Square that defines a square based on previous Square"""

    def __init__(self, size=0):
        self.size(value)
    def size(self):
        return self.__size
    def size(self, value):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        return self.__size ** 2
