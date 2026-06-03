# classe ball = sous classe de actors 
import Actors.Actor as Actor #pour avoir acces a d'autre fichier
import pygame
import random
from window import WINDOW_SIZE

class Ball(Actor.Actor):
    def __init__(self):
        self.size =10 
        x = random.randint(0, int(WINDOW_SIZE[0]) - self.size)
        y = 680
       
        super().__init__(x,y,self.size,self.size,(0,255,0))  # x, y, largeur, hauteur, couleur
        
    
        # remplace carrée par un autre transparent
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)

        # dessin cercle
        pygame.draw.circle(
            self.image,
            (0, 255, 0),
            (self.size // 2, self.size // 2),  # centre du cercle
            self.size // 2  # rayon
        )

        # vitesse
        self.dx = random.randint(-15, 15)
        self.dy = -10 # en pygame y aug vers le bas et diminue vers le haut
        self.piercing = False # la balle n'est pas transperçante au départ

        # balle visible par défaut
        self.blinking = False

        # utilisé pour faire clignoter
        self.visible = True

        # timer du clignotement
        self.last_blink = 0     

    def update(self):
        # déplacement
        self.rect.x += self.dx
        self.rect.y += self.dy

        # rebond murs
        if self.rect.left <= 0 or self.rect.right >= WINDOW_SIZE[0]:
            self.dx *= -1

        # rebond plafond
        if self.rect.top <= 0:
            self.dy *= -1

        # balle perdue
        if self.rect.bottom >= WINDOW_SIZE[1]:
            self.kill()  # supprime la balle

        # limite la vitesse horizontale
        self.dx = max(-15, min(15, self.dx))

        # limite aussi dy pour éviter les vitesses folles
        if self.dy > 0:
            self.dy = min(self.dy, 15)
        else:
            self.dy = max(self.dy, -15)

        # Effet clignotement
        if self.blinking:

            current_time = pygame.time.get_ticks()

            # change visibilité toutes les 150 ms
            if current_time - self.last_blink > 150:

                self.visible = not self.visible
                 
                if self.visible:
                    self.image.set_alpha(255)
                else:
                    self.image.set_alpha(40)

                self.last_blink = current_time