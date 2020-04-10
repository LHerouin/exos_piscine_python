print('saisir entier entre 1 et 10')
x=input()

try:
	val = int(x)
	if val>0 and val<10:
		print('ok')

except ValueError:
	print('error')