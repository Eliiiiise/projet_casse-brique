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

    def draw(self, screen): #affichage du menu 
        #couleur de fond
        screen.fill((0, 0, 255))

         #texte dynamique (score, level)
        #mettre a jour la position du texte vie en fonction de sa largeur pour qu'il soit toujours centré
        vie_rect = vie_text.get_rect(center=(1280//2, 380))
        
        #SCORE
        #score_text = self.text_font.render(
         #   f"Score: {self.game.player.score}",
          #  True,
           # (118,255,97)   
        #)
        #score_rect = score_text.get_rect(center=(1280//2, 430))

        #LEVEL
        level_text = self.text_font.render(
            f"Niveau : {self.game.current_level + 1}/10",
            True,
             (51,153,255)  
        )
        level_rect = level_text.get_rect(center=(1280//2, 480))

        #afficher le texte
        screen.blit(self.title, self.title_rect)
        #screen.blit(score_text, score_rect)
        screen.blit(level_text, level_rect)
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

