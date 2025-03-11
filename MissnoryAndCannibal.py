import numpy as np

def LtoR(M, C, L, R):
    L[0] -= M
    L[1] -= C
    R[0] += M
    R[1] += C
    print(L, "-> (", M, C, ") -> ", R)
    Check(R)

def RtoL(M, C, L, R):
    R[0] -= M
    R[1] -= C
    L[0] += M
    L[1] += C
    print(L, "-> (", M, C, ") --> ", R)
    Check(L)

def Check(R):
    if R[0] == 3 and R[1] == 3:
        print("Done!!")

L = np.array([3, 3])
R = np.array([0, 0])

LtoR(1, 1, L, R)
RtoL(1, 0, L, R)
LtoR(0, 2, L, R)
RtoL(0, 1, L, R)
LtoR(2, 0, L, R)
RtoL(1, 1, L, R)
LtoR(2, 0, L, R)
RtoL(0, 1, L, R)
LtoR(0, 2, L, R)
RtoL(0, 1, L, R)
LtoR(0, 2, L, R)
