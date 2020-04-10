#lecture fichier data.txt
f = open("data.txt", "r")
#pour chaque ligne du fichier
for line in f: 
	#on récupère la ligne avec la fonction strip
	ligne = line.strip()
	#test si email est valide
	if ligne.find('@') != -1 and ligne.endswith('.com'):
		print('email valide')
	else:
		print("email invalide")

#fermeture fichier
f.close()