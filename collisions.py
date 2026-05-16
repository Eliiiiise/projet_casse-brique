'''
import pygame
from Actors.raquette import Raquette
from Actors.ball import Ball
from Actors.brick import Brique

#collision raquette-balle
if self.ball.rect.colliderect(self.raquette.rect) and self.ball.dy > 0:
    self.ball.dy *= -1 # on inverse la direction 

    # éviter que la balle reste collée
    self.ball.rect.bottom = self.raquette.rect.top

    # influence de la raquette sur la balle (plus la souris bouge vite, plus la balle part sur les côtés)
    dx_mouse = pygame.mouse.get_rel()[0]
    if dx_mouse != 0:
        self.ball.dx = max(-15, min(15, dx_mouse))

#collision balle-brique
for brick in self.bricks:
    if self.ball.rect.colliderect(brick.rect):
        self.ball.dy *=-1
        brick.hit() #brique touchée
        break #on sort de la boucle pour éviter pls collisions dans la même frame

#collision raquette-powerup
if self.ball.rect.colliderect(brick.rect): 
    self.ball.dy *=-1
    brick.hit()
    # si la brique est cassée -> chance de power-up
    if not brick.alive(): 
        import random
        if random.random() <0.5: #50%
            #position du centre de la brique
            x = brick.rect.centerx
            y= brick.rect.centery

            powerups= PowerUp(x,y)
            self.powerups.add(powerups)
    #break 
'''