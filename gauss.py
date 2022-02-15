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
  
A = [[1,2,3],[4,5,6],[7,8,9]]  
def transvect(A,i1,i2;lamda):
  n,p = dimension(A)
  for i in range (n):
      A[i][c1]=A[i][c1]+A[i][c2]*lamda
  
def permut(A, c1, c2):
    afficher(A)
    n,p=dimension(A)
    col1=extraireColonne(A, c1)
    col2=extraireColonne(A, c2)
    memory=col1
    col1=col2
    col2=memory
    for i in range (n):
        A[i][c1]=col1[i]
        A[i][c2]=col2[i]
    afficher(A)

    
