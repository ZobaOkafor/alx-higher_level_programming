#!/usr/bin/python3
"""Defines a name printing function"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Args:
    - first_name: string, the first name
    - last_name: string, the last name (default is an empty string)

    Raises:
    - TypeError if first_name or last_name is not a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name
                        must be a string")

    full_name = first_name + " " + last_name if last_name else first_name
    print("My name is {}".format(full_name))
