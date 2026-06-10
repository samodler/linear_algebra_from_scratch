from linalg_from_scratch.vectors import dot_product

def shape (A):
    """
        Return the shape of a matrix: number of rows (m), number of columns (n).
        A matrix is represented as a list of rows: 
            [[a11, a12,..., a1n], 
             [a21, a22,..., amn]]
    """
    m = len(A)

    if m == 0:
        return 0, 0
    
    n = len(A[0])

    for row in A:
        if len(row) != n:
            raise ValueError("All rows must have the same length.")
    return m, n

def zeros(m, n):
    """
    Create a zero m by n matrix.
    """
    matrix = []
    for i in range(m):
        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix

def identity(n):
    """
    Create the an n by n identity matrix.
    """
    I = zeros(n, n)

    for i in range(n):
        I[i][i] = 1

    return I

def transpose(A):
    """
    Transpose an m by n matrix.
    If A has entries A_ij, then A^T has entries A_ji.
    """
    m, n = shape(A)

    result = zeros(n, m)

    for i in range(m):
        for j in range(n):
            result[j][i] = A[i][j]

    return result

def add_matrices(A, B):
    """
    Add two m by n matrices component by component.
    """
    m_A, n_A = shape(A)
    m_B, n_B = shape(B)

    if m_A != m_B or n_A != n_B:
        raise ValueError("Matrices must have the same shape.")

    result = zeros(m_A, n_A)

    for i in range(m_A):
        for j in range(n_A):
            result[i][j] = A[i][j] + B[i][j]

    return result

def scalar_multiply_matrix(c, A):
    """
    Multiply an m by n matrix by a scalar.
    """
    return [[c * value for value in row] for row in A]

def matrix_vector_multiply(A, v):
    """
    Multiply an m by n matrix by a vector.
    If v has length n, then vector u = Av has length m.
    """
    m, n = shape(A)

    if n != len(v):
        raise ValueError("Number of matrix columns must match vector length.")

    u = []

    for i in range(m):
        curr_element = 0

        for j in range(n):
            curr_element += A[i][j] * v[j]

        u.append(curr_element)

    return u

def matrix_multiply(A, B):
    """
    Multiply two matrices.
    If A is m by n and B is n by p, then A*B is m by p.
    """
    m_A, n_A = shape(A)
    m_B, n_B = shape(B)

    if n_A != m_B:
        raise ValueError("Number of columns of A must equal number of rows of B.")

    result = zeros(m_A, n_B)

    for i in range(m_A):
        for j in range(n_B):
            curr_element = 0

            for k in range(n_A):
                curr_element += A[i][k] * B[k][j]

            result[i][j] = curr_element

    return result

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

def is_square(A):
    """
    Check if matrix A is squre - the nummber of rows and columns are equal, m=n. 
    """
    m,n = shape(A)
    return m == n

def trace(A):
    """
    Find the trace of matrix A.
    Trace operation defined for square matrices only.
    """
    trace = 0
    if is_square(A):
        for i in range(len(A)):
            trace += A[i][i]
    else:
        raise ValueError("Trace operation is only defined for square matrices.")
    return trace