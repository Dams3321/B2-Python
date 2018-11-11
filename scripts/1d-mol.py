#!/usr/bin/env python3

# description: jeu du plus ou moins améliorer
# date: 15/10/2018
# auteur : Damien Pommier


import signal

#Variables

win = False
value_min = 0
value_max = 100
random = random.randint(value_min, value_max)
user_input = ''


#Le resultat

def display_result(result = None):
  if result is None:
    print('Tu n\'es pas alle au bout :/')
  else :
    print('Bravo ! Tu as trouve, il s\'agit du nombre: '+str(result))

def exit_game(sig, frame):
  print('\nBye! ;)')
  exit()


#Le script

#Si l'utilisateur appuie sur CTRL + C

signal.signal(signal.SIGINT, exit_game)

#Tant que l'utilisateur n'a pas trouvé le nombre aléatoire

while win == False :
  user_input = input('Entre un nombre compris entre '+str(min_value)+' et '+str(max_value)+' : ')
  if user_input == 'q':
    break
  if int(user_input) > random:
    print('Ta proposition est trop grande !')
  elif int(user_input) < random:
    print('Ta proposition est trop petite !')
  else:
    win = True

if win == True:
  display_result(random)
else:
  display_result()
