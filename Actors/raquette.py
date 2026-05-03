# classe Raquette -> sous-classe de Actor
import pygame
from window import * #importe tout le fichier

class Raquette(pygame.sprite.Sprite): #classe spéciale de Pygame pour gérer les objets du jeu ---> facilite les collisions plus tard
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

        # pas sortir de l'écran 
        if self.rect.left < 0: 
            self.rect.left = 0
        if self.rect.right > WINDOW_SIZE[0]:
            self.rect.right = WINDOW_SIZE[0]
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
