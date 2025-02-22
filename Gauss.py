import numpy as np
import warnings

def swapRows(A, i, j):
    """
    interchange two rows of A
    operates on A in place
    """
    tmp = A[i].copy()
    A[i] = A[j]
    A[j] = tmp

def relError(a, b):
    """
    compute the relative error of a and b
    """
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        try:
            return np.abs(a-b)/np.max(np.abs(np.array([a, b])))
        except:
            return 0.0

def rowReduce(A, i, j, pivot):
    """
    reduce row j using row i with pivot pivot, in matrix A
    operates on A in place
    """
    factor = A[j][pivot] / A[i][pivot]
    for k in range(len(A[j])):
        if np.isclose(A[j][k], factor * A[i][k]):
            A[j][k] = 0.0
        else:
            A[j][k] = A[j][k] - factor * A[i][k]


# stage 1 (forward elimination)
def forwardElimination(B):
    """
    Return the row echelon form of B
    """
    A = B.copy().astype(float)
    m, n = np.shape(A)
    for i in range(m-1):
        # Let lefmostNonZeroCol be the position of the leftmost nonzero value 
        # in row i or any row below it 
        leftmostNonZeroRow = m
        leftmostNonZeroCol = n
        ## for each row below row i (including row i)
        for h in range(i,m):
            ## search, starting from the left, for the first nonzero
            for k in range(i,n):
                if (A[h][k] != 0.0) and (k < leftmostNonZeroCol):
                    leftmostNonZeroRow = h
                    leftmostNonZeroCol = k
                    break
        # if there is no such position, stop
        if leftmostNonZeroRow == m:
            break
        # If the leftmostNonZeroCol in row i is zero, swap this row 
        # with a row below it
        # to make that position nonzero. This creates a pivot in that position.
        if (leftmostNonZeroRow > i):
            swapRows(A, leftmostNonZeroRow, i)
        # Use row reduction operations to create zeros in all positions 
        # below the pivot.
        for h in range(i+1,m):
            rowReduce(A, i, h, leftmostNonZeroCol)
    return A

#################### 

# If any operation creates a row that is all zeros except the last element,
# the system is inconsistent; stop.
def inconsistentSystem(A):
    """
    B is assumed to be in echelon form; return True if it represents
    an inconsistent system, and False otherwise
    
    for r in range(len(A)):
        entries = False
        for c in range(len(A[0])-1):
            if A[r,c] != 0:
                entries = True
        if (A[r][len(A[0])-1] !=0) & (entries):
            return True
    return False
    """
    entries = False
    for c in range(len(A[0])-1):
        if A[len(A)-1,c] != 0:
            entries = True
    if ((entries == False) & (A[len(A)-1,len(A[0])-1] != 0)):
        return True
    return False



      

def backsubstitution(B):
    """
    B is assumed to be return the reduced row echelon form matrix of B
    """
    i = 0

    while (i < len(B)):                                             #loop through each row of matrix
        for c in range(len(B[0])-1):                                #loop through each column of row
            if B[i,c] != 0:                                     #stop when reaching leading entry
                div = B[i,c]                                        #save value of leading entry
                for entry in range(c,len(B[0])):                   #for each entry to left of lead
                    B[i,entry] = B[i,entry]/div                      #divide by lead value
                                             
                for r in range(len(B)):                               #for each row
                    if (B[r,c] != 0) & (r != i):                                    #if there is a nonzero in the leading column
                        """
                        reduce row j using row i with pivot pivot, in matrix A
                        operates on A in place(A, i, j, pivot)
                        """
                        rowReduce(B, i, r, c)                          #row reduce 
                break
        i = i+1
    return B







# Create a 3x3 matrix
def solve(A):
    A = forwardElimination(A)
    #print("echeon: \n",A)
    #print(inconsistentSystem(A))
    if (inconsistentSystem(A) == False):
        A = backsubstitution(A)
        #print("reduced: \n",A)
        return A
    else:
        return "no solutions"

"""
C = np.array([[35,27,299.5],[5300,6700,49270],[215,330,2086]])
H = np.array([[4,2,3,-19],[-3,2,2,-2],[-6,-1,-3,22]])
I = np.array([[4,2,8,3],[-3,2,1,2],[-6,-1,-8,-3]])
k = np.array( [[ 3, 1, 2,-4, 1], [ 1,-7,-2, 6,-4], [ 3, 4, 2, 2, 3], [-2, 0,-1,-7,-3]] )
JA1 = np.array([[3,1,2,-4],[1,1,2,-2],[6,-4,-8,4],[2,2,4,-2]])
print(forwardElimination(k))
print()
print()
A = np.array([[1,0,-1,-1,0,50],[1,1,0,0,0,110],[0,1,1,0,-1,40],[0,0,0,1,1,20]])
Ab = np.array([[1,0,-1,0,50],[1,1,0,0,110],[0,1,1,-1,40],[0,0,0,1,20]])
Ac = np.array([[1,0,-1,0,50],[1,1,0,0,110],[0,1,1,-1,40],[0,0,0,1,15]])
"""

Ba = np.array([[1,-1,0,0,0,0,80],[0,1,-1,0,0,0,-10],[0,0,1,-1,0,0,120],[0,0,0,1,-1,0,-90],[0,0,0,0,1,-1,50],[-1,0,0,0,0,1,-150]])
G = np.array([[6,-18,-4],[4,-12,2],[6,-18,5]])
print(solve(G))





