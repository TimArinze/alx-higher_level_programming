#!/usr/bin/python3
"""
Search API
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(argv) == 1 else argv[1]
    payload = {"q" : letter}
    req = requests.post(url, data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("{[]} {}".format(response.get('id'), response.get('name')))
    except:
        print("Not a valid JSON")
