'''
Ce fichier gère:
- les brique : est un sprite (image + rect) qui peut être détruite --> Actor
- leur apparence des briques (couleur, taille)

'''
# son apparition (positions dans la fenêtre) est définie et gérée par le niveau, voir dans levels.py

import pygame
from window import WINDOW_SIZE
import Actors.Actor as Actor #pour avoir accès à d'autre fichier


class Brique(Actor.Actor):

    def __init__(self, x, y, resistance=2):

        # initialise Actor :
        # x, y, largeur, hauteur, couleur
        super().__init__(
            x,
            y,
            80,
            15,
            (255, 0, 0)
        )

        # résistance
        self.resistance = resistance
        self.max_resistance = resistance

        # applique la bonne couleur selon resistance
        self.update_color()

    # Change la couleur selon la solidité restante.
    def update_color(self):
      
        # 4 teintes possibles
        colors = {
            4: (255, 0, 0),      # rouge vif (clair)
            3: (200, 0, 0),
            2: (140, 0, 0),
            1: (80, 0, 0)        # rouge foncé
        }

        # adapte selon les résistances restantes
        color_index = max(1, self.resistance)

        self.image.fill(colors[color_index])

    # gère les dégâts subis par la brique
    def hit(self):

        self.resistance -= 1

        if self.resistance <= 0:
            self.kill()  # kill()= supprime la brick de tous les Group

        else:
            self.update_color()


