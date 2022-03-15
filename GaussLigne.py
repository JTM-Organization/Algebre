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
        for j in range(n):
            A[i].append(B[i][j])

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
    echange = A[i1]
    A[i1] = A[i2]
    A[i2] = echange
    
    afficher(A)

def gauss(M):
    p,q = dimension(M)
    for i in range(p):
        for j in range(i+1,p):
            l = -(M[j][i]//M[i][i])
            transvect(M,j,i,l)

def SolutionTriangulaire(A,B):
    n, p = dimension(A)
    colle(A,B)
    for i in range(p-1,-1,-1):
        print("i = ", i)
        for j in range(i-1,-1,-1):
            print("j = ", j)
            l = -(A[j][i]//A[i][i])
            transvect(A,j,i,l)
            afficher(A)

M = [[1,-1,-4,13],[-1,2,6,-21],[2,-1,-4,12],[2,0,-2,5]]
B = [[1, 2, 3, 4],[5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
I = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

gauss(M)
SolutionTriangulaire(M,I)