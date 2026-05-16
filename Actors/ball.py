# classe ball = sous classe de actors 
import Actors.Actor as Actor #pour avoir acces a d'autre fichier
import pygame
import random
from window import WINDOW_SIZE

class Ball(Actor.Actor):
    def __init__(self):

        # x, y, largeur, hauteur, couleur
        super().__init__(
            random.randint(0, int(WINDOW_SIZE[0]) - 10),
            680,
            10,
            10,
            (0, 255, 0)
        )

        # vitesse
        self.dx = random.randint(-15, 15)
        self.dy = -10
        

    def update(self):
        # déplacement
        self.rect.x += self.dx
        self.rect.y += self.dy

        # rebond murs
        if self.rect.left <= 0 or self.rect.right >= WINDOW_SIZE[0]:
            self.dx *= -1

        # rebond plafond
        if self.rect.top <= 0:
            self.dy *= -1

        # balle perdue
        if self.rect.bottom >= WINDOW_SIZE[1]:
            self.kill()  # supprime la balle
