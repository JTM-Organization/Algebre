from random import randrange
from traceback import extract_tb

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
        for j in range(p):
            A[i].append(B[i][0])

    return(A)

def decolle(M):
    P = []
    Q = []
    n,p = dimension(M)
    for i in range(n):
        P.append([M[i][p-1]])
        Q.append([])
        for j in range(p-1):
            Q[i].append(M[i][j])
    
    return Q,P

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
            l = -(M[j][i]/M[i][i])
            transvect(M,j,i,l)
    
    return(M)

def SolutionTriangulaire(A,B):
    n,p = dimension(A)
    x = [0 for i in range(n)]
    x[n-1] = B[n-1][0]/A[n-1][n-1]
    for i in range(n-2,-1,-1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j] * x[j]
            x[i] = (B[i][0] - s) / A[i][i]
    return x

def solve(A,B):
    colle(A,B)
    gauss(A)
    decolle(A)
    A,B = decolle(A)
    return SolutionTriangulaire(A,B)

"""def pivotMax(A,i):
    n,p = dimension(A)
    maxi = A[i][0]
    i_max = 0
    for j in range(p):
        if A[i][j] > maxi:
            maxi = A[i][j]
            i_max = j
    return i_max"""


M = [[1,3,1], [5,4,1], [1,2,1]]
B = [[1], [1], [2]]
