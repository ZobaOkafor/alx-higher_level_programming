#!/usr/bin/python3
"""
This module contains a function that adds two numbers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers or floats.

    Args:
        a: first integer/float
        b: second integer/float

    Raises:
        TypeError: if a or b is not an integer or a float

    Returns:
        The addition of the given numbers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
