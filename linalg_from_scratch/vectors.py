import math

def check_same_length(u,v):
    """
        Check that vectors u,v have the same length.
    """
    
    if len(u) != len(v):
        raise ValueError("Vectors must have the same length")

def add_vectors(u,v):
    """
        Add two vectors component by component.
    """

    check_same_length(u,v)

    result = []

    for i in range(len(u)):
        result.append(u[i]+v[i])
    
    return result

def subtract_vectors(u,v):
    """
        Subtract two vectors component by component.
    """

    check_same_length(u,v)

    result = []

    for i in range(len(u)):
        result.append(u[i]-v[i])
    
    return result

def scalar_mult(c,v):
    """
        Multiply a vector v by a scalar c.
    """

    result = []

    for i in range (len(v)):
        result.append(c*v[i])
    
    return result

def dot_product(u,v):
    """
        Compute the dot product of two vectors.
    """

    check_same_length(u,v)

    total = 0

    for i in range (len(u)):
        total += u[i]*v[i]
    
    return total

def norm(v):
    """
        Compute the Euclidean norm of a vector. 
    """

    return math.sqrt(dot_product(v, v))

def distance(u, v):
    """
    Compute the distance between two vectors.
    Mathematical definition: distance(u, v) = ||u - v||
    """

    return norm(subtract_vectors(u, v))

def normalise(v):
    """
    Return a unit vector in the direction of v.
    Mathematical definition: v_hat = v / ||v||
    """

    v_norm = norm(v)

    if v_norm == 0:
        raise ValueError("Cannot normalize the zero vector.")
    return scalar_mult(1 / v_norm, v)

def are_orthogonal(u, v, epsilon=1e-10):
    """
    Check whether two vectors are orthogonal.
    Two vectors are orthogonal if: u · v = 0
    
    epsilon accounts for flot rounding errors. 
    """

    return abs(dot_product(u, v)) < epsilon
def angle_between(u,v):
    """
    Find angle in radians between the two vectors.
    """
    if norm(u)*norm(v) != 0:
        return math.acos(dot_product(u,v)/(norm(u)*norm(v)))
    else:
        raise ZeroDivisionError("Cannot use a zero vector.")