#!/usr/bin/python3
"""Defines a text-indentation module"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
    - text: string, the input text

    Raises:
    - TypeError if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = {'.', '?', ':'}
    lines = []

    current_line = ""
    for char in text:
        if char in punctuation:
            lines.append(current_line.strip())
            current_line = ""
        else:
            current_line += char

    for line in lines:
        print(line)
        print()
