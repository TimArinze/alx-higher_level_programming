#!/usr/bin/python3
""" Printing a square """


class Square:
    """ A class that defines a square by 4-square.py"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        value = '#'
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(value * self.__size)
