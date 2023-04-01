#!/usr/bin/python3
"""Define matrix_divided."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""

    if isinstance(matrix, list) is not True:
        raise TypeError("matrix must be a matrix\
                        (list of lists) of integers/floats")

    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError("matrix must be a matrix (list of lists\
                             of integers/floats")
        for num in row:
            if isinstance(num, int) is False and\
                    isinstance(num, float) is False:
                raise TypeError("matrix must be a matrix (list of lists)\
                                 of integers/floats")

    size = len(matrix[0])

    div_matrix = []

    for row in matrix:
        new_array = []
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            new_array.append(round(num / div, 2))
        div_matrix.append(new_array)

    return div_matrix
