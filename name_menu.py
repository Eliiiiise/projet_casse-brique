"""
Ce fichier gère l'écran de saisie du pseudo.

Le joueur entre son nom avant le début de la partie.
Ce pseudo sera associé à son score final et utilisé dans
le classement des meilleurs scores.
"""

import pygame

class NameMenu:
    def __init__(self, game):
        self.game = game
    
     # texte actuellement saisi par le joueur
        self.name = ""

    # polices utilisées pour l'affichage
        self.title_font = pygame.font.SysFont(None, 70)
        self.text_font = pygame.font.SysFont(None, 45)
        self.small_font = pygame.font.SysFont(None, 30)

    def update(self):
        pass
        #mise à jour du jeu, même logique que les autres mais pas utilisé pour l'instant

    def handle_event(self, event):

        # une touche du clavier est pressée alors:
        if event.type == pygame.KEYDOWN:

            # touche ENTER : validation du pseudo
            if event.key == pygame.K_RETURN:

                # vérifie qu'un pseudo a été saisi
                if self.name.strip() != "":
                    self.game.player.name = self.name.strip()

                # pseudo par défaut si rien n'est écrit
                else:
                    self.game.player.name = "Player"

                # réinitialise la partie
                self.game.reset_game()

                # lance le jeu
                self.game.state = "playing"

                # touche supprimer
            elif event.key == pygame.K_BACKSPACE:

                 # supprime le dernier caractère
                self.name = self.name[:-1]

            # toutes les autres touches
            else:

                    # limite la longueur du pseudo
                    if len(self.name) < 20:

                        # ajoute le caractère saisi
                        self.name += event.unicode

    def draw(self, screen):
            """
            Affiche le menu de saisie du pseudo.
            """

            # couleur de fond (noir)
            screen.fill((0, 0, 0))

            # TITRE
            title = self.title_font.render(
                "ENTRER UN PSEUDO",
                True,
                (255, 255, 255) # blanc
            )
            # rectangle du titre centré milieu horizontal
            title_rect = title.get_rect(
                center=(640, 200)
            )

            screen.blit(title, title_rect)

            # CHAMP DE SAISIE
            # curseur visuel représenté par |
            input_text = self.text_font.render(
                self.name + "|", # affiche le curseur 
                True,
                (255, 255, 255)
            )

            input_rect = input_text.get_rect(
                center=(640, 330)
            )

            screen.blit(input_text, input_rect)

            # INSTRUCTIONS
            info = self.small_font.render(
                "Appuie sur ENTER pour commencer",
                True,
                (180, 180, 180)
            )

            info_rect = info.get_rect(
                center=(640, 420)
            )

            screen.blit(info, info_rect)
            