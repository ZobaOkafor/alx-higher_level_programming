#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing
    a specific string.

    Args:
    - filename (str): The name of the file.
    - search_string (str): The specific string to search for in each line.
    - new_string (str): The line of text to be inserted after each
    line containing the search string.
    """
    lines = []

    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
