#!/usr/bin/python3

"""Magic calculation"""


def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            result += (a ** b) / i
        if i > a:
            raise Exception('Too far')
        except Exception:
            result = b + a
            break

    return (result)
