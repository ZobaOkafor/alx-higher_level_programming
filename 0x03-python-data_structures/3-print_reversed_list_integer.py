#!/usr/bin/python3

"""Prints all integers of a list in reverse order"""


def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[num]))


print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

