#!/usr/bin/python3
# method that determines if all the boxes can be opened.

# using DFS

def canUnlockAll(boxes):
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


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
