''' le fichier doit définir la classe game, 
et gérer : les états du jeu ( menu,jeu,game over),
la boucle principale,
la coordination des objets,
mais il ne doit pas lancer le jeu!!!!'''
# game.py
# Gestion principale du jeu (boucle + états)

from tkinter import font # police pour les caractères, utile ?

import pygame
from window import *
from menu import Menu
from Actors.raquette import Raquette
from Actors.ball import Ball


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

        # Donnée joueur
        self.player = None   # sera créé plus tard
        self.scoreboard = None
        
        # Acteurs du jeu
        self.raquette = Raquette()
        self.ball = Ball()

        # capture la souris même hors de la fenêtre de jeu
        # pygame.event.set_grab(True)
        pygame.mouse.get_rel() # réinitialise le mouvement de la souris
        pygame.mouse.set_visible(True)
        

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
            self.raquette.update()
            self.ball.update()


            #collision raquette-balle
            if self.ball.rect.colliderect(self.raquette.rect) and self.ball.dy > 0:
                self.ball.dy *= -1

                # éviter que la balle reste collée
                self.ball.rect.bottom = self.raquette.rect.top

                # influence de la raquette sur la balle (plus la souris bouge vite, plus la balle part sur les côtés)
                dx_mouse = pygame.mouse.get_rel()[0]
                self.ball.dx = max(-15, min(15, dx_mouse))

    def draw(self):
        """
        Affichage à l'écran
        """
        self.screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

        if self.state == "menu":
            self.menu.draw(self.screen)

        elif self.state == "playing":
            font = pygame.font.SysFont(None, 50)
            text = font.render("GAME RUNNING", True, (255,255,255)) # supprimer plus tard 
            self.screen.blit(text, (100,100))

            # acteurs du jeu
            self.raquette.draw(self.screen)
            self.ball.draw(self.screen)

        pygame.display.flip()