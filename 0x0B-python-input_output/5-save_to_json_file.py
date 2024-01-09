#!/usr/bin/python3
"""
Module that contains the save_to_json_file function.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Parameters:
    - my_obj: The object to be saved to the file.
    - filename (str): The name of the file to save the object to.

    Returns:
    - None

    Note:
    The function uses the 'with' statement to automatically handle
    file operations.
    It does not manage exceptions if the object can't be serialized
    or file permission exceptions.
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
