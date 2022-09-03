#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary:
        for i in a_dictionary:
            if i == key:
                del i
    return (a_dictionary)
