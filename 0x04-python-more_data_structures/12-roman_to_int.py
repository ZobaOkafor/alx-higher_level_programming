#!/usr/bin/python3

"""Converts a Roman numeral to an integer"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)

    roman_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0

    for i in range(len(roman_str)):
        current_value = roman_n[roman_str[i]]

        if i < len(roman_string) - 1 and roman_n[roman_str[i + 1]] > current_value:
            total -= current_value
        else:
            total += current_value

    return (total)
