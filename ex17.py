v = "232"
if len(v) < 1:
	print("pas un palindrome car taille < 1")
else:
    if v == v[::-1]:
        print("palindrome")
    else:
    	print("pas palindrome car inverse pas identique")
