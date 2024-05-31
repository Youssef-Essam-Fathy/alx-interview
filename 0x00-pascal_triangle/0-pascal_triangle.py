#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n.
    """

    if n <= 0:
        return []

    RLIST = []
    lst = []
    for i in range(n):
        if len(lst) == 0:
            lst.append(1)
            RLIST.append([1])
        elif len(lst) == 1:
            lst.append(1)
            RLIST.append([1, 1])
        else:
            ndlst = []
            x = 0
            while x < len(lst):
                if x + 1 != len(lst):
                    ndlst.append(lst[x] + lst[x + 1])
                x += 1
            lst = [1]
            lst.extend(ndlst)
            lst.append(1)
            RLIST.append(lst)
    return RLIST
