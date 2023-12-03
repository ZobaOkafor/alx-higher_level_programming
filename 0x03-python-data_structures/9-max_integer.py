#!/usr/bin/python3

"""Finds the biggest integer of a list"""


def max_integer(my_list=[]):
    if my_list:
        max_value = my_list[0]

        for num in my_list:
            if num > max_value:
                max_value = num

        return (max_value)
    else:
        return (None)
