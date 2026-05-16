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
        
        mouse_x, _ = pygame.mouse.get_pos()

        # On centre la raquette sur la souris
        self.rect.centerx = mouse_x

        # Empêcher de sortir de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_SIZE[0]:
            self.rect.right = WINDOW_SIZE[0]
