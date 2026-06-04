'''
Ce fichier gère les données du joueur.

Il stocke les informations propres à une partie :
- le pseudo du joueur ;
- le nombre de vies restantes ;
- le score actuel.

La classe Player fournit également des méthodes permettant
de modifier ces données (ajouter des points, perdre une vie,
réinitialiser une partie, etc.).
'''

class Player:

    def __init__(self):

        # pseudo du joueur
        self.name = "Player"

        # nombre de vies restantes
        self.lives = 3

        # score actuel
        self.score = 0

    def lose_life(self):
        self.lives -= 1


    def reset_lives(self):
        self.lives = 3

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def reset_player(self):
        self.reset_lives()
        self.reset_score()