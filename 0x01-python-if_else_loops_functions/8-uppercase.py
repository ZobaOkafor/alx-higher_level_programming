#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase"""
    for alpha in str:
        upper_alpha = alpha
        if 'a' <= alpha <= 'z':
            upper_alpha = chr(ord(alpha) - ord('a') + ord('A'))
        print("{}".format(upper_alpha), end="")

    print()
