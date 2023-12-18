#!/usr/bin/python3

"""Magic calculation"""


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        if i > a:
            result += a + b
            break
        else:
            result += (a ** b) / i

    return (result)
