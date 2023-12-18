#!/usr/bin/python3

"""Prints the first x element of a list and only integers"""


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    i = 0

    try:
        while i < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
    except (ValueError, TypeError):
        continue
    print()
    return (count)
