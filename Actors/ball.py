# classe ball = sous classe de actors 
import Actors.Actor as Actor #pour avoir acces a d'autre fichier
import pygame
import random
from window import WINDOW_SIZE

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # apparence
        self.image = pygame.Surface((10, 10))
        self.image.fill((0, 255, 0))  # vert

        self.rect = self.image.get_rect()

        # position initiale
        self.rect.x = random.randint(0, int(WINDOW_SIZE[0]) - 10)
        self.rect.y = 680

        # vitesse (selon axe x et y)
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

    def draw(self, screen):
        screen.blit(self.image, self.rect)