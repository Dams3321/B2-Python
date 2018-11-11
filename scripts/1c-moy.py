#!/usr/bin/env python3
#Damien
#Créer le 15/10/18

 coef = 0
 compteur = 0
 index = 0 

 list = input("Entrez le nombre de notes --> ")
 list = int(list)
 while(compteur<list) :
 	try:
 		calc = input("Entrez la note :")
 	except :
 		print("Erreur, la note est négative")
 	
 	calc = int(calc)
 	print ("Vous avez rentrer %d "%calc)
 	index = index + calc
 	compteur += 1 

coef = list
coef = int(coef)
index = int(index)
index = index / coef
print("Votre moyenne est de --> %d"%index)
input("Veuillez appuyer sur Q pour stopper la saisie...")