#!/usr/bin/python3

"""Prints the number of and list of arguments"""

from sys import argv

if __name__ == "__main__":
    args_count = len(argv) - 1
    args = argv[1:]

    if args_count == 0:
        print("0 arguments.")
    elif args_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_count))

    for i in range(args_count):
        print("{:d}: {}".format(i + 1, args[i]))
