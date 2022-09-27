#!/usr/bin/python3
"""
A function that writes a string to a text file(UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """ WRITE TO A FILE"""

    with open(filename, encoding="utf-8") as f:
        x = f.write(text)
        return x
