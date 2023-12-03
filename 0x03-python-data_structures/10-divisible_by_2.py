#!/usr/bin/python3

"""Finds multiples of 2 in a list"""


def divisible_by_2(my_list=[]):
    result_list = [num % 2 == 0 for num in my_list]

    return (result_list)
