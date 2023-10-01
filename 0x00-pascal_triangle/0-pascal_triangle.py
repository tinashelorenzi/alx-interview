#!/usr/bin/python3
'''A module for pascal's triangle
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer based on arg int n
    '''
    if n <= 0 or type(n) not is int:
        return []
    result = [[1]]
    for i in range(1, n):
        prev_row = result[-1]
        row = [1]
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        row.append(1)
        result.append(row)
    return result
