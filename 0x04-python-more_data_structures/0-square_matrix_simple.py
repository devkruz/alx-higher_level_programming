#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []
        for index in range(len(row)):
            new_row.append((row[index] ** 2))
        new_matrix.append(new_row)

    return new_matrix
