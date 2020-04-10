print('Saisir une chaîne de caratère')
x=input()
if x.find('@') != -1 and x.endswith('.com'):
	print('email valide')