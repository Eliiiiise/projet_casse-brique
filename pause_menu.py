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

        #boutons
        self.button_rect =pygame.Rect(540,300,180,50)
        self.quit_rect = pygame.Rect(1200, 20, 40, 40) # position en haut a droite
        self.home_rect = pygame.Rect(self.quit_rect.x -70, #décalé à gauche
                                     20,40,40)


        # Texte titre
        self.title = self.title_font.render(
            "Pause :",
            True,              
            (0,204,204)     
        )

        #texte instructions
        self.vie = self.text_font.render(
            "nombre de vie: x",
            True,
            (51,153,255)  
        )
        self.score = self.text_font.render(
            "Score :0",
            True,
            (51,153,255)  
        )
        self.level = self.text_font.render(
            "Niveau : 1/10",
            True,
             (51,153,255)  
        )

        
        #texte bouton
        self.button_text = self.button_font.render("Reprendre", True, (255, 255, 255))

        # texte bouton X
        self.quit_text = self.quit_font.render("X", True, (255, 255, 255))

        
        # Position du texte 
        centre_x=1280//2 #centre ecran
        centre_y=720//2 # centre ecran
        self.title_rect = self.title.get_rect(
            center=(centre_x, 200)   #centré haut
        )
        
        #centré au milieu (espacé vertical)
        self.vie_rect = self.vie.get_rect(center=(centre_x, 380))
        self.score_rect = self.score.get_rect(center=(centre_x, 430))
        self.level_rect = self.level.get_rect(center=(centre_x, 480))
        self.button_text_rect = self.button_text.get_rect(center=self.button_rect.center)
        self.quit_text_rect = self.quit_text.get_rect(center=self.quit_rect.center)

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
                self.game.state = "playing"

        if event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_pos = pygame.mouse.get_pos()
                 
                # si la souris est sur la croix
                 if self.quit_rect.collidepoint(mouse_pos):
                    # quitter le jeu
                    self.game.running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            # si la souris est sur la croix
            if self.home_rect.collidepoint(mouse_pos):
                print("HOME CLIQUE ✅")  # debug
                
                # retour au menu principal
                self.game.state = "menu"


    def draw(self, screen): #affichage du menu 
        
        #afficher le texte
        screen.blit(self.title, self.title_rect)
        screen.blit(self.vie, self.vie_rect)
        screen.blit(self.score, self.score_rect)
        screen.blit(self.level, self.level_rect)
       
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

        #bouton home
        mouse_pos = pygame.mouse.get_pos()
        hover = self.home_rect.collidepoint(mouse_pos)
        # Si la souris est dessus → couleur plus claire et grossissement du bouton
        if hover: # quand la souris est dessus 
            color = (204, 0, 102) 
            scale_rect = self.quit_rect.inflate(10, 10)

        else: # de base 
            color = (255, 0, 127)
            scale_rect = self.quit_rect


    # Dessine le bouton home
        # mur
        pygame.draw.rect(screen, color, (self.home_rect.x +5, self.home_rect.y +15,30,25))
         
        # toit (tiangle)
        pygame.draw.polygon(screen,color,[(self.home_rect.x +0, self.home_rect.y+20),
                                          (self.home_rect.x +20, self.home_rect.y+0),
                                          (self.home_rect.x +40, self.home_rect.y +20),
                                          ]
                            )

       


   