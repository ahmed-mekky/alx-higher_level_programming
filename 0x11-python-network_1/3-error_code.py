#!/usr/bin/python3
"""this module is doing something"""
from urllib import request
from sys import argv
from urllib import error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as r:
            b_content = r.read()
            print(b_content.decode('UTF-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
