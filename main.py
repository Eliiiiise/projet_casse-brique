# point d'entrée du jeu 
import pygame 
from window import *
from Actors.raquette import *

from gameco import Gameco

if __name__  == "__main__":
    game = Gameco()
    game.run()


'''
# initialisation de pygame 
pygame.init()
# affichage de window + init
screen: pygame.Surface = pygame.display.set_mode(WINDOW_SIZE)
is_running: bool = True
game: Game = Game() # nom : type = valeur

clock = pygame.time.Clock()
# permet d'afficher la window plus de 2 sec 
running = True
screen.fill(pygame.Color(pygame.color.THECOLORS["black"]))
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()



# main.py
# Point d'entrée du jeu Casse-Brique

from game import Game


def main():
    game = Game()   # Création du jeu
    game.run()      # Lancement de la boucle principale


# Cette condition est TRÈS importante
# Elle empêche l'exécution automatique lors des imports
if __name__ == "__main__":
    main()
'''