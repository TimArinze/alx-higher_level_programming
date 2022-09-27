#!/usr/bin/python3
"""
A function that returns an object(Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """From JSON string to Object"""

    import json
    return json.load(my_str)
