# menus (start,game over,next level)
# bouton, clic souris, changement d'état
import pygame
class Menu:
    def __init__(self, gameco):
        self.game = gameco

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.state = "playing"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))