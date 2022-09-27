#!/usr/bin/python3
"""
A function that appends a string at the end
of a text file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ APPEND TO A FILE """

    with open(filename, 'a') as f:
        x = f.append(text)
    return x
