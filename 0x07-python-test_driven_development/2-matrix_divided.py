#!/usr/bin/python3
"""Defines a matrix division function"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    - matrix: list of lists of integers or floats.
    - div: number (integer or float) to divide the matrix elements by.

    Raises:
    - TypeError: If the matrix contains non-numbers.
    - TypeError: If the matrix contains rows of different sizes.
    - TypeError: if div is not an int or float.
    - ZeroDivisionError: If div is 0.

    Returns:
    - new matrix with elements rounded to 2 decimal places
    """

    if not all(
        isinstance(row, list) and
        all(isinstance(element, (int, float)) for element in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix
    ]

    return (result_matrix)
