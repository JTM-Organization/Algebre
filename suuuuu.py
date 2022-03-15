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

def transvect(A,i1,i2,landa):
    n,p = dimension(A)
    for i in range(p):
        A[i1][i] += (A[i2][i])*landa

def permut(A,i1,i2):
    A[i1],A[i2]=A[i2],A[i1]
    afficher(A)


def solution_triangulaire(A,B):
    n,n=dimension(A)
    X=[0]*n
    X[n-1]=B[n-1][0]/A[n-1][n-1]
    for i in range(n-1,0,-1):
        s=0
        for j in range(i,n-1):
            s=s+A[i][j]*X[j]
        X[i]=(B[i][0]-s)/A[i][i]
    return X

def solve(A,B):
    n,p=dimension(A)
    for i in range(n):
        for j in range(i+1,p):
            if A[i][i]!=0 and A[i][i]!=0:
                landa=-(A[j][i]/A[i][i])
                transvect(A,j,i,landa)
                B[j][0]*=landa
    return solution_triangulaire(A,B)

def pivotMax(A,c):
    n=len(A)
    i_max = c
    for i in range(c+1,n):
        if abs(A[i][c]) > abs(A[i_max][c]):
            i_max = i
    return i_max


def gauss(M):
    n,p=dimension(M)
    for i in range(n):
        for j in range(i+1,p):
            if M[i][i]!=0.0 and M[i][i]!=0:
                landa=-(M[j][i]/M[i][i])
                transvect(M,j,i,landa)
    return M

def gauss2(M):
    n,p=dimension(M)
    for i in range(n):
        k = pivotMax(M,i)
        if i > k:
            permut(M,i,k)
        for j in range(i+1,p):
            if int(M[i][i])!=0:
                landa = -(M[j][i]/M[i][i])
                transvect(M,j,i,landa)
    return M

def solve2(A,B):
    n,p=dimension(A)
    for i in range(n):
        k = pivotMax(A,i)
        if i > k:
            permut(A,i,k)
        for j in range(i+1,p):
            if A[i][i]!=0.0 and A[i][i]!=0:
                landa = -(A[j][i]/A[i][i])
                transvect(A,j,i,landa)
                B[j][0]*=landa
    return solution_triangulaire(A,B)

M = [[0,1,1,2],[1,0,0,1],[0,1,0,1]]

afficher(gauss2(M))
