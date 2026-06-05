'''
Ce module gère l'écran de transition entre les niveaux du jeu de casse-brique. 
Lorsqu'un joueur termine un niveau, cet écran s'affiche pour indiquer le niveau suivant, 
le cycle actuel et le score du joueur. 
Un voile noir transparent recouvre l'écran pour mettre en évidence les informations affichées. 
Après une courte pause de 2 secondes, le jeu reprend avec le niveau suivant.
'''
import pygame
from window import WINDOW_SIZE


class LevelTransition:

    def __init__(self, game):
        self.game = game
        self.font = pygame.font.SysFont(None, 50)
        self.title_font = pygame.font.SysFont(None, 90)

    def update(self):
        pass

    def draw(self, screen):
        '''
        affichage de l'écran de transition entre les niveaux
        '''
        # affiche le niveau déjà chargé
        self.game.bricks.draw(screen)
        self.game.raquette.draw(screen)

        # voile noir transparent
        overlay = pygame.Surface(WINDOW_SIZE)
        overlay.set_alpha(160)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        # texte du niveau
        font = self.title_font

        level_text = self.title_font.render(
            f"Niveau {self.game.current_level + 1}",
            True,
            (255, 255, 255)
        )

        level_rect = level_text.get_rect(
            center=(WINDOW_SIZE[0] // 2,
                    WINDOW_SIZE[1] // 2)
        )

        screen.blit(level_text, level_rect)

        # texte du cycle
        cycle_text = self.font.render(
            f"Cycle {self.game.cycle}",
            True,
            (180, 180, 180)
        )
        
        cycle_rect = cycle_text.get_rect(center=(640, 430))
        screen.blit(cycle_text, cycle_rect)

        # texte du score
        score_text = self.font.render(
            f"Score : {self.game.player.score}",
            True,
            (180, 180, 180)
        )
       
        score_rect = score_text.get_rect(center=(640, 480))
        screen.blit(score_text, score_rect)

        # les vies ne sont pas afficher ici car à chaque changement de niveau les vies sont réinitialisées (à 3)