from random import randrange

def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()

def extraireColonne(A,j):
    p=len(A[0])-(len(A[0])-len(A))
    col=[]
    for i in range(p):
        col.append(A[i][j])
    return col
  
def dimension(A):
  n = len(A)
  p = len(A[0])
  return n,p
    
def transvect(A,c1,c2,lamda):
  n,p = dimension(A)
  for i in range (n):
      A[i][c1]=A[i][c1]+A[i][c2]*lamda
  
def permut(A, c1, c2):
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
    
def gauss(A):
    print("La matrice avant échelonnement:")
    afficher(A)
    n,p=dimension(A)
    for i in range (p):
        col1=extraireColonne(A, i)
        for j in range (p):
            col2=extraireColonne(A, j)
            if i<j:
                if A[i][j]!=0:
                    lamda=(-col2[i])/(col1[i])
                    transvect(A, j, i, lamda)
    print("La matrice après échelonnement:")
    afficher(A)
