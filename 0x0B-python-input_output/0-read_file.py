#!/usr/bin/python3
"""
A function that reads a text file(UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """ READ FILE """

    with open(filename) as f:
        for line in f:
            print(line, end="")
