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
        self.button_rect =pygame.Rect(540,300,150,50)
        self.quit_rect = pygame.Rect(1200, 20, 50, 50) # position en haut a droite

        # Texte titre
        self.title = self.title_font.render(
            "GAME OVER :",
            True,              
            (255,0,0)     
        )
        # texte score 
        self.score_text = self.text_font.render(
            "Score : 0",
            True,
            (118,255,97)  
        )
        # texte level
        self.level_text = self.text_font.render(
            "Niveau : 1/10",
            True,
            (118,255,97)  
        )
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
        self.score_rect_rect = self.score_text.get_rect(center=(centre_x, 380))
        self.lev_rect_rect = self.level_text.get_rect(center=(centre_x, 430))
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
        #couleur de fond
        screen.fill((0, 0, 0))
        #afficher le texte
        screen.blit(self.title, self.title_rect)
        screen.blit(self.score, self.score_rect)
        screen.blit(self.level, self.level_rect)
        screen.blit(self.credit, self.credit_rect)
       
        
        #bouton 
        mouse_pos = pygame.mouse.get_pos()
        # Si la souris est dessus → couleur plus claire
        if self.button_rect.collidepoint(mouse_pos): # quand la souris est dessus 
            color = (102, 255, 255) 
        else:  # de base 
            color = (102, 178, 255)

        # Dessine les boutons
        pygame.draw.rect(screen, color, self.button_rect)

        # Dessine le texte
        screen.blit(self.button_text, self.button_text_rect)

        #bouton X
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
        pygame.draw.rect(screen, color, scale_rect)

        # Dessine le texte
        screen.blit(self.quit_text, self.quit_text_rect)

