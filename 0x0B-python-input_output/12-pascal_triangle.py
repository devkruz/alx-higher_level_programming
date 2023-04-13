#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []
    pascal = [[1]]
    for row in range(n - 1):
        arr_row = []
        tmp = [0] + pascal[-1] + [0]
        for index in range(1, len(tmp)):
            sum = tmp[index - 1] + tmp[index]
            arr_row.append(sum)
        pascal.append(arr_row)
    return pascal
