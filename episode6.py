#import de biblio pour tester l'existence du fichier
import os.path
from os import path


#fonction episode 5 modif
def triAffichage(liste):
	#on parcourt la liste
	i = 0
	while i<(len(liste)-1):
		#on créer deux liste, une pour la ligne courant, une autre pour la prochaine ligne
		liste_tmp = liste[i].split('\\')
		liste_tmp2 = liste[i+1].split('\\')
		#si le premier élément de la ligne courante et plus petit que celui de la prochaine ligne, on l'affiche
		if liste_tmp[1]<liste_tmp2[1]:
			print("Oui")
		else:
			print("Non")
		i+=1


#demande de saisie d'un nom de fichier
print("Saisir un nom de fichier")
x = input()
#test si le fichier existe
if path.exists(x) :
	#lecture du fichier
	f = open(x, "r")
	#tableau de ligne
	tb_ligne = []
	#pour chaque ligne du fichier
	for line in f: 
		tmp = line.strip()
		tmp2 = ''.join(tmp)
		tb_ligne.append(str(tmp2))
	#lancement fonction
	triAffichage(tb_ligne)

	#fermeture fichier
	f.close()

else :
	print("fichier non trouvé")