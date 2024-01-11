#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print(f"Error code: {r.status_code}")
