#!/usr/bin/python3
"""this module is doing something"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        print(r.text)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {r.status_code}")
