#!/usr/bin/python3
"""
Module that contains the to_json_string function.
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Parameters:
    - my_obj: The object to be converted to JSON.

    Returns:
    - str: The JSON representation of the object.

    Note:
    Exceptions are not managed if the object can't be serialized.
    """
    import json
    return (json.dumps(my_obj))
