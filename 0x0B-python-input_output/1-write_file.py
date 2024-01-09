#!/usr/bin/python3
"""Defines a file writing function."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters written.

    Parameters:
    - filename (str): The name of the file to write to. Defaults to an empty string.
    - text (str): The string to be written to the file.

    Returns:
    - int: The number of characters written to the file.

    Note:
    The function uses the 'with' statement to automatically handle file operations.
    It creates the file if it doesn't exist and overwrites its content if it already exists.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        nb_characters_written = file.write(text)
    return (nb_characters_written)
