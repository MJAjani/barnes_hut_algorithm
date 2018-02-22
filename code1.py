import numpy as np
#------------------------------
M=np.zeros(shape=(11,11))
M[0,0]=1
M[0,8]=1
M[4,7]=1
M[8,3]=1
M[10,6]=1
def premiere_decoupe(M):
    """Arguments : matrice M a traiter"""
    """Sauvegarde les 4 sous-matrices 'decoupees' et les iterations dans une liste(point(cardinal,depth))"""
    taille=np.shape(M)[0]
    coupe=taille//2
    nw=M[0:taille//2,0:coupe]
    sw=M[coupe+1:taille,0:coupe]
    ne=M[0:coupe,coupe+1:taille]
    se=M[coupe+1:taille,coupe+1:taille]

#------------------------------
def decoupe(M):
	if np.sum(M)<=rechercheMaxMatrice(M):
		return()
	else:
		premiere_decoupe(M)

print(M)  
premiere_decoupe(M)

    
def quadtree():
    "Retourne le quad-tree"
#---------

  
def rechercheMaxMatrice(M):
  coef_max=M[0][0]
  for i in np.shape(M)[0]:
    for j in np.shape(M)[1]:
      if M[i][j]>coef_max:
        coef_max=M[i][j]
  return coef_max