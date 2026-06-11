from linalg_from_scratch.matrices import shape

def copy_matrix(A):
    """
    Create a deep copy of a matrix.
    """
    copy = []

    for row in A:
        copy.append(row.copy())

    return copy

def augment_matrix(A, b):
    """
    Create the augmented matrix [A | b].
    """
    m, n = shape(A)

    if len(b) != m:
        raise ValueError("Length of the vector must match the number of rows of the matrix.")
    
    return [A[i].copy() + [b[i]] for i in range (m)]

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

def find_pivot_row(A, pivot_column, start_row, tolerance=1e-12):
    """
    Find the row with the largest absolute value in a pivot column.
    """
    best_row = start_row
    best_value = abs(A[start_row][pivot_column])

    for row in range(start_row + 1, len(A)):
        value = abs(A[row][pivot_column])

        if value > best_value:
            best_value = value
            best_row = row

    if best_value < tolerance:
        raise ValueError("Matrix is singular or nearly singular.")

    return best_row

def forward_elimination_square_only(augmented):
    """
    Convert the augmented matrix [A | b] into upper triangular form.
    Assumes A is a square matrix. 
    """
    A = copy_matrix(augmented)

    rows, columns = shape(A)

    # The last column is b, so the number of variable columns is columns - 1
    number_of_variables = columns - 1
    if rows != number_of_variables:
        raise ValueError("This solver expects a square system: "
            f"{rows} equations and {number_of_variables} variables were given."
        )

    for pivot_index in range(number_of_variables):
        # 1. Find the best pivot row
        pivot_row = find_pivot_row(
            A,
            pivot_column=pivot_index,
            start_row=pivot_index,
        )

        # 2. Move the best pivot row into the pivot position
        if pivot_row != pivot_index:
            swap_rows(A, pivot_index, pivot_row)

        pivot = A[pivot_index][pivot_index]

        # 3. Eliminate entries below the pivot
        for row_below in range(pivot_index + 1, rows):
            factor = -A[row_below][pivot_index] / pivot
            add_scaled_row(A, pivot_index, row_below, factor)

    return A

def forward_elimination (augmented, tolerance=1e-12):
    """
    Converts an augmented matrix [A|b] in row echelon form.
    Works for any matrix shape (i.e, square, tall, etc).
    Returns:
    A: the row echelon form of the augmented matrix.
    pivot_columns: list of columns where pivots were found. 
    """
    A = copy_matrix(augmented)

    rows, columns = shape(A)

    num_of_variable_columns = columns - 1 #last column is vector b

    pivot_row = 0
    pivot_columns = []

    for pivot_column in range(num_of_variable_columns):
        if pivot_row >= rows:
            break

        try:
            best_row = find_pivot_row(
                A, 
                pivot_column=pivot_column,
                start_row=pivot_row,
                tolerance=tolerance
                )
        except ValueError:
            continue

        if best_row != pivot_row:
            swap_rows(A, pivot_row, best_row)
        
        pivot = A[pivot_row][pivot_column]

        for row_below in range(pivot_row + 1, rows):
            factor = -A[row_below][pivot_column] / pivot
            add_scaled_row(A, pivot_row, row_below, factor)
        
        pivot_columns.append(pivot_column)
        pivot_row += 1

    return A, pivot_columns

def back_substitution(upper_triangular_augmented, tolerance=1e-12):
    """
    Solve an upper triangular system using back substitution.
    """
    A = upper_triangular_augmented

    rows, columns = shape(A)
    number_of_variables = columns - 1

    solution = [0 for x in range(number_of_variables)]

    for i in range(number_of_variables - 1, -1, -1):
        diagonal_entry = A[i][i]

        if abs(diagonal_entry) < tolerance:
            raise ValueError("Matrix is singular or nearly singular.")

        right_hand_side = A[i][-1]

        known_terms = 0

        for j in range(i + 1, number_of_variables):
            known_terms += A[i][j] * solution[j]

        solution[i] = (right_hand_side - known_terms) / diagonal_entry

    return solution


def solve_linear_system(A, b):
    """
    Solve Ax = b using Gaussian elimination with partial pivoting.

    Steps:

        1. Build augmented matrix [A | b].
        2. Convert it to upper triangular form.
        3. Use back substitution.
    """
    rows, columns = shape(A)

    if rows != columns:
        raise ValueError("A must be a square matrix.")

    if len(b) != rows:
        raise ValueError("Length of b must match the number of rows of A.")

    augmented = augment_matrix(A, b)

    upper_triangular = forward_elimination(augmented)

    solution = back_substitution(upper_triangular)

    return solution