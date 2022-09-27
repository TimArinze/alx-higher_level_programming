#!/usr/bin/python3
"""
A function that appends a string at the end
of a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ APPEND TO A FILE """

    with open(filename, 'a', encoding="utf-8") as f:
        x = f.write(text)
    return x
