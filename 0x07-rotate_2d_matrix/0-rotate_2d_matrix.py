#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix,
        rotate it 90 degrees clockwise
    """
    mat = matrix[:]

    for i in range(len(matrix)):
        column = [row[i] for row in mat]
        matrix[i] = column[::-1]
