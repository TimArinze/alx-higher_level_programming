#!/usr/bin/python3
"""
Search API
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        letter = argv[1]
    elif len(argv) == 1:
        letter = ""
    search = {"q" : letter}
    req = requests.post(url, data=search)
    req = req.json()
    try:
        if req:
            print("{[]} {}".format(req.get('id'), req.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
