"""
fonction draw de gameover

# texte dynamique : vies
        vie_text = self.text_font.render(
            f"Vies restantes : {self.game.player.lives}",
            True,
            (118, 255, 97)
        )

        vie_rect = vie_text.get_rect(center=(1280//2, 380))

        # texte dynamique : niveau
        level_text = self.text_font.render(
            f"Niveau : {self.game.current_level + 1}/10",
            True,
            (51,153,255)
        )

        level_rect = level_text.get_rect(center=(1280//2, 480))

        screen.blit(self.title, self.title_rect)
        screen.blit(vie_text, vie_rect)
        screen.blit(level_text, level_rect)
        
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

"""