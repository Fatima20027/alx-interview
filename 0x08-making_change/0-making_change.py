#!/usr/bin/python3
"""
Contains makeChange function
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins required to achieve the given total.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    combination = [float('inf')] * (total + 1)
    combination[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            combination[i] = combination[i - coin] + 1
    if combination[total] != float('inf'):
        return combination[total]
    else:
        return -1
