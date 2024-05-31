#!/usr/bin/env python3
"""
Module 0-pascal_triangle.py
In this function it will generate pascal triangle
"""


def fact(numb):
    """this method will return the factorial of the number"""
    if numb == 0 or numb == 1:
        return 1
    else:
        pro = 1
        for i in range(1, numb + 1):
            pro *= i
        return pro


def pascal_triangle(n):
    try:
        if n <= 0:
            return []
        else:
            lists = []
            for i in range(n):
                row = []
                for j in range(i + 1):
                    row.append(fact(i) // (fact(j) * fact(i - j)))
                lists.append(row)
            return lists
    except Exception:
        return []