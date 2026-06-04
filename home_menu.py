'''
Ce module gère le menu d'accueil (Home Menu) du jeu de casse-brique. 
Il affiche le titre du jeu, les instructions de base, les crédits, et propose un bouton pour commencer à jouer.
'''
import pygame
class HomeMenu:
    def __init__(self, gameco):
        self.game = gameco
        
        #police du texte
        self.title_font= pygame.font.SysFont(None,80) #titre
        self.button_font= pygame.font.SysFont(None,50)#bouton
        self.quit_font= pygame.font.SysFont(None,50)#bouton rejouer
        self.text_font = pygame.font.SysFont(None, 40) #texte
        self.small_font = pygame.font.SysFont(None, 25,italic=True) #crédit en italique

        # couleurs du menu
        self.bg_color = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (170, 170, 170)
        self.dark_grey = (35, 35, 35)
        self.pink = (255, 65, 161)
        self.pink_hover = (255, 120, 190)
        self.red = (255, 60, 60)

        centre_x = 1280 // 2
        centre_y = 720 // 2

        #boutton
        self.button_rect = pygame.Rect(0, 0, 150, 50)
        self.button_rect.center = (centre_x, 300)
        self.quit_rect = pygame.Rect(1200, 20, 40, 40) # position en haut a droite

        # Texte titre
        self.title = self.title_font.render(
            "CASSE-BRIQUE",
            True,              
            self.white    
        )

        #Texte instructions
        self.pause_text = self.text_font.render(
            "Appuie sur P pour mettre en pause",
            True,
            self.grey
        )
        self.menu_text = self.text_font.render(
            "Appuie sur M pour accéder au menu",
            True,
            self.grey  
        )
        self.quit_text = self.text_font.render(
            "Appuie sur ESC pour quitter",
            True,
            self.grey  
        )

        #Texte crédits
        self.credit = self.small_font.render(
            "Made by Estiiiiiii & Eliiiiise",
            True,
            self.grey
        )

        #Texte bouton
        self.button_text = self.button_font.render(
            "JOUER",
            True,
            self.white
        )
        
         # Texte bouton X
        self.quit_text = self.quit_font.render("X", True, (255, 255, 255))

        
        # Position du texte
        self.title_rect = self.title.get_rect(
            center=(centre_x, 200)   #centré haut
        )
        
        #centré au milieu (espacé vertical)
        self.pause_text_rect = self.pause_text.get_rect(center=(centre_x, 380))
        self.menu_text_rect = self.menu_text.get_rect(center=(centre_x, 430))
        self.quit_text_rect = self.quit_text.get_rect(center=(centre_x, 480))
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)


        # position du texte en bas a droite 
        self.credit_rect = self.credit.get_rect(
            bottomright=(1250, 700)
        )

    def update(self): 
        '''
        Méthode appelée à chaque frame (utile plus tard pour animations)
        '''
        pass

    def draw(self, screen): 
        '''
        affichage du menu 
        '''
        #couleur de fond
        screen.fill((0, 0, 0))
        
        #afficher le texte
        screen.blit(self.title, self.title_rect)
        screen.blit(self.pause_text, self.pause_text_rect)
        screen.blit(self.menu_text, self.menu_text_rect)
        screen.blit(self.quit_text, self.quit_text_rect)
        screen.blit(self.credit, self.credit_rect)
       
        # Bouton "Jouer"
        mouse_pos = pygame.mouse.get_pos()
        # Si la souris est dessus → couleur plus claire
        if self.button_rect.collidepoint(mouse_pos): # quand la souris est dessus
            color = self.pink_hover 
        else: #de base
            color = self.pink 

        # Dessine le bouton avec contour blanc
        pygame.draw.rect(screen, color, self.button_rect)

        # Dessine le texte
        screen.blit(self.button_text, self.button_text_rect)

       # Bouton "X" pour quitter
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



   