#spécialisé pour les inputs (clavier,souris,clics,interactions)
#centraliser tout ce qui concerne les entrées utilisateur (inputs)
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
    # gestion des touches du clavier
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE: # ESC = quitter complètement le programme
            game.running = False 

        elif game.state == "playing":
            if event.key == pygame.K_p: # P = mettre le jeu en pause
                game.state = "pause"
            elif event.key == pygame.K_m:# M = retour menu principal
                game.state = "menu" 

        elif game.state == "pause":
            if event.key == pygame.K_p: # P = retour au jeu
                game.state = "playing"
            elif event.key == pygame.K_m: # M = retour menu principal
                game.state = "menu"

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

def handle_input(game, events):

    # souris
    handle_mouse(game)

    # événements clavier/souris
    for event in events:
           handle_keyboard(game, event)
           handle_click(game, event) 

           if game.state == "name_menu":
                game.name_menu.handle_event(event)

           if event.type == pygame.QUIT:  # si on clique sur la croix de la fenêtre
               game.running = False

                          