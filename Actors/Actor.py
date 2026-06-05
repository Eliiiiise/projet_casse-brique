'''
Classe mère de tous les objets du jeu.

Un Actor possède :
- une image
- une position (rect)
- une méthode draw() pour s'afficher à l'écran

Les autres classes du jeu héritent de cette classe.
'''

from turtle import color

import pygame
from Actors.raquette import * 

class Actor(pygame.sprite.Sprite): #classe spéciale de Pygame pour gérer les objets du jeu ---> facilite les collisions plus tard

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

    def set_color(self, color):
        '''
        Change la couleur de l'objet en redessinant sa surface
        '''
        self.image.fill(color)

    def resize(self, width, height, color):
        """
        Redimensionne l'objet et met à jour son image + couleur
        """

        # garder le centre AVANT modification
        center = self.rect.center

        # nouvelle image
        self.image = pygame.Surface((width, height))

        # couleur
        self.image.fill(color)

        # nouveau rect basé sur la nouvelle image
        self.rect = self.image.get_rect()

        # remettre l'objet au bon endroit
        self.rect.center = center

    def update(self):
        pass

    def draw(self, screen):
     
        screen.blit(self.image, self.rect)
