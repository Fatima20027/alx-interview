#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations (copy and paste) needed
    to achieve exactly n 'H' characters.
    """
    if n <= 0:
        return 0

    op = 0
    i = 2

    while n > 1:
        while n % i == 0:
            op += i
            n //= i
        i += 1
    return op
