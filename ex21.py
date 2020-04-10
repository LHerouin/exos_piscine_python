#nombre de saisie
print('Saisir un nombre x')
x=int(input())
#ouverture de data.txt et écriture sur le fichier de chaine
f = open("data.txt", "a")
#Saisir x chaine
for i in range(0,x):
	print('Saisir chaine')
	chaine = input()
	f.write(chaine+'\n')
#fermeture du fichier
f.close()
