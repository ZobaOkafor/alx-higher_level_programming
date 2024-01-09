#!/usr/bin/python3
"""
Module for is_same_class function.
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class;
    otherwise False.

    Args:
    - obj: object to check
    - a_class: specified class for comparison

    Returns:
    - True if obj is an instance of a_class, False otherwise
    """
    return (type(obj) is a_class)
