fichier = open("AverageOfAllGrades.txt", "r")

moyennes = []

for line in fichier:
	listOfWords = line.split()
	for num in listOfWords:
		num = num.replace(",",".")
		if listOfWords[1]!="Examen":
			if num==listOfWords[len(listOfWords)-1]:
				if num != "Absent":
					moyennes.append(float(num))

print(moyennes)

somme = sum(moyennes)
longueur = len(moyennes)

laMoyenne = somme/longueur
print("\nLa moyenne de la promo est de : " + str(round(laMoyenne,2)) + " sur 40.")

fichier.close()
exit(1)
			

