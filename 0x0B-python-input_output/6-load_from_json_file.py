#!/usr/bin/python3
"""
A function that creates an object from a "JSON file"
"""


def load_from_json_file(filename):
    """Create object from a JSON file"""

    import json
    with open(filename, "r") as f:
        x = json.load(f)
    return x
