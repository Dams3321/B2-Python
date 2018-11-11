#!/usr/bin/env python3

# description: Jeu du plus ou moins qui lit dans un fichier.
# date: 28/10/2018
# auteur : Damien Pommier


import signal 
import random

file_chemin =  " plusoumoins.txt "
winn =  faux
value_min =  0
value_max =  100
aleat = random.randint (value_min, value_max)
user_input =  ' '

#Fonctions

 def Message():
 fichier = open('./message.txt', 'w')
 fichier.write(Bonjour)
 fichier.close()
    
 def Nombre():
 fichier = open('./message.txt', 'r')
 return fichier.read()
 fichier.close()
    
 def PPetit():
 fichier = open('./message.txt', 'w')
 fichier.write(PetitMess)
 fichier.close()


 def PGrand():
 fichier = open('./message.txt', 'w')
 fichier.write(GrandMess)
 fichier.close()


 def LaVictoire():
 fichier = open('./message.txt', 'w')
 fichier.write(LVictMess)
 fichier.close()


 def byebye():
 print('\nLa solution est ' + str(aleat))
 print('Byebye !')

#Scripts 

 while True:
 
    key = number()
    
  try:
  
     key = int(key)
     if key == aleat:
         LaVictoire()
         
  break
  
       elif key > aleat:
         PPetit()
         time.sleep(1)
   else:
   
         PGrand()
         time.sleep(3)
         
  except ValueError:
  
       time.sleep(3)   
    
    
