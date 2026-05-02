''' le fichier doit définir la classe game, 
et gérer : les états du jeu ( menu,jeu,game over),
la boucle principale,
la coordination des objets,
mais il ne doit pas lancer le jeu!!!!'''
# clasee game par copilote:
# game.py
# Gestion principale du jeu (boucle + états)

from tkinter import font

import pygame
from window import *
from menu import Menu


class Gameco:
    def __init__(self):
        """
        Initialisation du jeu
        """
        pygame.init()

        # Fenêtre
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

        # Horloge (FPS)
        self.clock = pygame.time.Clock()
        self.fps = 60

        # État du jeu
        self.running = True
        self.state = "menu"   # "menu", "playing", "game_over"

        # Éléments du jeu
        self.menu = Menu(self)
        self.player = None   # sera créé plus tard
        self.scoreboard = None

    def run(self):
        """
        Boucle principale du jeu
        """
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()

    def handle_events(self):
        """
        Gestion des événements (clavier, souris, fermeture)
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif self.state == "menu":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.state = "playing"

            elif self.state == "playing":
                pass  # futur : player.handle_event(event)

    def update(self):
        """
        Mise à jour de la logique du jeu
        """
        if self.state == "menu":
            self.menu.update()

        elif self.state == "playing":
            pass  # futur : mise à jour du jeu

    def draw(self):
        """
        Affichage à l'écran
        """
        self.screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

        if self.state == "menu":
            self.menu.draw(self.screen)

        elif self.state == "playing":
            font = pygame.font.SysFont(None, 50)
            text = font.render("GAME RUNNING", True, (255,255,255))
            self.screen.blit(text, (100,100))

        pygame.display.flip()