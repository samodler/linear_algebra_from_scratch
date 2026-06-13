from dataclasses import dataclass

from linalg_from_scratch.matrices import *
from linalg_from_scratch.elimination import *
from linalg_from_scratch.row_operations import *

@dataclass
class LinearSystemClassification:
    status: str
    rank_A: int
    rank_augmented: int
    number_of_variables: int


def augment_matrix(A, b):
    """
    Create the augmented matrix [A | b].
    """
    m, n = shape(A)

    if len(b) != m:
        raise ValueError("Length of the vector must match the number of rows of the matrix.")
    
    return [A[i].copy() + [b[i]] for i in range (m)]

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

    elimination_result = forward_elimination_augmented(augmented)
    
    if elimination_result.rank != columns:
        raise ValueError("Matrix is singular or nearly singular.")

    solution = back_substitution(elimination_result.matrix)

    return solution

def classify_linear_system(A, b):
    """
    Classify the linear system Ax = b.

    Returns:
        LinearSystemClassification with status:
        - "unique"
        - "infinite"
        - "inconsistent"
    """
    rows, columns = shape(A)

    if len(b) != rows:
        raise ValueError("Length of b must match the number of rows of A.")

    augmented = augment_matrix(A, b)

    rank_A = rank(A)
    rank_augmented = rank(augmented)
    number_of_variables = columns

    if rank_A < rank_augmented:
        status = "inconsistent"
    elif rank_A == rank_augmented == number_of_variables:
        status = "unique"
    else:
        status = "infinite"

    return LinearSystemClassification(
        status=status,
        rank_A=rank_A,
        rank_augmented=rank_augmented,
        number_of_variables=number_of_variables,
    )
