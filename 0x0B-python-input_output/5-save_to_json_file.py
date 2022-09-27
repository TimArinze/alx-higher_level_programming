#!/usr/bin/python3
"""
A function that writes an Object to a text file,
using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Save Object to a file"""

    with open(filename, 'w', encoding='utf-8')
    import json
    json.dump(my_obj, filename)
