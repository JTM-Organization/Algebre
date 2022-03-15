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

def gauss(M):
    for j in range(len(M)):
        for i in range(j+1,len(M[0])):
            if int(M[j][j])!=0:
                landa=-(M[i][j]/M[j][j])
                transvect(M,i,j,landa)
    return M



M = [[1,3,1],[5,4,1],[1,2,1]]
P = [[1],[1],[1]]

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
    for j in range(len(A)):
        for i in range(j+1,len(A[0])):
            if int(A[j][j])!=0:
                landa=-(A[i][j]/A[j][j])
                transvect(A,i,j,landa)
                B[i][0]*=landa
    return solution_triangulaire(A,B)

def pivotMax(A,i):
    i_max = i
    for j in range(i+1,len(A)):
        if abs(A[j][i]) > abs(A[i_max][i]):
            i_max = j
    return i_max

def gauss(M):
    for j in range(len(M)):
        for i in range(j+1,len(M[0])):
            if int(M[j][j])!=0:
                landa=-(M[i][j]/M[j][j])
                transvect(M,i,j,landa)
    return M
    
def gauss2(M):
    for j in range(len(M)):
        k = pivotMax(M,j)
        if j > k:
            permut(M,j,k)
        for i in range(j+1,len(M[0])):
            if int(M[j][j])!=0:
                landa = -(M[i][j]/M[j][j])
                transvect(M,i,j,landa)
    return M

afficher(gauss2(M))


