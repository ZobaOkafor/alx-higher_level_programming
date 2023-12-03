#!/usr/bin/python3

"""Removes all charcters 'c' and 'C' from a string"""


def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() not in ('c', 'C'):
            new_string += char
    return (new_string)
