def is_zero_row(row, tolerance=1e-12):
    """
    Return True if every entry in the row is close to zero.
    """
    for value in row:
        if abs(value) > tolerance:
            return False

    return True

def leading_entry_index(row, tolerance=1e-12):
    """
    Return the index of the first nonzero entry in a row.

    If the row is zero, return None.
    """
    for j, value in enumerate(row):
        if abs(value) > tolerance:
            return j

    return None

def swap_rows(A, row_i, row_j):
    """
    Swap two rows of a matrix.
    """
    A[row_i], A[row_j] = A[row_j], A[row_i]

def scale_row(A, row_index, scalar):
    """
    Multiply a row by a scalar.
    """
    if scalar == 0:
        raise ValueError("Cannot scale a row by zero.")

    n = len(A[row_index]) # the number of columns of matrix A

    for j in range(n):
        A[row_index][j] *= scalar

def add_scaled_row(A, source_row_index, target_row_index, scalar):
    """
    Add a scalar multiple of one row to another row.
    """
    source_row = A[source_row_index]
    target_row = A[target_row_index]

    if len(source_row) != len(target_row):
        raise ValueError("Source row and target row must have the same length.")

    A[target_row_index] = [
        target_value + scalar * source_value
        for target_value, source_value in zip(target_row, source_row)
    ]