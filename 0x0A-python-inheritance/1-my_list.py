#!/usr/bin/python3
"""
Inheritance Modules
"""


class MyList(list):
    """
    This thing adds something to the world.
    """
    def print_sorted(self):
        print(sorted(self))
