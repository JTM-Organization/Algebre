from biblio import *

def colle(A):
    n=len(A)
    compteur=0
    for i in range(n):
        for j in range(n):
            if j==compteur:
                A[i].append(1)
            else:
                A[i].append(0)
        compteur+=1
    return A

def dimension(A):
    n = len(A)
    p = len(A[0])
    return n,p

def decolle(B):
    n=len(B)
    M=[[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j]=B[i][j+n]
    return M

def transvect(A,i1,i2,landa):
    p = len(A[0])
    for i in range(p):
        A[i1][i] -= (A[i2][i])*landa

def dilat(A,i,landa):
    p = len(A[0])
    for j in range(p):
        A[i][j] = landa*A[i][j]
    return A

def inverse(A):
    M=colle(A)
    gauss3(M)
    print()
    k=decolle(M)

    return k

def pivotMax(A,c):
    n=len(A)
    i_max = c
    for i in range(c+1,n):
        if abs(A[i][c]) > abs(A[i_max][c]):
            i_max = i
    return i_max

def permut(A,i1,i2):
    A[i1],A[i2]=A[i2],A[i1]

def gauss3(M):
    n=len(M)
    for i in range(n):
        k = pivotMax(M,i)
        permut(M,i,k)
        dilat(M,i,1/M[i][i])
        for j in range(i+1,n):
            if M[i][i]!=0 and M[i][i]!=0.0:
                transvect(M,j,i,M[j][i])
    for i in range(n-1,-1,-1):
        for j in range(i-1,-1,-1):
            transvect(M,j,i,M[j][i])
    return M
