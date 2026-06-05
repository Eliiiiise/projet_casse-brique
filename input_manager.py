'''
Ce module gère les entrées utilisateur (inputs) pour le jeu de casse-brique.
Il centralise tout ce qui concerne les interactions de l'utilisateur, telles que: 
les clics de souris, les touches du clavier, et les mouvements de la souris.
'''
import pygame

def handle_mouse(game):
    """
    Gère la souris en fonction de l'état du jeu
    """
    # Si on est en train de jouer
    if game.state == "playing":

        # cache la souris
        pygame.mouse.set_visible(False)

        # bloque la souris dans la fenêtre
        pygame.event.set_grab(True)

    else:
        # affiche la souris (menu, pause, game over,…)
        pygame.mouse.set_visible(True)

        # libére la souris
        pygame.event.set_grab(False)

def handle_keyboard (game,event):  
    """
    Gère les touches clavier 
    """    
    #partout
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE: # ESC = quitter complètement le programme
            game.running = False 

        #----------------------------
        # EN JEU
        #----------------------------
        elif game.state == "playing":
            if event.key == pygame.K_p: # P = mettre le jeu en pause
                game.state = "pause"
            elif event.key == pygame.K_m:# M = retour menu principal
                game.state = "menu" 

        #----------------------------
        # PAUSE
        # ----------------------------    
        elif game.state == "pause":
            if event.key == pygame.K_p: # P = retour au jeu
                game.state = "playing"
            elif event.key == pygame.K_m: # M = retour menu principal
                game.state = "menu"

        #----------------------------
        # MENU DE SAISIE DU PSEUDO
        #----------------------------
        elif game.state == "name_menu":
            if event.key == pygame.K_RETURN: # touche ENTER : validation du pseudo

                # vérifie qu'un pseudo a été saisi
                if game.name_menu.name.strip() != "":
                    game.player.name = game.name_menu.name.strip()

                # pseudo par défaut si rien n'est écrit
                else:
                    game.player.name = "Player"

                # réinitialise la partie
                game.reset_game()

                # lance le jeu
                game.state = "playing"

            elif event.key == pygame.K_BACKSPACE: # touche supprimer

                 # supprime le dernier caractère
                game.name_menu.name = game.name_menu.name[:-1]

            else: # toutes les autres touches

                 # ajoute le caractère saisi
                game.name_menu.name += event.unicode


def handle_click (game,event):  
    """
    Gère les clics de la souris 
    """    
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

        mouse_pos = pygame.mouse.get_pos()

        # ---------------------------
        # MENU PRINCIPAL
        # ---------------------------
        if game.state == "menu":

            if game.home_menu.button_rect.collidepoint(mouse_pos):
                game.state = "name_menu" # transition vers le menu de saisie du pseudo avant de commencer le jeu

            elif game.home_menu.quit_rect.collidepoint(mouse_pos):
                print("QUIT")
                game.running = False

        # ---------------------------
        # MENU DE SAISIE DU PSEUDO
        # ---------------------------
        elif game.state == "name_menu":

            if game.name_menu.quit_rect.collidepoint(mouse_pos):
                print("QUIT")
                game.running = False

        # ---------------------------
        # MENU PAUSE
        # ---------------------------
        elif game.state == "pause":

            # bouton reprendre
            if game.pause_menu.button_rect.collidepoint(mouse_pos):
                print("REPRENDRE")
                game.state = "playing"

            # bouton quitter (X)
            elif game.pause_menu.quit_rect.collidepoint(mouse_pos):
                print("QUIT")
                game.running = False

            # bouton home
            elif game.pause_menu.home_rect.collidepoint(mouse_pos):
                print("HOME")
                game.state = "menu"

        # ---------------------------
        # GAME OVER
        # ---------------------------
        elif game.state == "game_over":

            if game.gameover_menu.button_rect.collidepoint(mouse_pos):
                game.reset_game()
                game.state = "playing"

            #bouton quitter (X)    
            elif game.gameover_menu.quit_rect.collidepoint(mouse_pos):
                print("QUIT")
                game.running = False

            # bouton home
            elif game.pause_menu.home_rect.collidepoint(mouse_pos):
                print("HOME")
                game.state = "menu"

def handle_input(game, events):
    '''
    Gère tous les inputs (clavier, souris, clics) en fonction de l'état du jeu
    '''
    # souris
    handle_mouse(game)

    # événements clavier/souris
    for event in events:
           handle_keyboard(game, event)
           handle_click(game, event) 

           if event.type == pygame.QUIT:  # si on clique sur la croix de la fenêtre
               game.running = False

                          