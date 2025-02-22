import numpy as np
import Ax
import Gauss as gs

def main():
    A = np.array([[1,2,1],[3,1,1],[1,2,7]])
    x = np.array([5,5,4])
    print(Ax.AxIP(A,x))
    print(Ax.AxVS(A,x))

