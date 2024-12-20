#!/usr/bin/python3
"""
  Island Perimeter
"""


def island_perimeter(grid):
    """
    It returns the perimeter of the island described in grid.
    """

    rows = len(grid)
    clms = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(clms):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == clms - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
