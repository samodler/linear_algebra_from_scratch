from linalg_from_scratch.matrices import *


def get_column(A, column_index):
    """
    Extract one column from a matrix.
    """
    m, n = shape(A)

    if column_index < 0 or column_index >= n:
        raise IndexError("Column index is out of range.")

    column = []

    for i in range(m):
        column.append(A[i][column_index])

    return column