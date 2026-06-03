# affiche un écran de transition entre les niveaux
# affiche le niveau en cours et un voile noir transparent
# après 2 secondes, le jeu reprend


import pygame
from window import WINDOW_SIZE


class LevelTransition:

    def __init__(self, game):
        self.game = game


    def update(self):
        pass


    def draw(self, screen):

        # affiche le niveau déjà chargé
        self.game.bricks.draw(screen)
        self.game.raquette.draw(screen)

        # voile noir transparent
        overlay = pygame.Surface(WINDOW_SIZE)
        overlay.set_alpha(160)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # texte du niveau
        font = pygame.font.SysFont(None, 90)

        level_text = font.render(
            f"Niveau {self.game.current_level + 1}",
            True,
            (255, 255, 255)
        )

        level_rect = level_text.get_rect(
            center=(WINDOW_SIZE[0] // 2,
                    WINDOW_SIZE[1] // 2)
        )

        screen.blit(level_text, level_rect)