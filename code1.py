import numpy as np
from random import randint

#------------------------------
#http://arborjs.org/docs/barnes-hut

############################################
############################################
#############  FUNCTIONS   #################
############################################
############################################
def processMatrix(M, level):
  # 2. on decoupe la matrice en 4 sous matrices
  Ms = decoupe(M)
  for Mm in Ms:
    # 3. on compte le nombre de point dans nos sous matrices
    if countPoints(Mm) < 2:# 3.1 on a au plus un point l'arbre s'arrete 
      printMatrix(Mm,level,True)
    else:# 3.2 on a au moins deux points
      #recursivity
      printMatrix(Mm,level,False)
      processMatrix(Mm, level+1)
  # 3.2.1 on recommence la decoupe selon le point 2.
  #------------------------------

def printMatrix(M, level, leaf):
  tab = repeat_to_length('\t',level+1)
  if leaf:
    print(tab + 'leaf')
  else:
    print(tab + 'branch')

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def initMatrix(n,m):
  return np.zeros(shape=(n,m)) # init a matrix 8/8

def initPoints(M):#TODO randomize
  size = M.shape
  n = size[0]
  m = size[1]
  maxPoints = randint(4, int(n*m/6))
  for i in range(maxPoints): 
    (x,y) = getRandomPoints(m,n)
    M[x,y] = 1
  return M

def getRandomPoints(m,n):
  x = randint(0, m-1)
  y = randint(0, n-1)
  return (x,y)

def decoupe(M):
  size = M.shape # (8,8)
  n = size[0]
  m = size[1]
  newSizeN = n // 2
  newSizeM = m // 2
  M1 = M[0:newSizeN,0:newSizeM]
  M2 = M[newSizeN:n,0:newSizeM]
  M3 = M[0:newSizeN,newSizeM:m]
  M4 = M[newSizeN:n,newSizeM:m]
  return (M1, M2, M3, M4)

def countPoints(M):
  return np.count_nonzero(M)

############################################
############################################
#############  END FUNCTIONS   #############
############################################
############################################

# Init our system
i = randint(2, 9)
n = i*2
m = n # to have a square matrix
M = initMatrix(n, m)

# 1. on place des points aleatoire dans notre matrice
M = initPoints(M)

# go !!!
processMatrix(M, 0)