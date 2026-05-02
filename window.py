# crée la fenêtre , gérer le screen, clear() / update()
import pygame
import os

WINDOW_SIZE: pygame.Vector2 = pygame.Vector2(1280, 720)
WINDOW_TITLE: str = str(os.path.basename(__file__)).replace(".py", "")
WINDOW_BORDER_LINE_OFFSET: int = int(WINDOW_SIZE.x // 96)
WINDOW_BORDERS_NAME: list[str] = ["left", "right", "top"]
WINDOW_BORDERS_COLOR: dict[str, str] = {"left" : "red", "right" : "red", "top" : "red", "bottom" : "red"}
GAME_COLOR: pygame.Color = pygame.Color(pygame.color.THECOLORS["black"])
TEXT_SIZE: int = int(WINDOW_SIZE.x // 12)
FPS: int = 60
NULL_PYGAME_VECTOR2: pygame.Vector2 = pygame.Vector2(0, 0)

