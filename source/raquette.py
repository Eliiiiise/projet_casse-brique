import pygame
from window import * #importe tout le fichier
from game import Game

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

    