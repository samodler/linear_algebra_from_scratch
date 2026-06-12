# linalg_from_scratch/elimination.py

from dataclasses import dataclass

from linalg_from_scratch.matrices import shape, copy_matrix
from linalg_from_scratch.row_operations import swap_rows, add_scaled_row


@dataclass
class EliminationResult:
    matrix: list[list[float]]
    pivot_columns: list[int]
    row_swaps: int
    rank: int


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

def forward_elimination_augmented (augmented, tolerance=1e-12):
    """
    Converts an augmented matrix [A|b] in row echelon form.

    Works for rectangular systems as well as square systems.


    Returns
    -------
    EliminationResult
        A dataclass instance containing:
        - matrix: the row echelon form of the augmented matrix
        - pivot_columns: a list of variable-column indices where pivots were found
        - row_swaps: the number of row swaps performed
        - rank: the number of pivots found
    """
    A = copy_matrix(augmented)

    rows, columns = shape(A)

    num_of_variable_columns = columns - 1 #last column is vector b

    pivot_row = 0
    pivot_columns = []
    row_swaps = 0

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
            row_swaps += 1
        
        pivot = A[pivot_row][pivot_column]

        for row_below in range(pivot_row + 1, rows):
            factor = -A[row_below][pivot_column] / pivot
            add_scaled_row(A, pivot_row, row_below, factor)
        
        pivot_columns.append(pivot_column)
        pivot_row += 1

    return EliminationResult(
        matrix=A,
        pivot_columns=pivot_columns,
        row_swaps=row_swaps,
        rank=len(pivot_columns),
    )

def forward_elimination (A, tolerance=1e-12):
    """
    Converts matrix A in row echelon form.

    Works for rectangular systems as well as square systems.


    Returns
    -------
    EliminationResult
        A dataclass instance containing:
        - matrix: the row echelon form of the augmented matrix
        - pivot_columns: a list of variable-column indices where pivots were found
        - row_swaps: the number of row swaps performed
        - rank: the number of pivots found
    """
    matrix_copy = copy_matrix(A)

    rows, columns = shape(matrix_copy)

    pivot_row = 0
    pivot_columns = []
    row_swaps = 0

    for pivot_column in range(columns):
        if pivot_row >= rows:
            break

        try:
            best_row = find_pivot_row(
                matrix_copy, 
                pivot_column=pivot_column,
                start_row=pivot_row,
                tolerance=tolerance
                )
        except ValueError:
            continue

        if best_row != pivot_row:
            swap_rows(matrix_copy, pivot_row, best_row)
            row_swaps += 1
        
        pivot = matrix_copy[pivot_row][pivot_column]

        for row_below in range(pivot_row + 1, rows):
            factor = -matrix_copy[row_below][pivot_column] / pivot
            add_scaled_row(matrix_copy, pivot_row, row_below, factor)
        
        pivot_columns.append(pivot_column)
        pivot_row += 1

    return EliminationResult(
        matrix=matrix_copy,
        pivot_columns=pivot_columns,
        row_swaps=row_swaps,
        rank=len(pivot_columns),
    )