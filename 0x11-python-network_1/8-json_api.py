#!/usr/bin/python3
"""
Search API
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = requests.post(url)
    print(req.json)



    """search = req.text.find(argv[2])
    if search"""
