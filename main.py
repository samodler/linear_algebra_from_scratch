from linalg_from_scratch.vectors import *
from linalg_from_scratch.matrices import *
from linalg_from_scratch.solvers import *

u = [3,4]
v = [5,12,6]
#print(angle_between(u,v))

A = [[1,2],[3,4]]
B = [
    [1, 2, 3, 4],
    [3, 4, 5, 6],
    [5, 6, 7, 9]
]
#print(is_square(A))
#print(trace(B))

#print(augment_matrix(A,u))
#add_scaled_row(A,0,1,-3)
#print(A)

#print (forward_elimination(augment_matrix(B,v)))

#augmented = augment_matrix(B, v)

#res_augmented = forward_elimination_augmented(augmented)
#print(res_augmented.matrix)
#print(res_augmented.rank)

#res = forward_elimination(B)
#print(res.matrix)
#print(res.rank)

#print(echelon_matrix)
#print(pivot_columns)

A = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

#ref = forward_elimination(A)
#print(ref.matrix)
#print(ref.rank)
#print(ref.row_swaps)

print(is_ref(A))

A = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 0]
]
print(is_ref(A))

A = [
    [0, 2, 3],
    [0, 4, 5],
    [0, 0, 0]
]

print(is_ref(A))

A = [
    [1, 2, 3],
    [0, 0, 5],
    [0, 5, 0]
]

print(is_ref(A))

A = [
    [0, 2, 3],
    [0, 0, 5],
    [0, 0, 0]
]
print(is_ref(A))