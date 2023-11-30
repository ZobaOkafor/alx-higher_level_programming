#!/usr/bin/python3

"""Magic calculation that replicates the workings of provided bytecode"""


def magic_calculation(a, b):
    add = __import__('magic_calculation_102').add
    sub = __import__('magic_calculation_102').sub

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (C)

    else:
        return (__import__('magic_calculation_102').sub(a, b))
