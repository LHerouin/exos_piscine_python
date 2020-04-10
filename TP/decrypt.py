import hashlib 
import io

#fonction ini mdp
def ini():
	#liste des infos
	infos = []
	#lecture fichier
	f = io.open("liste_mdp.csv", mode="r", encoding="utf-8")
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		ligne_bis = ligne.strip(";")
		infos.append(ligne_bis)
	return infos

# fonction test dico simple
def testDicoSimple(tuple):
	#lecture fichier
	f = open("dico_animaux.txt", "r")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		f2 = open("dico_animaux.txt", "r")
		for line2 in f2: 
			ligne2 = line2.strip()
			ligne_enc = hashlib.md5((ligne+ligne2).encode())
			if ligne_enc.hexdigest() == mdp :
				print("good",(ligne+ligne2), mdp)
		f2.close()

	#fermeture fichier
	f.close()

# fonction test dico + nombre
def testDicoN(tuple):
	#lecture fichier
	f = io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		for i in range(0,3501):
			ligne_enc = hashlib.md5((ligne+str(i)).encode())
			if ligne_enc.hexdigest() == mdp :
				print("good",(ligne+str(i)), mdp)
		

	#fermeture fichier
	f.close()

# fonction test Maj + dico + nombre
def testMDicoN(tuple):
	#lecture fichier
	f = io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		for i in range(0,3501):
			ligne_enc = hashlib.md5((ligne.capitalize()+str(i)).encode())
			if ligne_enc.hexdigest() == mdp :
				print("good",(ligne.capitalize()+str(i)), mdp)
		

	#fermeture fichier
	f.close()

# fonction test nombre +dico
def testNDico(tuple):
	#lecture fichier
	f = io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		for i in range(0,10000):
			ligne_enc = hashlib.md5((str(i)+ligne).encode())
			if ligne_enc.hexdigest() == mdp :
				print("good",(str(i)+ligne), mdp)
		

	#fermeture fichier
	f.close()

# fonction test Maj + nombre +dico
def testMNDico(tuple):
	#lecture fichier
	f =io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		for i in range(0,10000):
			ligne_enc = hashlib.md5((str(i)+ligne.capitalize()).encode())
			if ligne_enc.hexdigest() == mdp :
				print("good",(str(i)+ligne.capitalize()), mdp)
		

	#fermeture fichier
	f.close()

# fonction test nombre + dico + nombre
def testNDicoN(tuple):
	#lecture fichier
	f = io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		for i in range(0,10000):
			for j in range(0,10000):
				ligne_enc = hashlib.md5((str(i)+ligne+str(j)).encode())
				if ligne_enc.hexdigest() == mdp :
					print("good",(str(i)+ligne+str(j)), mdp)
		

	#fermeture fichier
	f.close()

# fonction test nombre + dico + nombre
def testMNDicoN(tuple):
	#lecture fichier
	f = io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		#test mdp
		for i in range(0,10000):
			for j in range(0,10000):
				ligne_enc = hashlib.md5((str(i)+ligne.capitalize()+str(j)).encode())
				if ligne_enc.hexdigest() == mdp :
					print("good",(str(i)+ligne.capitalize()+str(j)), mdp)
		

	#fermeture fichier
	f.close()


# fonction test dico simple
def testDicoSpe(tuple):
	#lecture fichier
	f = io.open("dico_animaux.txt", mode="r", encoding="utf-8")
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#pour chaque ligne du fichier
	for line in f: 
		#on récupère la ligne avec la fonction strip
		ligne = line.strip()
		nom_bis=''
		for i in ligne:
			if i == 'e' or i == 'a' or i == 'i' or i == 'u' or i == 'o' or i=='y' or i=='é' or i=='è' or i=='U' or i=='A' or i=='I' or i=='Y' or i=='O' or i=='E':
				nom_bis+='*'
			else:
				nom_bis+=i
			tmp = "*"
			#test mdp
		if nom_bis.count('*') == 1 :
			tmp1 = nom_bis.index("*")
			for i in range(0,10):
				nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:]
				nom_enc = hashlib.md5(nom_bis.upper().encode())
				#test
				if nom_enc.hexdigest() == mdp:
					print("good",nom_bis.upper(), mdp)

		if nom_bis.count('*') == 2 :
			tmp1 = nom_bis.index("*")
			nom_bis = nom_bis.replace("*","-",1)
			booltest = True
			for i in range(0,10):
				if booltest:
					tmp2 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest = False
				for j in range(0,10):
					nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:] 
					nom_enc = hashlib.md5(nom_bis.upper().encode())
					#test
					if nom_enc.hexdigest() == mdp:
						print("good",nom_bis.upper(), mdp)

		if nom_bis.count('*') == 3 :
			tmp1 = nom_bis.index("*")
			nom_bis = nom_bis.replace("*","-",1)
			booltest = True
			booltest2 = True
			for i in range(0,10):
				if booltest:
					tmp2 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest = False
				for j in range(0,10):
					if booltest2:
						tmp3 = nom_bis.index("*")
						nom_bis = nom_bis.replace("*","-",1)
						booltest2 = False
					for k in range(0,10):
						nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:tmp3] + str(k) +  nom_bis[tmp3 + 1:]
						nom_enc = hashlib.md5(nom_bis.upper().encode())
						#test
						if nom_enc.hexdigest() == mdp:
							print("good",nom_bis.upper(), mdp)

		if nom_bis.count('*') == 4 :
			tmp1 = nom_bis.index("*")
			nom_bis = nom_bis.replace("*","-",1)
			booltest = True
			booltest2 = True
			booltest3 = True
			for i in range(0,10):
				if booltest:
					tmp2 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest = False
				for j in range(0,10):
					if booltest2:
						tmp3 = nom_bis.index("*")
						nom_bis = nom_bis.replace("*","-",1)
						booltest2 = False
					for k in range(0,10):
						if booltest3:
							tmp4 = nom_bis.index("*")
							nom_bis = nom_bis.replace("*","-",1)
							booltest3 = False
						for l in range(0,10):
							nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:tmp3] + str(k) +  nom_bis[tmp3 + 1:tmp4] + str(l) +  nom_bis[tmp4 + 1:]
							nom_enc = hashlib.md5(nom_bis.upper().encode())
							#test
							if nom_enc.hexdigest() == mdp:
								print("good",nom_bis.upper(), mdp)

		if nom_bis.count('*') == 4 :
			tmp1 = nom_bis.index("*")
			nom_bis = nom_bis.replace("*","-",1)
			booltest = True
			booltest2 = True
			booltest3 = True
			booltest4 = True
			for i in range(0,10):
				if booltest:
					tmp2 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest = False
				for j in range(0,10):
					if booltest2:
						tmp3 = nom_bis.index("*")
						nom_bis = nom_bis.replace("*","-",1)
						booltest2 = False
					for k in range(0,10):
						if booltest3:
							tmp4 = nom_bis.index("*")
							nom_bis = nom_bis.replace("*","-",1)
							booltest3 = False
						for l in range(0,10):
							if booltest4:
								tmp5 = nom_bis.index("*")
								nom_bis = nom_bis.replace("*","-",1)
								booltest4 = False
							for m in range(0,10):
								nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:tmp3] + str(k) +  nom_bis[tmp3 + 1:tmp4] + str(l) +  nom_bis[tmp4 + 1:tmp5]+str(m) +  nom_bis[tmp5+ 1:]
								nom_enc = hashlib.md5(nom_bis.upper().encode())
								#test
								if nom_enc.hexdigest() == mdp:
									print("good",nom_bis.upper(), mdp)

	#fermeture fichier
	f.close()

# fonction test noms
def testPrenomsSpe(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	nom = tuple_mdp[0]
	nom_bis=''
	for i in nom:
		if i == 'e' or i == 'a' or i == 'i' or i == 'u' or i == 'o' or i=='y' or i=='é' or i=='è' or i=='U' or i=='A' or i=='I' or i=='Y' or i=='O' or i=='E':
			nom_bis+='*'
		else:
			nom_bis+=i
	tmp = "*"
	if nom_bis.count('*') == 1 :
		tmp1 = nom_bis.index("*")
		for i in range(0,10):
			nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:]
			nom_enc = hashlib.md5(nom_bis.upper().encode())
			#test
			if nom_enc.hexdigest() == mdp:
				print("good",nom_bis.upper(), mdp)

	if nom_bis.count('*') == 2 :
		tmp1 = nom_bis.index("*")
		nom_bis = nom_bis.replace("*","-",1)
		booltest = True
		for i in range(0,10):
			if booltest:
				tmp2 = nom_bis.index("*")
				nom_bis = nom_bis.replace("*","-",1)
				booltest = False
			for j in range(0,10):
				nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:] 
				nom_enc = hashlib.md5(nom_bis.upper().encode())
				#test
				if nom_enc.hexdigest() == mdp:
					print("good",nom_bis.upper(), mdp)

	if nom_bis.count('*') == 3 :
		tmp1 = nom_bis.index("*")
		nom_bis = nom_bis.replace("*","-",1)
		booltest = True
		booltest2 = True
		for i in range(0,10):
			if booltest:
				tmp2 = nom_bis.index("*")
				nom_bis = nom_bis.replace("*","-",1)
				booltest = False
			for j in range(0,10):
				if booltest2:
					tmp3 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest2 = False
				for k in range(0,10):
					nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:tmp3] + str(k) +  nom_bis[tmp3 + 1:]
					nom_enc = hashlib.md5(nom_bis.upper().encode())
					#test
					if nom_enc.hexdigest() == mdp:
						print("good",nom_bis.upper(), mdp)

	if nom_bis.count('*') == 4 :
		tmp1 = nom_bis.index("*")
		nom_bis = nom_bis.replace("*","-",1)
		booltest = True
		booltest2 = True
		booltest3 = True
		for i in range(0,10):
			if booltest:
				tmp2 = nom_bis.index("*")
				nom_bis = nom_bis.replace("*","-",1)
				booltest = False
			for j in range(0,10):
				if booltest2:
					tmp3 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest2 = False
				for k in range(0,10):
					if booltest3:
						tmp4 = nom_bis.index("*")
						nom_bis = nom_bis.replace("*","-",1)
						booltest3 = False
					for l in range(0,10):
						nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:tmp3] + str(k) +  nom_bis[tmp3 + 1:tmp4] + str(l) +  nom_bis[tmp4 + 1:]
						nom_enc = hashlib.md5(nom_bis.upper().encode())
						#test
						if nom_enc.hexdigest() == mdp:
							print("good",nom_bis.upper(), mdp)

	if nom_bis.count('*') == 4 :
		tmp1 = nom_bis.index("*")
		nom_bis = nom_bis.replace("*","-",1)
		booltest = True
		booltest2 = True
		booltest3 = True
		booltest4 = True
		for i in range(0,10):
			if booltest:
				tmp2 = nom_bis.index("*")
				nom_bis = nom_bis.replace("*","-",1)
				booltest = False
			for j in range(0,10):
				if booltest2:
					tmp3 = nom_bis.index("*")
					nom_bis = nom_bis.replace("*","-",1)
					booltest2 = False
				for k in range(0,10):
					if booltest3:
						tmp4 = nom_bis.index("*")
						nom_bis = nom_bis.replace("*","-",1)
						booltest3 = False
					for l in range(0,10):
						if booltest4:
							tmp5 = nom_bis.index("*")
							nom_bis = nom_bis.replace("*","-",1)
							booltest4 = False
						for m in range(0,10):
							nom_bis = nom_bis[:tmp1] + str(i) + nom_bis[tmp1 + 1:tmp2] + str(j)+ nom_bis[tmp2 + 1:tmp3] + str(k) +  nom_bis[tmp3 + 1:tmp4] + str(l) +  nom_bis[tmp4 + 1:tmp5]+str(m) +  nom_bis[tmp5+ 1:]
							nom_enc = hashlib.md5(nom_bis.upper().encode())
							#test
							if nom_enc.hexdigest() == mdp:
								print("good",nom_bis.upper(), mdp)



	


# fonction test noms+nombre
def testNomsN(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	nom = tuple_mdp[1]
	#test
	for i in range(0,10000):
		nom_enc = hashlib.md5((nom+str(i)).encode())
		if nom_enc.hexdigest() == mdp:
			print("good",(nom+str(i)), mdp)

# fonction test lettre prenom+noms+nombre
def testPNomsN(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	lettre = tuple_mdp[0][0]
	nom = tuple_mdp[1]
	#test
	for i in range(0,10000):
		nom_enc = hashlib.md5((lettre+nom+str(i)).encode())
		if nom_enc.hexdigest() == mdp:
			print("good",(lettre+nom+str(i)), mdp)


# fonction test noms
def testPrenomsN(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	prenom = tuple_mdp[0]
	
	#test
	for i in range(0,10000):
		prenom_enc = hashlib.md5((prenom.lower()+str(i)).encode())
		if prenom_enc.hexdigest() == mdp:
			print("good",(prenom.lower()+str(i)), mdp)
	

# fonction test prenoms+noms
def testPN(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	pn = tuple_mdp[0]+tuple_mdp[1]
	pn_enc = hashlib.md5(pn.encode())
	#test
	if pn_enc.hexdigest() == mdp:
		print("good",pn, mdp)

# fonction test prenoms+espace+noms
def testPEN(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	pn = tuple_mdp[0]+" "+tuple_mdp[1]
	pn_enc = hashlib.md5(pn.encode())
	#test
	if pn_enc.hexdigest() == mdp:
		print("good",pn, mdp)

# fonction test noms+prenoms
def testNP(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	pn = tuple_mdp[1]+tuple_mdp[0]
	pn_enc = hashlib.md5(pn.encode())
	#test
	if pn_enc.hexdigest() == mdp:
		print("good",pn, mdp)

# fonction test noms+espace+prenoms
def testNEP(tuple):
	#recup mdp hashé
	tuple_mdp = tuple.split(';')
	mdp = tuple_mdp[2]
	#recup nom
	pn = tuple_mdp[1]+" "+tuple_mdp[0]
	pn_enc = hashlib.md5(pn.encode())
	#test
	if pn_enc.hexdigest() == mdp:
		print("good",pn, mdp)


#initialisation
tuples_mdp=ini()


#fonction prenoms
for i in range(0,20):
	testPrenomsSpe(tuples_mdp[i])

#fonction M N dico
'''for i in range(0,20):
	testDicoSpe(tuples_mdp[i])'''

#fonction M dico N
'''for i in range(0,20):
	testMDicoN(tuples_mdp[i])'''

#fonction N dico N
'''for i in range(0,20):
	testNDicoN(tuples_mdp[i])'''

#fonction N dico
'''for i in range(0,20):
	testNDico(tuples_mdp[i])'''

#fonction dico simple
'''for i in range(0,20):
	testDicoSimple(tuples_mdp[i])'''

#fonction dico N
'''for i in range(0,20):
	testDicoN(tuples_mdp[i])'''

'''#fonction noms
for i in range(0,20):
	testNoms(tuples_mdp[i])

#fonction prenoms
for i in range(0,20):
	testPrenoms(tuples_mdp[i])

#fonction prenoms+noms
for i in range(0,20):
	testPN(tuples_mdp[i])

#fonction prenoms+espace+noms
for i in range(0,20):
	testPEN(tuples_mdp[i])

#fonction noms+prenoms
for i in range(0,20):
	testNP(tuples_mdp[i])

#fonction prenoms+espace+noms
for i in range(0,20):
	testNEP(tuples_mdp[i])

#fonction noms+Nombre
for i in range(0,20):
	testNomsN(tuples_mdp[i])
# fonction test lettre prenom+noms+nombre
for i in range(0,20):
	testPNomsN(tuples_mdp[i])'''