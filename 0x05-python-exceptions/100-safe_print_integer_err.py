#!/usr/bin/python3

"""Prints an integer"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return (False)
