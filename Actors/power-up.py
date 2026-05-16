# classe power-up -> sous-classe de Actor
# Powe-up = bonus qui tombe à 50% de chance quand une brique est détruite
# les effet sont à définir selon le cahier des charges en héritant de cette classe  en définisant apply_effect() pour chacun

#mettre les 50% de chance que le powerup tombe dans brick.py, dans la méthode hit() ou dans gameco.py après la collision balle-brick

import random
from Actors import brick
import Actors.Actor as Actor
from window import WINDOW_SIZE


class PowerUp(Actor.Actor):

    def __init__(self, x, y, color):

        # x, y, largeur, hauteur, couleur
        super().__init__(
            brick.rect.centerx,
            brick.rect.centery,
            10,
            10,
            (0,0,255) # bleu
        )

        # vitesse de chute
        self.dy = 8


    def update(self):

        # le power-up tombe
        self.rect.y += self.dy

        # supprime si sort de l'écran
        if self.rect.top > WINDOW_SIZE[1]:
            self.kill()


    def apply_effect(self, game):
        """
        Effet du power-up.
        Redéfini dans les classes filles.
        """
        pass