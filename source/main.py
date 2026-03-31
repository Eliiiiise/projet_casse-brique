import pygame

if __name__ == '__main__':
    screen = pygame.display.set_mode((300, 200))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    print('Hello world')