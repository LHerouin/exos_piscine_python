#fonction Somme
def somme(n1,n2,n3):
	return n1+n2+n3

#programme principal
#définition tuple de 3 nombres
tuple3 = (1,2,3)
#décompression du tuple
v1,v2,v3 = tuple3
#appel et affichage fonction
print(somme(v1,v2,v3))