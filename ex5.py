pSeuil=2.3
vSeuil=7.41
print("Saisir pression")
p=float(input())
print("Saisir volume")
v=float(input())
if p>pSeuil and v>vSeuil:
	print('arrêt immediat')
elif p>pSeuil and v<vSeuil:
	print('augmentez le volume de l\'enceinte')
elif p<pSeuil and v>vSeuil:
	print('diminuez le volume de l\'enceinte')
else:
	print('tout va bien')
