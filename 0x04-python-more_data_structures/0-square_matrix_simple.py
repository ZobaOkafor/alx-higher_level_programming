#!/usr/bin/python3

"""Computes the square value of all integers of a matrix"""


def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            element = matrix[row][col]
            squared_element = element ** 2
            new_matrix[row][col] = squared_element

    return (new_matrix)
