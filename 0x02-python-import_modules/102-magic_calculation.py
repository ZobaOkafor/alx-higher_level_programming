#!/usr/bin/python3

"""Magic calculation that replicates the workings of provided bytecode"""


def magic_calculation(a, b):
    if a < b:
        from magic_calculation_102 import add, sub
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)
        return (C)

    else:
        return (sub(a, b))
