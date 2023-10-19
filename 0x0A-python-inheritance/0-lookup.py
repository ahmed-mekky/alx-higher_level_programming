#!/usr/bin/python3
"""
    idk
"""
def get_attributes_and_methods(obj):
    """
        This function returns a dictionary with the attributes and methods of an object.
    """
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
