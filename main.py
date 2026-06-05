'''
Ce fichier est le point d'entrée du jeu de casse-brique.
Il initialise le jeu et lance la boucle principale du jeu.
'''

import pygame 
from window import *
from Actors.raquette import *

from gameco import Gameco

if __name__  == "__main__":
    game = Gameco()
    game.run()
