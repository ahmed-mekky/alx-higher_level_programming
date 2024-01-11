#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {"email": argv[2]}
    r = requests.post(argv[1], data=data)
    print(r.text)
