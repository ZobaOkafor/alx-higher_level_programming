#!/usr/bin/python3
"""
Module that contains the load_from_json_file function.
"""


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    Parameters:
    - filename (str): The name of the file containing the JSON
    representation of the object.

    Returns:
    - obj: The Python data structure represented by the JSON file.

    Note:
    The function uses the 'with' statement to automatically
    handle file operations.
    It does not manage exceptions if the JSON string doesn't
    represent an object.
    """
    import json
    with open(filename, encoding="utf-8") as file:
        return (json.load(file))
