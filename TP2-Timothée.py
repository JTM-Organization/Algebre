# -*- coding: utf-8 -*-

from random import randrange


def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()  


def extraireColonne(A,j):
    p=len(A[0])
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

    print("Matrice collée :")
    afficher(A)


def decolle(M):
    P = []
    Q = []
    n,p = dimension(M)
    for i in range(n):
        P.append([M[i][p-1]])
        Q.append([])
        for j in range(p-1):
            Q[i].append(M[i][j])
    
    print("\nGrande matrice:")
    afficher(Q)
    print("\nPetite matrice:")
    afficher(P)
    return Q,P


def transvect(A,i1,i2,landa):
    n,p = dimension(A)
    for i in range(p):
        A[i1][i] += (A[i2][i])*landa
    
    afficher(A)


def permut(A,i1,i2):
    echange = A[i1]
    A[i1] = A[i2]
    A[i2] = echange
    
    afficher(A)


def gauss(M):
    p,q = dimension(M)
    for i in range(p):
        print("Étape", i)
        for j in range(i+1,p):
            l = -(M[j][i]/M[i][i])
            transvect(M,j,i,l)
        afficher(M)


A = [[1,2,3],[0,4,5],[0,0,6]]
B = [[1,-1,-4,13,1],[-1,2,6,-21,-1],[2,-1,-4,12,2],[2,0,-2,5,2]]



def solutionTriangulaire(A,B):
    n,p = dimension(A)
    I=[[0 for colonne in range(p)] for ligne in range(n)]
    for i in range(p):
        I[i][i] = 1
    
    colle(A,I)
    for b in range(n-1):
        for a in range (p):
            del I[a][0]
        colle(A,I)
            
    for i in range(p-1,0,-1):
        print("")
        for j in range(i-1,-1,-1):
            l = -(A[j][i]/A[i][i])
            transvect(A,j,i,l)
            
    n,p = dimension(A)        
    for i in range(n):
        if A[i][i]!=1:
            div = A[i][i]
            for j in range(p):
                A[i][j] /= div

    afficher(A)
   
    decolle(A)
    A ,B = decolle(A)
    decolle(A)
    A ,B = decolle(A)
    decolle(A)
    A ,B = decolle(A)
        
    
    
solutionTriangulaire(A,B)
