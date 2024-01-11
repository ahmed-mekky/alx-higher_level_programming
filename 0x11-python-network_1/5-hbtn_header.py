#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    headers = r.headers
    print(headers.get('X-Request-Id'))
