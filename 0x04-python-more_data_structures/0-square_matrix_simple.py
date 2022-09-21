#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    product=[[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            product[i][j] = matrix[i][j] ** 2
    return product
