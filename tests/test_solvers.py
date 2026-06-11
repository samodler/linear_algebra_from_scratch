import pytest

from linalg_from_scratch.solvers import (
    augment_matrix,
    forward_elimination,
    back_substitution,
    solve_linear_system,
)


def assert_matrix_close(actual, expected, tolerance=1e-12):
    """
    Compare two matrices using floating-point tolerance.
    """
    assert len(actual) == len(expected)

    for actual_row, expected_row in zip(actual, expected):
        assert len(actual_row) == len(expected_row)

        for actual_value, expected_value in zip(actual_row, expected_row):
            assert actual_value == pytest.approx(expected_value, abs=tolerance)


def assert_vector_close(actual, expected, tolerance=1e-12):
    """
    Compare two vectors using floating-point tolerance.
    """
    assert len(actual) == len(expected)

    for actual_value, expected_value in zip(actual, expected):
        assert actual_value == pytest.approx(expected_value, abs=tolerance)


# ---------------------------------------------------------
# augment_matrix tests
# ---------------------------------------------------------


def test_augment_matrix_combines_A_and_b():
    A = [
        [1, 2],
        [3, 4],
    ]

    b = [5, 6]

    result = augment_matrix(A, b)

    expected = [
        [1, 2, 5],
        [3, 4, 6],
    ]

    assert result == expected


def test_augment_matrix_does_not_mutate_original_matrix():
    A = [
        [1, 2],
        [3, 4],
    ]

    b = [5, 6]

    original_A = [
        [1, 2],
        [3, 4],
    ]

    augment_matrix(A, b)

    assert A == original_A


def test_augment_matrix_raises_error_if_b_has_wrong_length():
    A = [
        [1, 2],
        [3, 4],
    ]

    b = [5]

    with pytest.raises(ValueError, match="Length of the vector"):
        augment_matrix(A, b)


# ---------------------------------------------------------
# forward_elimination tests
# ---------------------------------------------------------


def test_forward_elimination_returns_row_echelon_form_for_square_system():
    augmented = [
        [2, 1, 5],
        [4, 4, 12],
    ]

    result, pivot_columns = forward_elimination(augmented)

    expected = [
        [4, 4, 12],
        [0, -1, -1],
    ]

    assert_matrix_close(result, expected)
    assert pivot_columns == [0, 1]


def test_forward_elimination_does_not_mutate_input():
    augmented = [
        [2, 1, 5],
        [4, 4, 12],
    ]

    original = [
        [2, 1, 5],
        [4, 4, 12],
    ]

    forward_elimination(augmented)

    assert augmented == original


def test_forward_elimination_works_for_tall_matrix():
    augmented = [
        [1, 1, 2],
        [2, 3, 5],
        [3, 4, 7],
    ]

    result, pivot_columns = forward_elimination(augmented)

    expected = [
        [3, 4, 7],
        [0, 1 / 3, 1 / 3],
        [0, 0, 0],
    ]

    assert_matrix_close(result, expected)
    assert pivot_columns == [0, 1]


def test_forward_elimination_skips_singular_column():
    augmented = [
        [0, 1, 2],
        [0, 3, 6],
    ]

    result, pivot_columns = forward_elimination(augmented)

    expected = [
        [0, 3, 6],
        [0, 0, 0],
    ]

    assert_matrix_close(result, expected)
    assert pivot_columns == [1]


# ---------------------------------------------------------
# back_substitution tests
# ---------------------------------------------------------


def test_back_substitution_solves_upper_triangular_system():
    upper_triangular_augmented = [
        [2, 1, 5],
        [0, 3, 6],
    ]

    result = back_substitution(upper_triangular_augmented)

    expected = [1.5, 2]

    assert_vector_close(result, expected)


def test_back_substitution_raises_error_for_zero_diagonal_entry():
    upper_triangular_augmented = [
        [2, 1, 5],
        [0, 0, 6],
    ]

    with pytest.raises(ValueError, match="singular or nearly singular"):
        back_substitution(upper_triangular_augmented)


# ---------------------------------------------------------
# solve_linear_system tests
# ---------------------------------------------------------


def test_solve_linear_system_solves_simple_2_by_2_system():
    A = [
        [2, 1],
        [4, 4],
    ]

    b = [5, 12]

    result = solve_linear_system(A, b)

    expected = [2, 1]

    assert_vector_close(result, expected)


def test_solve_linear_system_solves_3_by_3_system():
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]

    b = [8, -11, -3]

    result = solve_linear_system(A, b)

    expected = [2, 3, -1]

    assert_vector_close(result, expected)


def test_solve_linear_system_handles_zero_first_pivot_by_swapping_rows():
    A = [
        [0, 2],
        [1, 3],
    ]

    b = [4, 5]

    result = solve_linear_system(A, b)

    expected = [-1, 2]

    assert_vector_close(result, expected)


def test_solve_linear_system_does_not_mutate_inputs():
    A = [
        [2, 1],
        [4, 4],
    ]

    b = [5, 12]

    original_A = [
        [2, 1],
        [4, 4],
    ]

    original_b = [5, 12]

    solve_linear_system(A, b)

    assert A == original_A
    assert b == original_b


def test_solve_linear_system_raises_error_for_non_square_matrix():
    A = [
        [1, 2, 3],
        [4, 5, 6],
    ]

    b = [7, 8]

    with pytest.raises(ValueError, match="square matrix"):
        solve_linear_system(A, b)


def test_solve_linear_system_raises_error_if_b_has_wrong_length():
    A = [
        [1, 2],
        [3, 4],
    ]

    b = [5]

    with pytest.raises(ValueError, match="Length of b"):
        solve_linear_system(A, b)


def test_solve_linear_system_raises_error_for_singular_matrix():
    A = [
        [1, 2],
        [2, 4],
    ]

    b = [3, 6]

    with pytest.raises(ValueError, match="singular or nearly singular"):
        solve_linear_system(A, b)