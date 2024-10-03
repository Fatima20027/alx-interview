# function returns a list of lists of integers
# representing the Pascal’s triangle of n

def pascal_triangle(n):
    if n <= 0:
        return []
    mtx = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(mtx[i - 1][j - 1] + mtx[i - 1][j])
        row.append(1)
        mtx.append(row)
    return mtx
