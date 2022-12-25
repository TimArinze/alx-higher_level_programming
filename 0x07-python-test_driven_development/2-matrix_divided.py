#!/usr/bin/python3
"""
A function that divides all element of a matrix
"""


def matrix_divided(matrix, div):
    """ Divide a matrix """

    errmsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(errmsg)

    elif type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(errmsg)
        elif len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(errmsg)

    return [[round(element / div, 2) for element in row] for row in matrix]
