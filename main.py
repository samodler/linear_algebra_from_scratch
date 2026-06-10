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
from linalg_from_scratch.solvers import (
    augment_matrix,
    forward_elimination,
    solve_linear_system,
)

u = [3,4]
v = [5,12,6]
#print(angle_between(u,v))

A = [[1,2],[3,4]]
B = [[1,0,-7],[1,-2,5],[2,3,10]]

#print(is_square(A))
#print(trace(B))

#print(augment_matrix(A,u))
#add_scaled_row(A,0,1,-3)
#print(A)

#print (forward_elimination(augment_matrix(B,v)))
