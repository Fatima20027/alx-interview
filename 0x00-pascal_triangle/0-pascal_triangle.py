def pascal_triangle(n):
    """
    Generates Pascal's triangle of height 'n'.

    Pascal's triangle is a triangular array of binomial coefficients.
    Each number is the sum of the two numbers directly above it.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
         list of lists of integers representing the Pascal’s triangle of n.
    """
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
