#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        for index in range(len(row)):
            print("{:d}".format(row[index]), end="")
            if index != (len(row) - 1):
                print(" ", end="")
        print("")
