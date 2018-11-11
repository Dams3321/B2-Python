#!/usr/bin/env python3

# description: jeu du plus ou moins améliorer
# date: 15/10/2018
# auteur : Damien Pommier


import signal

#Variables

winn = False
value_min = 0
value_max = 100
aleat = random.randint(value_min, value_max)
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

while winn == False :
  user_input = input('Entre un nombre compris entre '+str(value_min)+' et '+str(value_max)+' : ')
  if user_input == 'q':
    break
  if int(user_input) > aleat:
    print('Ta proposition est trop grande !')
  elif int(user_input) < aleat:
    print('Ta proposition est trop petite !')
  else:
    winn = True

if winn == True:
  display_result(aleat)
else:
  display_result()
