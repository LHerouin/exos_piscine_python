liste =[17, 38, 10, 25, 72]
liste.sort()
print(liste)
liste.append(12)
print(liste)
liste.sort(reverse=True)
print(liste)
print(liste.index(17))
liste.remove(38) 
print(liste)
print (liste[1:3])
print (liste[0:2])
print (liste[2:len(liste)])
print (liste[0:len(liste)])