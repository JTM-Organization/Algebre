from suuuu import *

def transvect2(A,i1,i2,landa):
    p = len(A[0])
    for i in range(p):
        A[i1][i] += (A[i2][i])*landa

def gauss2(M):
    n,p=dimension(M)
    for i in range(n):

        for j in range(i+1,p):
            if M[i][i]!=0 and M[i][i]!=0.0:
                landa = -(M[j][i]/M[i][i])
                transvect2(M,j,i,landa)
            afficher(M)
            print()
    afficher(M)
    return M

def produitIteratif(A):
    n=len(A)
    produit=A[0][0]
    for i in range(1,n):
        produit*=A[i][i]
    return produit

def produitRecursif(A):
    if len(A)==0:
        return 1
    n=len(A)-1
    s=A[n][n]
    B=[[A[i][j] for j in range(n)] for i in range(n)]
    return s*produitRecursif(B)

B=[[1,2,0,-1],[2,0,1,1],[3,1,0,1],[2,-1,1,0]]
#afficher(gauss2(B))

C=[[-2,2,1,2],[2,1,2,2],[2,-2,-2,2],[1,0,-2,-1]]
k=gauss2(C)

print(produitIteratif(k))
