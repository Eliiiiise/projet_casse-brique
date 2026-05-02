# classe raquette -> sous-classe de Actor
import pygame
from window import * #importe tout le fichier
from game import Game # du fichier game importe la classe Game 

class raquette :
    __raquette: raquette
    __color: pygame.color
    __rect: pygame.rect

    def __init__(self, raquette:raquette,color)->None:
        self.__raquette = raquette
        self.__color = color
        self.__rect = pygame.rect(self.__raquette.position, self.__raquette.size)

    def draw(self, surface= WINDOW_SIZE)->None:
        pygame.draw.rect(surface,pygame.color.Color["white"],((600,700),(100,10)))

    

class Raquette(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # image (rectangle blanc)
        self.image = pygame.Surface((100, 10))
        self.image.fill((255, 255, 255))

        # position
        self.rect = self.image.get_rect()
        self.rect.y = 700
        self.rect.centerx = WINDOW_SIZE[0] // 2

    def update(self):
        # suivre la souris
        mouse_x = pygame.mouse.get_pos()[0]
        self.rect.centerx = mouse_x

        # bloquer dans l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_SIZE[0]:
            self.rect.right = WINDOW_SIZE[0]