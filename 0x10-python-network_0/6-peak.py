#!/usr/bin/python3
"""
A peak module
"""


def find_peak(list_of_integers):
    """Function that finds a peak in a list"""
    # sort the list
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
