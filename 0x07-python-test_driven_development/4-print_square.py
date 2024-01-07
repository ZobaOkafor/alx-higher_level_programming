#!/usr/bin/python3
"""Defines a module for square printing"""


def print_square(size):
    """
    Prints a square of '#' characters.

    Args:
    - size: integer, the size length of the square

    Raises:
    - TypeError if size is not an integer or if size is a float
    - ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
