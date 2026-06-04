'''
Ce fichier gère l'écran de saisie du pseudo.
Le joueur entre son nom avant le début de la partie.
Ce pseudo sera associé à son score final et utilisé dans le classement des meilleurs scores.
'''
import pygame

class NameMenu:
    def __init__(self, game):
        self.game = game
    
     # Texte actuellement saisi par le joueur
        self.name = ""

    # polices utilisées pour l'affichage
        self.title_font = pygame.font.SysFont(None, 70)
        self.text_font = pygame.font.SysFont(None, 45)
        self.small_font = pygame.font.SysFont(None, 30)
        self.quit_font= pygame.font.SysFont(None,50)
        self.red = (255, 60, 60)

    # bouton quitter
        self.quit_rect = pygame.Rect(1200, 20, 40, 40) # position en haut a droite

    # Texte bouton X
        self.quit_text = self.quit_font.render("X", True, (255, 255, 255))
    # centreé au milieu 
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)

    def update(self):
        pass

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

            # CADRE AUTOUR DU CHAMP DE SAISIE
            # padding autour du texte (espace)
            padding = 20

            # créer un rectangle plus grand que le texte
            box_rect = pygame.Rect(
                input_rect.x - padding,
                input_rect.y - padding,
                input_rect.width + padding * 2,
                input_rect.height + padding * 2
            )

            # dessiner le contour rose
            pygame.draw.rect(
                screen,
                (255, 65, 161),
                box_rect,
                2  # épaisseur du contour
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

            # BOUTON "X" POUR QUITTER
            mouse_pos = pygame.mouse.get_pos()
            hover = self.quit_rect.collidepoint(mouse_pos)
            # Si la souris est dessus → couleur plus claire et grossissement du bouton
            if hover: # quand la souris est dessus 
                color = (150, 0, 0) 
                scale_rect = self.quit_rect.inflate(10, 10)

            else: # de base 
                color = (236, 0, 0)
                scale_rect = self.quit_rect

            # Dessine le bouton X
            if self.quit_rect.collidepoint(mouse_pos):
                rect = self.quit_rect.inflate(6, 6)
                quit_color = (120, 0, 0)
            else:
                rect = self.quit_rect
                quit_color = (70, 0, 0)

            pygame.draw.rect(screen, quit_color, self.quit_rect, border_radius=6)
            pygame.draw.rect(screen, self.red, self.quit_rect, width=2, border_radius=6)

            self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)
            screen.blit(self.quit_text, self.quit_text_rect)
            