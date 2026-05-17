# vies
# score
# pseudos
# highscore...

"""
Gestion des données du joueur.
"""
class Player:

    def __init__(self):
        # nombre de vies restantes
        self.lives = 3

    def lose_life(self):
        self.lives -= 1


    def reset_lives(self):
        self.lives = 3