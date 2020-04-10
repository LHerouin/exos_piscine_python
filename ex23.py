#fonction compterMots
def compterMots(chaine):
	mots = chaine.split()
	for i in mots:
		#fonction count pour avoir le nombre d'occurence dans la liste mots
		print(i,' ',mots.count(i))

#lancement de la fonction
compterMots("je suis je ok ok")

