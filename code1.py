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
  #On realise l'arborescence, et on l'affiche
  tab = repeat_to_length('\t',level+1)
  weight=np.count_nonzero(M)
  if leaf:
    print(tab + ('leaf',weight))
  else:
    print(tab + ('branch',weight))

def repeat_to_length(string_to_expand, length):
    return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

def initMatrix(n,m):
  return np.zeros(shape=(n,m)) # init a matrix 8/8

def initPoints(M):
  size = M.shape()
  n = size[0] #nombre lignes matrice
  m = size[1] #nombre colonnes matrice
  maxPoints = randint(4, int(n*m/6)) #Obtention aleatoire d'un nombre de points
  for i in range(maxPoints): #On place les points de coordonnees aleatoires
    (x,y) = getRandomPoints(m,n)
    M[x,y] = 1
  return M

def getRandomPoints(m,n):
  #Pour obtenir des points aléatoires
  x = randint(0, m-1)
  y = randint(0, n-1)
  return (x,y)

def decoupe(M):
  size = M.shape # (8,8)
  n = size[0] #taille d'une ligne
  m = size[1] # taille d'une colonne
  newSizeN = n // 2 #taille d'une ligne coupee en deux
  newSizeM = m // 2 #taille d'une colonne coupee en deux
  M1 = M[0:newSizeN,0:newSizeM] #Matrice nw
  M2 = M[newSizeN:n,0:newSizeM] #Matrice sw
  M3 = M[0:newSizeN,newSizeM:m] #Matrice ne
  M4 = M[newSizeN:n,newSizeM:m] #Matrice se
  return (M1, M2, M3, M4)

def countPoints(M):
  return np.count_nonzero(M)

############################################
############################################
#############  END FUNCTIONS   #############
############################################
############################################


