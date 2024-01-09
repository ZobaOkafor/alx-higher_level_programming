#!/usr/bin/python3
"""
Module that contains the class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.

    Parameters:
    - obj: An instance of a class.

    Returns:
    - dict: The dictionary representation of the object suitable
    for JSON serialization.
    """
    json_dict = {}

    # Iterate over the attributes of the object
    for key, value in obj.__dict__.items():
        # Check if the attribute is serializable
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value

    return (json_dict)
