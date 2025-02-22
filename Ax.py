import numpy as np

def innerProduct(a,b):
    """
    Takes two vectors a and b, of equal length, and returns their inner product
    """
    assert(len(a) == len(b))
    total = 0;
    for i in range(len(a)):
        total += a[i]*b[i]
    return total
    

def AxIP(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    v = np.zeros([len(A)])
    for i in range(len(A)):
        v[i] = innerProduct(A[i],x)
    return v

def AxVS(A,x):
    """
    Takes a matrix A and a vector x and returns their product
    """
    "initialize resultant vector"
    total = np.zeros([len(A)])

    "loop through each column in matrix"
    for c in range(len(A[0])):
        "initialize column to zero"
        vec = np.zeros([len(A)])
        "loop through rows to create vertical vector"
        for r in range(len(A)):
            vec[r] = A[r,c]
        "multiply each column by corresponding component from x"
        vec *= x[c] 
        total += vec
    return total