# menus (start,game over,next level)
# bouton jouer
import pygame
class HomeMenu:
    def __init__(self, gameco):
        self.game = gameco
        
        #police du texte
        self.title_font= pygame.font.SysFont(None,80) #titre
        self.button_font= pygame.font.SysFont(None,50)#bouton
        self.text_font = pygame.font.SysFont(None, 40) #texte
        self.small_font = pygame.font.SysFont(None, 25,italic=True) #crédit en italique

        #boutton
        self.button_rect =pygame.Rect(540,300,150,50)

        # Texte titre
        self.title = self.title_font.render(
            "Casse Brique :",
            True,              
            (0,204,204)     
        )

        #texte instructions
        self.line2 = self.text_font.render(
            "Appuie sur P pour mettre en pause",
            True,
            (51,153,255)  
        )
        self.line3 = self.text_font.render(
            "Appuie sur M pour accéder au menu",
            True,
            (51,153,255)  
        )
        self.line4 = self.text_font.render(
            "Appuie sur ESC pour quitter",
            True,
            (102,102,255)  
        )

        #texte crédits
        self.credit = self.small_font.render(
            "Made by Estiiiiiii & Eliiiiise",
            True,
            (153,204,255)
        )

        #texte bouton
        self.button_text = self.button_font.render("Jouer", True, (255, 255, 255))

        
        # Position du texte 
        centre_x=1280//2 #centre ecran
        centre_y=720//2 # centre ecran
        self.title_rect = self.title.get_rect(
            center=(centre_x, 200)   #centré haut
        )
        
        #centré au milieu (espacé vertical)
        self.line2_rect = self.line2.get_rect(center=(centre_x, 380))
        self.line3_rect = self.line3.get_rect(center=(centre_x, 430))
        self.line4_rect = self.line4.get_rect(center=(centre_x, 480))
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

        #texte en bas a droite 
        self.credit_rect = self.credit.get_rect(
            bottomright=(1250, 700)
        )

    def update(self): 
        '''
        Méthode appelée à chaque frame (utile plus tard pour animations)
        '''
        pass

    def draw(self, screen): #affichage du menu 
       
        #couleur de fond
        screen.fill((0, 0, 0))
        
        #afficher le texte
        screen.blit(self.title, self.title_rect)
        screen.blit(self.line2, self.line2_rect)
        screen.blit(self.line3, self.line3_rect)
        screen.blit(self.line4, self.line4_rect)
        screen.blit(self.credit, self.credit_rect)
       
        #bouton 
        mouse_pos = pygame.mouse.get_pos()
        # Si la souris est dessus → couleur plus claire
        if self.button_rect.collidepoint(mouse_pos): # quand la souris est dessus
            color = (102, 255, 255) 
        else: #de base
            color = (102, 178, 255) 

        # Dessine le bouton
        pygame.draw.rect(screen, color, self.button_rect)

        # Dessine le texte
        screen.blit(self.button_text, self.button_text_rect)




    '''
        def update(self):
       
    # position de la souris
        mouse_pos = pygame.mouse.get_pos()
    # clic souris
        mouse_click = pygame.mouse.get_pressed()
        # Vérifie si :
        # - la souris est sur le bouton
        # - le clic gauche est enfoncé
        if self.button_rect.collidepoint(mouse_pos):
            if mouse_click[0]:  # bouton gauche
                self.game.state = "playing"
    '''