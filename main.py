from linalg_from_scratch.vectors import (
    add_vectors,
    subtract_vectors,
    scalar_mult,
    dot_product,
    norm,
    distance,
    normalise,
    are_orthogonal,
    angle_between
)

from linalg_from_scratch.matrices import (
    shape,
    identity,
    transpose,
    add_matrices,
    scalar_multiply_matrix,
    matrix_vector_multiply,
    matrix_multiply,
    is_square,
    trace
)

u = [3,4]
v = [5,12]
print(angle_between(u,v))

A = [[1,2],[3,4]]
B = [[1,2],[3,4],[5,6]]
print(is_square(A))
print(trace(B))
