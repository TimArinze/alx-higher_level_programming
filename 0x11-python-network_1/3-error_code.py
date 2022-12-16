#!/usr/bin/python3
"""
Error code #0
"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
