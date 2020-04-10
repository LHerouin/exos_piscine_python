#fonction conversion de devises
def conversionDevises():
	Euros = 0
	AriAry = 0
	print("commencer la saisie par EA pour conversion euros et  AE pour AriAry")
	x = input()
	#conversion euros en ariary
	if x.startswith('EA'):
		AriAry = float(x[3:len(x)])*4111.06
		print(AriAry,"AriAry")
	#conversion ariary en euros
	elif x.startswith('AE'):
		Euros = float(x[3:len(x)])/4111.06
		print(Euros,"Euros")
	#mauvaise saisie
	else:
		print("Erreur de saisie")

#lancement fonction
conversionDevises()