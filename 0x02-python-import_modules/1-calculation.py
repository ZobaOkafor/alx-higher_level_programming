#!/usr/bin/python3
"""Prints the sum, difference, multiple and quotient of 10 and 5"""

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5

    add_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, add_result))
    print("{:d} - {:d} = {:d}".format(a, b, sub_result))
    print("{:d} * {:d} = {:d}".format(a, b, mul_result))
    print("{:d} / {:d} = {:d}".format(a, b, div_result))