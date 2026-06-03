import pygame
import random
from Actors.powerup import PowerUp


def handle_collisions(game):
    
    #collision raquette-balle
    for ball in game.balls:
        if ball.rect.colliderect(game.raquette.rect) and ball.dy > 0:
            # on inverse la direction 
            ball.dy *= -1 

            # éviter que la balle reste collée
            ball.rect.bottom = game.raquette.rect.top

            # influence de la raquette sur la balle (plus la souris bouge vite, plus la balle part sur les côtés)
            dx_mouse = pygame.mouse.get_rel()[0]
           
           #limite l'influence de la souris pour éviter des vitesses extrêmes
            dx_mouse = max(-15, min(15, dx_mouse))

            if dx_mouse != 0:
                ball.dx = dx_mouse
            else:
                ball.dx = max(-10, min(10, ball.dx))
    

    #collision balle-brique
    for ball in game.balls:
        for brick in game.bricks:
        
                # collision détectée
                if ball.rect.colliderect(brick.rect):

                    if not ball.piercing:
                    # inverse la direction verticale --> rebond
                        ball.dy *= -1

                     #sort la balle de la brique sinon plusieurs collisions se produisent
                    if ball.dy > 0:
                        ball.rect.top = brick.rect.bottom

                    else:
                        ball.rect.bottom = brick.rect.top

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
                            game.powerups.add(powerup)

                    # évite plusieurs collisions dans la même frame
                    break

    # collision raquette-powerup
    for powerup in game.powerups:
        if game.raquette.rect.colliderect(powerup.rect):
                
                # applique l'effet 
                powerup.apply_effect(game)

                # supprime le power-up
                powerup.kill()