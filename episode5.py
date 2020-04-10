#definition de la fonction
def triAffichage(liste):
	#on parcourt la liste
	i = 0
	while i<(len(liste)-1):
		#on créer deux liste, une pour la ligne courant, une autre pour la prochaine ligne
		liste_tmp = liste[i].split('\\')
		liste_tmp2 = liste[i+1].split('\\')
		#si le premier élément de la ligne courante et plus petit que celui de la prochaine ligne, on l'affiche
		if liste_tmp[1]<liste_tmp2[1]:
			print(liste[i])
		i+=1







#definition de la liste
list_exo = ['\\a\\t80cm\\t60cm\\n','\\b\\t81cm\\t51cm\\n','\\b\\t105cm\\t145cm\\n']
#lancement de la fonction
triAffichage(list_exo)