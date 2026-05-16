# classe Raquette -> sous-classe de Actor
import pygame
from window import * #importe tout le fichier
import Actors.Actor as Actor


class Raquette(Actor.Actor):
    def __init__(self):
        # x, y, largeur, hauteur, couleur
        super().__init__(
            WINDOW_SIZE[0] // 2 - 50,
            700,
            100,
            10,
            (255, 255, 255)
        )

        # position
        self.rect = self.image.get_rect()
        self.rect.y = 700
        self.rect.centerx = WINDOW_SIZE[0] // 2

    def update(self):
        # suivre la souris
        dx = pygame.mouse.get_rel()[0]
        self.rect.x += dx
        
        # pas sortir de l'écran 
        if self.rect.left < 0: 
            self.rect.left = 0
        if self.rect.right > WINDOW_SIZE[0]:
            self.rect.right = WINDOW_SIZE[0]

        # replace le curseur au centre de la raquette
        pygame.mouse.set_pos(self.rect.centerx, self.rect.centery)
    

