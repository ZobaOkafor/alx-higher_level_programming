#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number and returns its value"""
    last_num = abs(number) % 10
    print("{}".format(last_num), end="")
    return last_num
