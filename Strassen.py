#Page 44

import numpy as np
def squareMatrixMultipluRecursive(A,B):
    n = len(A)
    if(n ==1):
        return A[0]*B[0]

    C = np.array(A)
    mid_n = int(n/2)
    C[:mid_n,:mid_n] = squareMatrixMultipluRecursive(A[:mid_n,:mid_n],B[:mid_n,:mid_n])+squareMatrixMultipluRecursive(A[:mid_n,mid_n:],B[mid_n:,:mid_n])
    C[:mid_n,mid_n:] = squareMatrixMultipluRecursive(A[:mid_n,:mid_n],B[:mid_n,mid_n:])+squareMatrixMultipluRecursive(A[:mid_n,mid_n:],B[mid_n:,mid_n:])
    C[mid_n:,:mid_n] = squareMatrixMultipluRecursive(A[mid_n:,:mid_n],B[:mid_n,:mid_n])+squareMatrixMultipluRecursive(A[mid_n:,mid_n:],B[mid_n:,:mid_n])
    C[mid_n:,mid_n:] = squareMatrixMultipluRecursive(A[mid_n:,:mid_n],B[:mid_n,mid_n:])+squareMatrixMultipluRecursive(A[mid_n:,mid_n:],B[mid_n:,mid_n:])

    return C

def strassen(A,B):
    n = len(A)
    if(n ==1):
        return A[0]*B[0]

    C = np.array(A)
    mid_n = int(n/2)
    A11 = A[:mid_n,:mid_n]
    A12 = A[:mid_n,mid_n:]
    A21 = A[mid_n:,:mid_n]
    A22 = A[mid_n:,mid_n:]

    B11 = B[:mid_n,:mid_n]
    B12 = B[:mid_n,mid_n:]
    B21 = B[mid_n:,:mid_n]
    B22 = B[mid_n:,mid_n:]

    S1 = B12-B22
    S2 = A11+A12
    S3 = A21+A22
    S4 = B21-B11
    S5 = A11+A22
    S6 = B11+B22
    S7 = A12-A22
    S8 = B21+B22
    S9 = A11-A21
    S10 = B11+B12

    P1 = strassen(A11,S1)
    P2 = strassen(S2,B22)
    P3 = strassen(S3,B11)
    P4 = strassen(A22,S4)
    P5 = strassen(S5,S6)
    P6 = strassen(S7,S8)
    P7 = strassen(S9,S10)

    C[:mid_n, :mid_n] = P5+P4-P2+P6
    C[:mid_n, mid_n:] = P1+P2
    C[mid_n:, :mid_n] = P3+P4
    C[mid_n:, mid_n:] = P5+P1-P3-P7


    return C


import numpy as np

a = np.array(
[[1,2,1,4],
 [10,6,1,1],
 [1,1,7,1],
 [1,9,1,1]]
)
b = np.array(
[[1,1,1,1],
 [1,133,1,1],
 [1,14,1,1],
 [1,1,71,1]]
)
c = squareMatrixMultipluRecursive(a,b)

c_true = np.matmul(a,b)
print(c)

c_s = strassen(a,b)
print(c_s)
