#!/usr/bin/python3
"""
Error code #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code > 200:
        print("Error code: {:d}".format(r.status_code))
    else:
        print(r.text)
