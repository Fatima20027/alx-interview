#!/usr/bin/python3
"""
This method determines if all boxes can be opened, given an array of boxes.
Each box contains keys that unlock other boxes.

The algorithm uses Depth-First Search (DFS) to explore the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked starting from the first box.

    The function starts from box 0 (always unlocked) and uses a stack
    to keep track of which boxes are available to unlock.

    Returns:
    -------
    bool
        Returns True if all boxes can be unlocked, otherwise False.
    """

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)
    return all(unlocked)
