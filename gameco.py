''' le fichier doit définir la classe game, 
et gérer : les états du jeu ( menu,jeu,game over),
la boucle principale,
la coordination des objets,
mais il ne doit pas lancer le jeu!!!!'''
# clasee game par copilote:
# game.py
# Gestion principale du jeu (boucle + états)

import pygame
from window import Window
from menu import Menu


class Gameco:
    def __init__(self):
        """
        Initialisation du jeu
        """
        pygame.init()

        # Fenêtre
        self.window = Window()
        self.screen = self.window.screen

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

            if self.state == "menu":
                self.menu.handle_event(event)

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
        self.window.clear()

        if self.state == "menu":
            self.menu.draw(self.screen)

        elif self.state == "playing":
            pass  # futur : afficher la raquette, la balle, etc.

        self.window.update()