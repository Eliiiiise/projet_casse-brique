#permet d'accéder au score, niveau, changer d'état
# bouton X arrête la boucle while self.running donc le jeu se ferme propre

import pygame

class GameOverMenu:
    def __init__(self, game):
        
        self.game = game

        #police du texte
        self.title_font= pygame.font.SysFont(None,80) #titre
        self.button_font= pygame.font.SysFont(None,50)#bouton rejouer
        self.quit_font= pygame.font.SysFont(None,50)#bouton rejouer
        self.text_font = pygame.font.SysFont(None, 40) #texte
        self.small_font = pygame.font.SysFont(None, 25,italic=True) #crédit en italique

        #boutons
        self.button_rect =pygame.Rect(540,560,200,55)
        self.quit_rect = pygame.Rect(1200, 20, 50, 50) # position en haut a droite

        # couleurs
        self.bg_color = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (160, 160, 160)
        self.dark_grey = (45, 45, 45)
        self.light_grey = (100, 100, 100)
        self.red = (255, 60, 60)

        # Texte titre
        self.title = self.title_font.render(
            "GAME OVER :",
            True,              
            (255,0,0)     
        )
        ''' a supprimer plus tard, remplacé par du texte dynamique dans draw()
        # texte score 
        self.score_text = self.text_font.render(
            "Score : ",
            True,
            (118,255,97)  
        )
        # texte level
        self.level_text = self.text_font.render(
            "Niveau : ",
            True,
            (118,255,97)  
        )
        '''
        # texte crédits
        self.credit = self.small_font.render(
            "Made by Estiiiiiii & Eliiiiise",
            True,
            (153,204,255)
        )
        # texte bouton
        self.button_text = self.button_font.render("Rejouer", True, (255, 255, 255))

        # texte bouton X
        self.quit_text = self.quit_font.render("X", True, (255, 255, 255))

    # Position du texte 
        centre_x=1280//2 #centre ecran
        centre_y=720//2 # centre ecran
        self.title_rect = self.title.get_rect(
            center=(centre_x, 200)   #centré haut
        )

        #centré au milieu (espacé vertical)
        #self.score_rect = pygame.Rect(0, 0, 0, 0) # Initialisation vide, sera mis à jour dans draw() pour être centré dynamiquement
        #self.score_rect.center = (centre_x, 380)
        self.level_rect = pygame.Rect(0, 0, 0, 0) # Initialisation vide, sera mis à jour dans draw() pour être centré dynamiquement
        self.level_rect.center = (centre_x, 430)
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)
       
        #texte en bas a droite 
        self.credit_rect = self.credit.get_rect(bottomright=(1250, 700))

    def update(self): 
            '''
            Méthode appelée à chaque frame (utile plus tard pour animations)
            '''
            pass

    def handle_event(self, event): # a déplacer dans imput_manager
            ''' 
            Gère les clics souris dans le menu
            '''
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # vérifier que le clic est sur le bouton
                if self.button_rect.collidepoint(pygame.mouse.get_pos()):
                
                    # changer l’état du jeu
                    self.game.reset_game()
                    self.game.state = "playing"


            if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 
                # si la souris est sur la croix
                 if self.quit_rect.collidepoint(mouse_pos):
                    # quitter le jeu
                    self.game.running = False

            
    def draw(self, screen): #affichage du menu 
        #couleur de fond (noir)
        screen.fill((0, 0, 0))

        #TITRE GAME OVER
        title_text = self.title_font.render(
            "GAME OVER",
            True,
            self.red
        )

        title_rect = title_text.get_rect(center=(640, 90))
        screen.blit(title_text, title_rect)

        # RECAP DE LA PARTIE
        recap_title = self.text_font.render(
            "RÉCAPITULATIF",
            True,
            self.white
        )

        recap_title_rect = recap_title.get_rect(center=(640, 180))
        screen.blit(recap_title, recap_title_rect)

        pseudo_text = self.text_font.render(
            f"Joueur : {self.game.player.name}",
            True,
            self.grey
        )

        score_text = self.text_font.render(
            f"Score final : {self.game.player.score}",
            True,
            self.grey
        )

        level_text = self.text_font.render(
            f"Niveau atteint : {self.game.current_level + 1}",
            True,
            self.grey
        )

        screen.blit(pseudo_text, pseudo_text.get_rect(center=(640, 230)))
        screen.blit(score_text, score_text.get_rect(center=(640, 275)))
        screen.blit(level_text, level_text.get_rect(center=(640, 320)))

        # AFFICHAGE 3 MEILLEURS SCORES
        top_title = self.text_font.render(
            "TOP 3",
            True,
            self.white
        )

        top_title_rect = top_title.get_rect(center=(640, 380))
        screen.blit(top_title, top_title_rect)

        top_scores = self.game.scoreboard.get_top_scores()

        if len(top_scores) == 0:
            empty_text = self.text_font.render(
                "Aucun score enregistré",
                True,
                self.grey
            )
            screen.blit(empty_text, empty_text.get_rect(center=(640, 430)))

        else:
            for index, score_data in enumerate(top_scores):

                line = self.text_font.render(
                    f"{index + 1}. {score_data['name']} - {score_data['score']}",
                    True,
                    self.grey
                )

                line_rect = line.get_rect(center=(640, 430 + index * 40))
                screen.blit(line, line_rect)

        #BOUTON REJOUER
        mouse_pos = pygame.mouse.get_pos()

        if self.button_rect.collidepoint(mouse_pos):
            button_color = self.light_grey
        else:
            button_color = self.dark_grey

        pygame.draw.rect(screen, button_color, self.button_rect, border_radius=8)
        pygame.draw.rect(screen, self.white, self.button_rect, width=2, border_radius=8)

        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)
        screen.blit(self.button_text, self.button_text_rect)

        #BOUTON QUITTER

        if self.quit_rect.collidepoint(mouse_pos):
            quit_color = (120, 0, 0)
        else:
            quit_color = (70, 0, 0)

        pygame.draw.rect(screen, quit_color, self.quit_rect, border_radius=6)
        pygame.draw.rect(screen, self.red, self.quit_rect, width=2, border_radius=6)

        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)
        screen.blit(self.quit_text, self.quit_text_rect)