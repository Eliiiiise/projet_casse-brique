# classe power-up -> sous-classe de Actor
# Power-up = bonus qui tombe à 50% de chance quand une brique est détruite
# les effet sont à définir selon le cahier des charges en héritant de cette classe  en définisant apply_effect() pour chacun

#mettre les 50% de chance que le power-up tombe dans brick.py, dans la méthode hit() ou dans gameco.py après la collision balle-brick
import pygame
import random
from Actors.ball import Ball
from Actors import brick
import Actors.Actor as Actor
from window import WINDOW_SIZE


class PowerUp(Actor.Actor):

    def __init__(self, x, y):
        self.color = (0,0,255) #doit être bleu 
        # x, y, largeur, hauteur,couleur
        super().__init__(x,y,10,10,self.color)
    

        # vitesse de chute
        self.dy = 8
        # type aléatoire 
        self.type =random.randint(1,7)
        # temps pour les effets
        self.start_time = None

    def update(self):

        # le power-up tombe
        self.rect.y += self.dy

        # supprime si sort de l'écran
        if self.rect.top > WINDOW_SIZE[1]:
            self.kill()


    def apply_effect(self, game):
        """
        apllique l'effet du power-up gameco
        Redéfini dans les classes filles.
        """
        current_time = pygame.time.get_ticks() # get_ticks() = gère la durée des effets

        # Type 1: agrandir la raquette 
        if self.type == 1:
            game.raquette.rect.width = 200
            #redessiner la raquette
            game.raquette.resize(200, game.raquette.rect.height, (165, 255, 223))
            game.power_end_time = current_time + 10000
            print("Power-up appliqué :", self.type)

        # Type 2: rapetissir la raquette
        elif self.type == 2:
            game.raquette.rect.width = 50
            #redessiner la raquette
            game.raquette.resize(50, game.raquette.rect.height, (255, 232, 165))
            game.power_end_time = current_time + 10000
            print("Power-up appliqué :", self.type)

        # Type 3: balle ralentie
        elif self.type == 3:
            for ball in game.balls:
                if ball.dy > 0:
                    ball.dy = 5
                else:
                    ball.dy = -5
            game.power_end_time = current_time + 5000
            print("Power-up appliqué :", self.type)

        # Type 4: balle accélérée 
        elif self.type == 4:
            for ball in game.balls:
                if ball.dy > 0:
                    ball.dy = 15
                else:
                    ball.dy = -15
            game.power_end_time = current_time + 5000
            print("Power-up appliqué :", self.type)

        # Type 5: 10 balles supplémentaires
        elif self.type == 5:
            for _ in range(10):
                new_ball = Ball()
                game.balls.add(new_ball)
                print("Power-up appliqué :", self.type)

        # Type 6: balle invisible (clignotte)
        elif self.type == 6:
            for ball in game.balls:
                ball.blinking = True # la balle clignotte
            game.power_end_time = current_time + 2000
            print("Power-up appliqué :", self.type)

        # Type 7: balles transperçantes
        elif self.type == 7:
            for ball in game.balls:
                ball.piercing = True
            game.power_end_time = current_time + 10000
            print("Power-up appliqué :", self.type)

