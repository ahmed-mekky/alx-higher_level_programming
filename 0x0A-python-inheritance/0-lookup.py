#!/usr/bin/python3
def get_attributes_and_methods(obj):
    return [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
