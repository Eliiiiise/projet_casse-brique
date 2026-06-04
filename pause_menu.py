'''
Ce module gère le menu de pause du jeu de casse-brique.
Il affiche les informations de la partie en cours (score, niveau, vies restantes), 
et propose des options pour reprendre la partie, retourner au menu principal ou quitter le jeu.
'''
# affiche le menu pause
# bouton play
import pygame

class PauseMenu:
    def __init__(self, gameco):
        self.game = gameco
        
        #police du texte
        self.title_font= pygame.font.SysFont(None,80) #titre
        self.button_font= pygame.font.SysFont(None,50)#bouton
        self.quit_font= pygame.font.SysFont(None,50)#bouton rejouer
        self.text_font = pygame.font.SysFont(None, 40) #texte

        #couleurs
        self.bg_color = (0, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (170, 170, 170)
        self.light_grey = (220, 220, 220)
        self.dark_grey = (35, 35, 35)
        self.pink = (255, 65, 161)
        self.pink_hover = (255, 120, 190)
        self.red = (255, 60, 60)

        #boutons
        self.button_rect =pygame.Rect(540,300,180,50)
        self.quit_rect = pygame.Rect(1200, 20, 40, 40) # position en haut a droite
        self.home_rect = pygame.Rect(self.quit_rect.x -70, 20, 40, 40) # décalé à gauche

        # Texte titre
        self.title = self.title_font.render(
            "PAUSE",
            True,              
            self.white     
        )

        # Texte info pause
        self.pause_text = self.text_font.render(
            "Appuie sur P pour reprendre",
            True,
            self.grey
        )
        
        # Texte bouton reprendre
        self.button_text = self.button_font.render("Reprendre", True, (255, 255, 255))

        # Texte bouton X
        self.quit_text = self.quit_font.render("X", True, (255, 255, 255))

        
        # Position du texte 
        centre_x=1280//2 #centre ecran
        centre_y=720//2 # centre ecran
        self.title_rect = self.title.get_rect(
            center=(centre_x, 200)   #centré haut
        )
        
        # centré au milieu (espacé vertical)
        self.vie_rect = pygame.Rect(0, 0, 0, 0) # Initialisation vide, sera mis à jour dans draw() pour être centré dynamiquement
        self.vie_rect.center = (centre_x, 280) 
        self.score_rect = pygame.Rect(0, 0, 0, 0) # Initialisation vide, sera mis à jour dans draw() pour être centré dynamiquement 
        self.score_rect.center = (centre_x, 330)
        self.level_rect= pygame.Rect(0, 0, 0, 0) # Initialisation vide, sera mis à jour dans draw() pour être centré dynamiquement
        self.level_rect.center = (centre_x, 380)
        self.button_rect = pygame.Rect(0, 0, 180, 50)
        self.button_rect.center = (centre_x, 480)
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)

    def update(self): 
        '''
        Méthode appelée à chaque frame (utile plus tard pour animations)
        '''
        pass


    def draw(self, screen): #affichage du menu 
        '''
        affichage du menu pause 
        '''
        # titre pause
        pause_text = self.title_font.render(
            "PAUSE",
            True,
            self.white
        )

        pause_rect = pause_text.get_rect(
            center=(1280 // 2, 170)
        )
            
        #TEXTES DYNAMIQUES
        #vies
        vie_text = self.text_font.render(
            f"nombre de vie: {self.game.player.lives}",
            True,
            self.grey 
        )
        #mettre a jour la position du texte vie en fonction de sa largeur pour qu'il soit toujours centré
        vie_rect = vie_text.get_rect(center=(1280//2, 280))

        #score
        score_text = self.text_font.render(
            f"Score : {self.game.player.score}",
            True,
            self.grey
        )

        score_rect = score_text.get_rect(center=(1280 // 2, 330))
       
        #niveau
        level_text = self.text_font.render(
            f"Niveau : {self.game.current_level + 1}/10",
            True,
             self.grey  
        )
        level_rect = level_text.get_rect(center=(1280//2, 380))

        # instructions clavier
        controls_text = self.text_font.render(
            "P : reprendre    |    M : menu principal",
            True,
            self.grey
        )
        controls_rect = controls_text.get_rect(center=(1280 // 2, 600))
        
        # afficher le texte
        screen.blit(pause_text, pause_rect)
        screen.blit(vie_text, vie_rect)
        screen.blit(score_text, score_rect)
        screen.blit(level_text, level_rect)
        screen.blit(controls_text, controls_rect)
       
        # Bouton "Reprendre"
        mouse_pos = pygame.mouse.get_pos()
        # Si la souris est dessus → couleur plus claire
        if self.button_rect.collidepoint(mouse_pos): # quand la souris est dessus
            color = self.pink_hover
        else: #de base
            color = self.pink 

        # Dessine le bouton
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

        # Bouton "Home"
        mouse_pos = pygame.mouse.get_pos()
        hover = self.home_rect.collidepoint(mouse_pos)
        # Si la souris est dessus → couleur plus claire et grossissement du bouton
        if hover: # quand la souris est dessus 
            color = self.pink_hover
            scale_rect = self.home_rect.inflate(10, 10)

        else: # de base 
            color = self.pink
            scale_rect = self.home_rect

        # Dessine le bouton home
        # mur
        pygame.draw.rect(screen, color, (self.home_rect.x +5, self.home_rect.y +15,30,25))
         
        # toit (tiangle)
        pygame.draw.polygon(screen,color,[(self.home_rect.x +0, self.home_rect.y+20),
                                          (self.home_rect.x +20, self.home_rect.y+0),
                                          (self.home_rect.x +40, self.home_rect.y +20),
                                          ]
                            )

       


   