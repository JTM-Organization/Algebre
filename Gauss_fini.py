# -*- coding: utf-8 -*-

from random import randrange

A = [[0.0000000001,1],[1,1]]

B = [[1],[2]]

N = [[0,1,1,2],[1,0,0,1],[0,1,0,1]]

def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()  


def extraireColonne(A,j):
    p=len(A)
    col=[]
    for i in range(p):
        col.append(A[i][j])
    return col


def dimension(A):
    n = len(A)
    p = len(A[0])
    return n,p


def colle(A,B):
    n,p = dimension(B)
    for i in range(n):
        A[i].append(B[i][0])

    #print("Matrice collée :")
    #afficher(A)
    return A


def decolle(M):
    A = []
    B = []
    n,p = dimension(M)
    for i in range(n):
        B.append([M[i][p-1]])
        A.append([])
        for j in range(p-1):
            A[i].append(M[i][j])
    
    #print("\nGrande matrice:")
    #afficher(Q)
    #print("\nPetite matrice:")
    #afficher(P)
    return A,B


def transvect(A,i1,i2,landa):
    n,p = dimension(A)
    for i in range(p):
        A[i1][i] += (A[i2][i])*landa
    #afficher(A)


def permut(A,i1,i2):
    echange = A[i1]
    A[i1] = A[i2]
    A[i2] = echange
    #afficher(A)


def gauss(M):
    n,p = dimension(M)
    for j in range(n):
        for i in range(j+1, n):
            landa = -(A[i][j]/A[j][j])
            transvect(A, i, j, landa)
    return M


def solutionTriangulaire(A,B):
    n,p = dimension(A)
    X = [[0 for colonne in range(1)] for ligne in range(n)]
    X[n-1][0] = B[n-1][0]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1, n):
            s = s + A[i][j]*X[j][0]
        X[i][0] = (B[i][0]-s)/A[i][i]
    return X


def solve(A,B):
    A = colle(A,B)
    A = gauss(A)
    A, B = decolle(A)
    return solutionTriangulaire(A, B)


def pivotMax(A,u):
    n,p = dimension(A)
    indice_pivot_maximal = 0
    for i in range(1,n):
        if A[i][u] < 0:
            A[i][u] *= -1
        if A[i][u] >= A[indice_pivot_maximal][u]:
            indice_pivot_maximal = i
    return indice_pivot_maximal


def gauss2(M):
    n,p = dimension(M)
    for j in range(n):
        if M[j][j]==0:
            v = pivotMax(M,j)
            permut(M,j,v)
        for i in range(j+1, n):
            landa = -(A[i][j]/A[j][j])
            transvect(A, i, j, landa)
    return M


def solve2(A,B):
    A = colle(A,B)
    A = gauss2(A)
    A, B = decolle(A)
    return solutionTriangulaire(A, B)

print(solve(A,B))
print(solve2(A,B))  
