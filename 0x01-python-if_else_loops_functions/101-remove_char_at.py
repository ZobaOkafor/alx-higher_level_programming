#!/usr/bin/python3

"""Creates a copy of a string while removing the character at 'n' position"""


def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return (str)

    return (str[:n] + str[n + 1:])
