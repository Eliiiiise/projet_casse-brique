''' le fichier doit définir la classe game, 
et gérer : les états du jeu ( menu,jeu,game over),
la boucle principale,
la coordination des objets,
mais il ne doit pas lancer le jeu!!!!'''
# gameco.py remplace le habituel game.py 
# Gestion principale du jeu (boucle + états)

#from tkinter import font # police pour les caractères, utile ?

import pygame
from window import *
from menu import Menu
from Actors.raquette import Raquette
from Actors.ball import Ball
from Actors.brick import Brique
from Actors.powerup import PowerUp
from levels import LEVELS
from player import Player
import collisions
import random


class Gameco:
    def __init__(self):
        """
        Initialisation du jeu
        """
        pygame.init()

        # Fenêtre
        self.screen = pygame.display.set_mode((int(WINDOW_SIZE.x), int(WINDOW_SIZE.y)))
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
        self.player = Player() 
        self.scoreboard = None
        
        # Acteurs du jeu
        self.raquette = Raquette()
        self.ball = Ball()

        self.bricks = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        ball = Ball() # création de la balle
        self.balls.add(ball) # ajout de la balle au groupe

        # niveau actuel
        self.current_level = 0 #renvoi à la position dans la liste LEVELS ---> 0==1

        # charge le niveau
        self.load_level(self.current_level)   

        #power-up
        self.powerups =pygame.sprite.Group()               

    def run(self):
        '''
        Boucle principale du jeu
        '''
        print(">>>Gameco.run() est exécuté")
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()

    def handle_events(self):
        '''
        Gestion des événements (clavier, souris, fermeture)
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # si on clique sur la croix de la fenêtre
                self.running = False

             # gestion des touches du clavier
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE: # ESC = quitter complètement le programme
                    self.running = False 

                elif self.state == "playing":
                    if event.key == pygame.K_p: # P = mettre le jeu en pause
                        self.state = "pause"
                    elif event.key == pygame.K_m:# M = retour menu principal
                        self.state = "menu" 

                elif self.state == "pause":
                    if event.key == pygame.K_p: # P = reprendre la partie
                        self.state = "playing"
                    elif event.key == pygame.K_m: # M = retour menu principal
                        self.state = "menu"

    def update(self):
        '''
        Mise à jour de la logique du jeu
        '''
        if self.state == "menu":
            self.menu.update()

        elif self.state == "playing":
            self.raquette.update()
            self.ball.update()
            self.powerups.update()

             # si la balle tombe sous l'écran
            if self.ball.rect.top > WINDOW_SIZE[1]:

                self.player.lose_life() # le joueur perd une vie

                # GAME OVER
                if self.player.lives <= 0:
                    self.state = "game_over"

                # recrée une balle
                else:

                    self.ball = Ball()

            #collision raquette-balle
            if self.ball.rect.colliderect(self.raquette.rect) and self.ball.dy > 0:
                self.ball.dy *= -1 # on inverse la direction 

                # éviter que la balle reste collée
                self.ball.rect.bottom = self.raquette.rect.top

                # influence de la raquette sur la balle (plus la souris bouge vite, plus la balle part sur les côtés)
                dx_mouse = pygame.mouse.get_rel()[0]
                if dx_mouse != 0:
                    self.ball.dx = max(-15, min(15, dx_mouse))

            # collision balle-brique
            for brick in self.bricks:

                # collision détectée
                if self.ball.rect.colliderect(brick.rect):

                    # inverse la direction verticale --> rebond
                    self.ball.dy *= -1

                     #sort la balle de la brique sinon plusieurs collisions se produisent
                    if self.ball.dy > 0:
                        self.ball.rect.top = brick.rect.bottom

                    else:
                        self.ball.rect.bottom = brick.rect.top

                    # la brique subit des dégâts
                    brick.hit()

                    # si la brique est détruite --> chance de power-up
                    if not brick.alive():

                    # 50% de chance de créer un power-up
                        if random.random() < 0.5:

                            # céation du powerup au centre de la brique
                            x = brick.rect.centerx
                            y = brick.rect.centery
                            powerup = PowerUp(x, y)

                            # ajout au groupe
                            self.powerups.add(powerup)


                    # évite plusieurs collisions dans la même frame
                    break
            
            # collision raquette-powerup
            for powerup in self.powerups:

                if self.raquette.rect.colliderect(powerup.rect):

                    # applique l'effet
                    powerup.apply_effect(self)

                    # supprime le power-up
                    powerup.kill()

            # fin des powerup temporaires
            current_time = pygame.time.get_ticks()

            if hasattr(self, "power_end_time"):

                if current_time > self.power_end_time:

                    # taille normale raquette
                    self.raquette.rect.width = 100

                    # désactive effets
                    self.invisible = False
                    self.piercing = False

            #ici la souris se bloque a la raquette lors du jeu mais en dehors(menu/pause) elle est elle même
            pygame.mouse.set_visible(False)# Cache la souris
            pygame.event.set_grab(True)# Capture la souris dans la fenêtre
        else:
            pygame.mouse.set_visible(True) # Affiche la souris
            pygame.event.set_grab(False) # Libère la souris


                
    def draw(self):
        '''
        Affichage à l'écran
        '''
        self.screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

        if self.state == "menu":
            self.menu.draw(self.screen)

        elif self.state == "playing":
            """
            font = pygame.font.SysFont(None, 50)
            text = font.render("GAME RUNNING", True, (255,255,255)) # supprimer plus tard 
            self.screen.blit(text, (100,100))
            """
            # acteurs du jeu
            self.bricks.draw(self.screen)
            self.raquette.draw(self.screen)
            if not getattr(self, "invisible", False): # si la balle n'est pas invisible
                self.ball.draw(self.screen)
            self.powerups.draw(self.screen)
        
        elif self.state == "pause":

            # affiche le jeu figé
            self.bricks.draw(self.screen)
            self.raquette.draw(self.screen)
            self.ball.draw(self.screen)

            # texte pause
            font = pygame.font.SysFont(None, 80)

            text = font.render("PAUSE", True, (255,255,255))

            self.screen.blit(text, (450,350))
           

        pygame.display.flip()
    
    def load_level(self, level_index):
        '''
        Charge un niveau à partir de LEVELS
        '''
        self.bricks.empty()  # vide les anciennes briques

        layout = LEVELS[level_index]

        brick_width = 80
        brick_height = 15
        offset_x = 50   # marge à gauche
        offset_y = 50   # marge en haut
        spacing_x = 5
        spacing_y = 5

        # lit nos dessins dans levels.py
        for row_index, row in enumerate(layout):
            for col_index, char in enumerate(row):

                if char == ".":
                    continue  # trou

                resistance = int(char)

                x = offset_x + col_index * (brick_width + spacing_x)
                y = offset_y + row_index * (brick_height + spacing_y)

                brick = Brique(x, y, resistance)
                self.bricks.add(brick)