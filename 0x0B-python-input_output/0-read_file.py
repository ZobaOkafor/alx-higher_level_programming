#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Parameters:
    - filename (str): The name of the file to be read.
    Defaults to an empty string.

    Returns:
    - None

    Note:
    The function uses the 'with' statement to automatically close
    the file after reading.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
