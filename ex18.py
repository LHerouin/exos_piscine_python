chaine = "@.123"

if chaine.find('@') != -1 and chaine.find('.') != -1:
	if chaine.index('.')+3 >= len(chaine)-1:
		print('ok')
	else:
		print("non")