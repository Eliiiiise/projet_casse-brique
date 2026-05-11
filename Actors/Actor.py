import pygame
from Actors.raquette import * 

#reprendre pour réecrire brique, ball, brick

'''
Classe mère de tous les objets du jeu.

Un Actor possède :
- une image
- une position (rect)
- une méthode draw()

Les autres classes du jeu héritent de cette classe.
'''
class Actor(pygame.sprite.Sprite):

    #Initialise l'apparence de l'objet.
    def __init__(self,x,y, width, height, color):
       
        # initialise Sprite de pygame
        super().__init__()

        # surface
        self.image = pygame.Surface((width, height))

        # couleur
        self.image.fill(color)

        # rectangle utilisé pour :
        # - la position
        # - les collisions
        self.rect= self.image.get_rect(topleft= (x,y))

    def update(self):
        pass

    def draw(self, screen):
        """
        Affiche l'objet à l'écran.
        """

        screen.blit(self.image, self.rect)
