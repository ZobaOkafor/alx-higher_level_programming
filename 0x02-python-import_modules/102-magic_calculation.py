#!/usr/bin/python3

"""Magic calculation that replicates the workings of provided bytecode"""


import magic_calculation_102

def magic_calculation(a, b):
    if a < b:
        add = magic_calculation_102.add 
        sub = magic_calculation_101.sub
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return (sub(a, b))
