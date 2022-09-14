#!/usr/bin/python3
"""Size validation"""


class Square:
    """A class Square defined"""
    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
