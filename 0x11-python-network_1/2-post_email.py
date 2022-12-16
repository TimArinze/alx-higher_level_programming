#!/usr/bin/python3
"""
POST an email module
"""
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
