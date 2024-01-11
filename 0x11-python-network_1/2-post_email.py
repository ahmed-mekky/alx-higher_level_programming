#!/usr/bin/python3
"""this module is doing something"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    data = {"email": argv[2]}
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)

    with request.urlopen(req) as r:
        print(r.read().decode("UTF-8"))
