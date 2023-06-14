#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nmatrix = []
    for col in matrix:
        ans = list(map(lambda x: x**2, col))
        nmatrix.append(ans)
    return nmatrix
