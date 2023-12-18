#!/usr/bin/python3

"""Raises a type exception"""


def raise_exception():
    raise TypeError("Exception raised")

raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
