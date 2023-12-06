#!/usr/bin/python3

"""Adds all unique integers in a list"""


def uniq_add(my_list=[]):
    uniq_dict = {}
    result = 0

    for num in my_list:
        if num not in uniq_dict:
            uniq_dict[num] = True
            result += num

    return (result)
