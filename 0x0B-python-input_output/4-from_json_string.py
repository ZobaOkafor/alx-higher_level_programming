#!/usr/bin/python3
"""
Module that contains the from_json_string function.
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Parameters:
    - my_str (str): The JSON string to be converted to a Python object.

    Returns:
    - obj: The Python data structure represented by the JSON string.

    Note:
    Exceptions are not managed if the JSON string doesn't represent an object.
    """
    import json
    return (json.loads(my_str))
