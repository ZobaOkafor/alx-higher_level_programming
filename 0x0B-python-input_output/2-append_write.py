#!/usr/bin/python3
"""Defines a file appending function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.

    Parameters:
    - filename (str): The name of the file to append to.
    Defaults to an empty string.
    - text (str): The string to be appended to the file.

    Returns:
    - int: The number of characters added to the file.

    Note:
    The function uses the 'with' statement to automatically handle file
    operations.
    If the file doesn't exist, it will be created.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        nb_characters_added = file.write(text)
    return (nb_characters_added)
