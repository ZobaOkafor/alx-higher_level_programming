#!/usr/bin/python3
"""Defines a function to add a new attribute to an object"""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible"""
    if (
        hasattr(obj, "__dict__") or
        (hasattr(obj, "__slots__") and attribute in obj.__slots__)
    ):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
