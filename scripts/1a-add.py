#!/usr/bin/env python3

# description: Demander deux nombres à l’utilisateur,afficher le résultat de l’addition.
# date: 15/10/2018
# auteur : Damien Pommier

def AfficheSomme(a,d):  #definie deux parametres 
	print (a+d)

		try: 
			i=int(input("Veuillez entrez deux nombres entiers : \na = ") )
			j=int(input("d = ") )
		except : #En cas de nombre non entier saisie ce message d'erreur s'affiche
			print("La variable nombre ne contient pas un chiffre entier")

print(" a + d = ") #affiche la somme des deux nombres saisies
AfficheSomme(i,j) #affiche les nombres saisies
