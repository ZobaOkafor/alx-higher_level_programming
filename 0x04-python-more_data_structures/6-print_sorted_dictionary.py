#!/usr/bin/python3

"""Prints a dictionary by ordered keys"""


def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())

    for key in sort_keys:
        print("{}: {}".format(key, a_dictionary[key]))
