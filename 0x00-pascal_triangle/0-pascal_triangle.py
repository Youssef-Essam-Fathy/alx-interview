#!/usr/bin/python3

"""
No module importing
"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (int): _description_

    Returns:
        List of lists of int: _description_
    """
    if n <= 0:
        return []

    triangleElements = [[1]]

    if n == 1:
        return triangleElements

    for i in range(1, n):
        baseRow = triangleElements[-1]
        row = [1]
        for j in range(1, i):
            row.append(baseRow[j] + baseRow[(j - 1)])
        row.append(1)
        triangleElements.append(row)
    return triangleElements
