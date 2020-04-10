#import de tous les éléments de la bibli math
from math import *
#fonction volumeSphere
def volumeSphere(r):
	#calcul de du valume de la sphere via le rayon
	return (4/3)*pi*r**3

#lancement de la fonction et affichage resu
print(volumeSphere(5))