''' 
Le fichier doit définir la classe game, et gérer : 
les états du jeu ( menu,jeu,game over),
la boucle principale,
la coordination des objets,
mais il ne doit pas lancer le jeu!!!!'''
# gameco.py remplace le habituel game.py 
# gameco-> dessine tout le jeu 

from tkinter import font

import pygame
import random
from Actors import ball
from window import *
from home_menu import HomeMenu
from gameover_menu import GameOverMenu
from pause_menu import PauseMenu
from Actors.raquette import Raquette
from Actors.ball import Ball
from Actors.brick import Brique
from Actors.powerup import PowerUp
from levels import LEVELS
from player import Player
from collisions import handle_collisions
from input_manager import handle_input
from level_transition import LevelTransition
from name_menu import NameMenu
from scoreboard import Scoreboard



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
        self.state = "menu"   # "menu", "playing","pause", "game_over"

        # Éléments du jeu
        self.home_menu = HomeMenu(self)
        self.gameover_menu = GameOverMenu(self)
        self.pause_menu =PauseMenu(self)
        self.level_transition = LevelTransition(self)
        self.name_menu = NameMenu(self) 

        # Donnée joueur
        self.player = Player() 
        self.scoreboard = Scoreboard()
        
        # Acteurs du jeu
        self.raquette = Raquette()

        self.bricks = pygame.sprite.Group()

        self.balls = pygame.sprite.Group()
        ball = Ball() # création de la balle
        self.balls.add(ball) # ajout de la balle au groupe

        # niveau actuel
        self.current_level = 0 #renvoi à la position dans la liste LEVELS ---> 0==1

        # cycle actuel des niveaux
        # cycle 1 = résistance normale (2)
        # cycle 2 = +1 résistance (3)
        # cycle 3 = +2 résistance (4(max))
        self.cycle = 1

        # charge le niveau
        self.load_level(self.current_level) 

        #power-up
        self.powerups =pygame.sprite.Group()    

        # timer anti-click
        self.last_state_change= pygame.time.get_ticks() # temps écoulé depuis le lancement du jeu (en ms)

    def run(self):
        '''
        Boucle principale du jeu
        '''
        print(">>>Gameco.run() est exécuté")
        while self.running:
            events = pygame.event.get() #evenement clavier/souris
            handle_input(self, events) # on renvoie au doc input
            self.update()
            self.draw()
            self.clock.tick(self.fps)

        pygame.quit()

    def update(self):
        '''
        Mise à jour de la logique du jeu
        '''
        if self.state == "menu":
            self.home_menu.update()

        elif self.state == "name_menu":
            self.name_menu.update()

        elif self.state == "playing":
            # appel d'une méthode d'un objet
            self.raquette.update()  
            self.balls.update()
            self.powerups.update()

            #appel d'une fonction externe
            handle_collisions(self) 

            # vérifier chaque balle si elle sort de l'écran (perte de balle) 
            for ball in self.balls:
                if ball.rect.top > WINDOW_SIZE[1]:
                    ball.kill()  # supprimer la balle
            if len(self.balls) == 0: # si aucune balle n'est présente
                    self.player.lose_life()

                    # GAME OVER
                    if self.player.lives <= 0:

                        # enregistre le score final
                        self.scoreboard.add_score(
                            self.player.name,
                            self.player.score
                        )

                        # passe à l'écran game over
                        self.state = "game_over"

                    else:# recréer une balle
                        new_ball = Ball()
                        self.balls.add(new_ball)

            # la gestion du temps  doit être dans la partie "playing" pour éviter que les timers avancent pendant le menu ou la pause 
            # fin des powerup temporaires => à chaque frame, on vérifie si un power-up est actif et si son timer est écoul
            current_time = pygame.time.get_ticks()

            # si un power-up est actif (on a défini un timer)
            if hasattr(self, "power_end_time"): 

                if current_time > self.power_end_time:
                        # taille normale raquette
                        self.raquette.rect.width = 100
                        
                        # recréer surface normale
                        self.raquette.resize(100, self.raquette.rect.height, (255, 255, 255))

                        # désactive effets
                        self.invisible = False
                        self.piercing = False

                        # remet les balles normales
                        for ball in self.balls:
                            ball.piercing = False
                            ball.blinking = False
                            ball.visible = True
                            ball.image.set_alpha(255)

                        #supprime le timer pour éviter de vérifier à chaque frame
                        del self.power_end_time

            """
            passage au niveau suivant si toutes les briques sont détruites
            """
            if len(self.bricks) == 0:

                        # passe au niveau suivant
                        self.current_level += 1

                        # si on dépasse le dernier niveau, on revient au niveau 1 + augmente resistance
                        if self.current_level >= len(LEVELS):
                            self.current_level = 0
                            self.cycle += 1

                        #reset des vies
                        self.player.reset_lives()

                        # charge le niveau suivant
                        self.load_level(self.current_level)

                        # supprime les anciennes balles
                        self.balls.empty()

                        # crée une nouvelle balle pour le niveau suivant
                        self.balls.add(Ball())

                        # lance l'écran de transition
                        self.state = "level_transition"

                        # mémorise le début de la transition
                        self.transition_start_time = pygame.time.get_ticks()        

        elif self.state == "level_transition":

            self.level_transition.update()

            current_time = pygame.time.get_ticks()

            if current_time - self.transition_start_time > 2000:
                self.state = "playing"
    
        elif self.state == "pause":
            self.pause_menu.update()
          
        elif self.state == "game_over":
            self.gameover_menu.update()

  

    
    def reset_game(self):
        """
        Réinitialise le jeu quand on clique Rejouer
        """
        print(">>>Gameco.reset_game() est exécuté")
        # reset joueur ---> vies + score
        self.player.reset_player()

        # retour au premier niveau
        self.current_level = 0
        self.load_level(self.current_level)

        # recrée raquette et balle/s 
        self.balls = pygame.sprite.Group()
        self.balls.add(Ball())
        self.raquette = Raquette()

        # supprime les power-ups encore présents (pas qu'ils apparaissent à la partie suivante)
        self.powerups.empty()
        if hasattr(self, "power_end_time"):
            del self.power_end_time

        # recrée briques au cycle de résistance 1
        self.load_level(self.current_level)
        self.cycle = 1

        # désactive les effets temporaires
        self.invisible = False
        self.piercing = False

         # relance la partie
        self.state = "playing"

        
        
    def draw_heart(self, screen, x, y, size=10):
        """
        Dessine un coeur pixelisé à la position (x, y)
        size = taille des pixels
        """
        color = (255, 65, 161)  # même que bouton home dans pause_menu pour une cohérence visuelle 
 
        # liste de "pixels" du coeur (forme simple)
        heart_shape = [
                  (1,0),(2,0),      (4,0),(5,0),
            (0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),
            (0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),
                  (1,3),(2,3),(3,3),(4,3),(5,3),
                        (2,4),(3,4),(4,4),
                              (3,5)
        ] # sur des axes x(->),y(descendant) avec (0,0) en haut à gauche du coeur, chaqque coordonnée correspond à un pixel de couleur du coeur 

        # dessiner chaque "pixel"
        for (dx, dy) in heart_shape:
            pygame.draw.rect(
                screen,
                color,
                (x + dx * size, y + dy * size, size, size)
            ) 

    def draw(self):
        '''
        Affichage à l'écran
        '''
        self.screen.fill((0, 0, 0))  # Remplir l'écran avec une couleur de fond

        if self.state == "menu":
            self.home_menu.draw(self.screen)

        elif self.state == "name_menu":
            self.name_menu.draw(self.screen)

        elif self.state == "playing":
            # affiche le SCORE
            font = pygame.font.SysFont(None, 40)

            score_text = font.render(
                f"Score : {self.player.score}",
                True,
                (255, 255, 255)
            )
            # place le texte à droite avec une marge de 20 px
            score_rect = score_text.get_rect(
                topright=(WINDOW_SIZE[0] - 20, 20)
            )
            self.screen.blit(score_text, score_rect)
            
            # affiche les VIES(coeurs)
            for i in range(self.player.lives):
                self.draw_heart(self.screen, 20 + i * 30, 20, size=4) # espacement entre les coeurs = 30px, taille des pixels = 4px
            
            # acteurs du jeu
            self.bricks.draw(self.screen)
            self.raquette.draw(self.screen)
            if not getattr(self, "invisible", False): # si la balle n'est pas invisible
                self.balls.draw(self.screen)
            self.powerups.draw(self.screen)
        
        elif self.state == "pause":

            # affiche le jeu figé
            self.bricks.draw(self.screen)
            self.raquette.draw(self.screen)
            self.balls.draw(self.screen)

            overlay = pygame.Surface((1280, 720)) # créer une surface de lataille de l'écran

            # on gère la transparence : 0=invisible, 255=opaque
            overlay.set_alpha(150)

            #couleur de l'effet (noir->effet sombre)
            self.screen.blit(overlay,(0,0))

            #dessine le menu pause (par dessu le jeu)
            self.pause_menu.draw(self.screen)

        elif self.state == "level_transition":
            self.level_transition.draw(self.screen)


        elif self.state == "game_over":
            self.gameover_menu.draw(self.screen)
           

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

                base_resistance = int(char)
                resistance = base_resistance + self.cycle - 1
                # ne jamais dépasser 4
                resistance = min(resistance, 4)

                x = offset_x + col_index * (brick_width + spacing_x)
                y = offset_y + row_index * (brick_height + spacing_y)

                brick = Brique(x, y, resistance)
                self.bricks.add(brick)