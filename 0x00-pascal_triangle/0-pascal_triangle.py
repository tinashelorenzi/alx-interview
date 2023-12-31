#!/usr/bin/python3
'''A module for pascal's triangle
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer based on arg int n
    '''
    if n <= 0 or type(n) is not int:
        return []
    result = []
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or i == j:
                line.append(1)
            elif j > 0 and i > 0:
                line.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(line)
    return result
