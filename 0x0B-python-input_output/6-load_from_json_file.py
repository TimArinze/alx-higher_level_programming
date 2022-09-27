#!/usr/bin/python3
"""
A function that creates an object from a "JSON file"
"""


def load_from_json_file(filename):
    """Create object from a JSON file"""

    import json
    from io import StringIO
    with open(filename, "r") as f:
        json.load(StringIO(f))
