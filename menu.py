# menus (start,game over,next level)
# bouton, clic souris, changement d'état
import pygame
class Menu:
    def __init__(self, gameco):
        self.game = gameco
        
        #police du texte
        self.title_font= pygame.font.SysFont(None,80) #titre
        self.button_font= pygame.font.SysFont(None,50)#bouton
        self.text_font = pygame.font.SysFont(None, 40) #texte
        self.small_font = pygame.font.SysFont(None, 25,italic=True) #crédit en italique

        #boutton
        self.button_rect =pygame.Rect(540,300,150,50)

        # Texte
        self.title = self.title_font.render(
            "Casse Brique :",   # texte
            True,              
            (0,204,204)     
        )

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
        self.line2_rect = self.line2.get_rect(center=(centre_x, 370))
        self.line3_rect = self.line3.get_rect(center=(centre_x, 420))
        self.line4_rect = self.line4.get_rect(center=(centre_x, 470))
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)

        #texte en bas a droite 
        self.credit_rect = self.credit.get_rect(
            bottomright=(1250, 700)
        )


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.game.state = "playing"

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
        if self.button_rect.collidepoint(mouse_pos):
            color = (102, 255, 255)
        else:
            color = (102, 178, 255)

        # Dessine le bouton
        pygame.draw.rect(screen, color, self.button_rect)

        # Dessine le texte
        screen.blit(self.button_text, self.button_text_rect)




        # en pause un texte recap s'affiche genre points, nb de vie, level,... 
        # et quand je perds "game over" apparait en gros avec en dessous un recap des point du level et en dessous un bouton pour rejouer 
        # afficher un bouton menu sur la page pause en haut a droite
        # pendant le texte pause mettre un bouton recommencer
        # faire une partie entrer nom de joueur pour le highscore