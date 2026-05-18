import pygame
import random
from Actors.powerup import PowerUp


def handle_collisions(game):
    
    #collision raquette-balle
    if game.ball.rect.colliderect(game.raquette.rect) and game.ball.dy > 0:
        game.ball.dy *= -1 # on inverse la direction 

        # éviter que la balle reste collée
        game.ball.rect.bottom = game.raquette.rect.top

        # influence de la raquette sur la balle (plus la souris bouge vite, plus la balle part sur les côtés)
        dx_mouse = pygame.mouse.get_rel()[0]
        if dx_mouse != 0:
            game.ball.dx = max(-15, min(15, dx_mouse))

    #collision balle-brique
    for brick in game.bricks:
        
                # collision détectée
                if game.ball.rect.colliderect(brick.rect):

                    # inverse la direction verticale --> rebond
                    game.ball.dy *= -1

                     #sort la balle de la brique sinon plusieurs collisions se produisent
                    if game.ball.dy > 0:
                        game.ball.rect.top = brick.rect.bottom

                    else:
                        game.ball.rect.bottom = brick.rect.top

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

                # fin des powerup temporaires
                current_time = pygame.time.get_ticks()

                if hasattr(game, "power_end_time"):

                    if current_time > game.power_end_time:

                         # taille normale raquette
                        game.raquette.rect.width = 100

                        # désactive effets
                        game.invisible = False
                        game.piercing = False
