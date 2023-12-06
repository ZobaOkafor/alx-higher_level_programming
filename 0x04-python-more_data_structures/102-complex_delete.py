#!/usr/bin/python3

"""Deletes keys with a specific value in a dictionary"""


def complex_delete(a_dictionary, value):
    keys_to_del = [key for key, val in a_dictionary.items() if val == value]

    for key in keys_to_del:
            a_dictionary.pop(key)

    return (a_dictionary)
