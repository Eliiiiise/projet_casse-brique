# point d'entrée du jeu 
import pygame 
from window import *
from Actors.raquette import *
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
