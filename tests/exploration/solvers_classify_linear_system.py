from linalg_from_scratch.solvers import classify_linear_system

examples = [
    (
        "unique square",
        [[1, 2], [3, 4]],
        [5, 11],
    ),
    (
        "infinite square dependent",
        [[1, 2], [2, 4]],
        [5, 10],
    ),
    (
        "inconsistent square dependent",
        [[1, 2], [2, 4]],
        [5, 11],
    ),
    (
        "unique overdetermined",
        [[1, 0], [0, 1], [1, 1]],
        [2, 3, 5],
    ),
    (
        "infinite underdetermined",
        [[1, 2, 3], [2, 4, 6]],
        [6, 12],
    ),
    (
        "inconsistent underdetermined",
        [[1, 2, 3], [2, 4, 6]],
        [6, 13],
    ),
]

for name, A, b in examples:
    result = classify_linear_system(A, b)
    print(name)
    print(result)
    print()
