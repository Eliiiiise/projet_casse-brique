import pygame
from window import *

class Game:
    __screen: pygame.Surface
    __screen_rect: pygame.Rect
    __screen_borders_lines: dict[str, pygame.Rect]
    __is_running: bool
    __clock: pygame.time.Clock
    __level_clock_ticks: int
    __frame_counter: int
    __game_state: str
    __borders_collision_sprites: pygame.sprite.Group
    __start_buttons: pygame.sprite.Group
    __end_buttons: pygame.sprite.Group
    __player: 'Player'
    __scores: 'Scoreboard'

    def __init__(self) -> None:
        pygame.init()
        self.__clock = pygame.time.Clock()
        self.__frame_counter = 0
        self.__is_running = False
        self.__init_screen()
        self.__game_state = "start"

    def __init_screen(self) -> None:
        self.__screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)
        self.__screen_rect = self.__screen.get_rect()

    def __init_start(self) -> None:
        self.__init_start_buttons()
        self.__player = Player(random.choice(PLAYER_NAMES), 0)
        self.__scores = Scoreboard()
        self.__scores.load_score()

    def __init_start_buttons(self) -> None:
        self.__start_buttons = pygame.sprite.Group()
        Button(
               pygame.Vector2(self.__screen_rect.center),
               pygame.Color(pygame.color.THECOLORS["green"]),
               pygame.Color(pygame.color.THECOLORS["white"]),
               "Play",
               self.__start_buttons
              )
        self.__start_buttons.sprites()[0].center_at_width()
        self.__start_buttons.sprites()[0].center_at_height()

    def __handle_start_events(self, event: pygame.event.Event) -> None:
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if self.__start_buttons.sprites()[0].rect.collidepoint(event.pos):
                    self.__game_state = "level"
                    self.__init_level()
            case pygame.QUIT:
                self.__is_running = False
                pygame.quit()
                sys.exit()

    def __draw_greetings(self) -> None:
        text = "Hello " + self.__player.name
        font = pygame.font.SysFont(None, TEXT_SIZE)
        text_render = font.render(text, True, pygame.Color(pygame.color.THECOLORS["white"]))
        self.__screen.blit(text_render, (self.__screen_rect.centerx - text_render.get_rect().width // 2, TEXT_SIZE))

    def __draw_start_buttons(self) -> None:
        self.__draw_greetings()
        self.__start_buttons.draw(self.__screen)

    def __inside_start_loop(self) -> None:
        for event in pygame.event.get():
            self.__handle_start_events(event)
        self.__draw_start_buttons()


    def __init_game(self) -> None:
        self.__init_actors()

    def __init_actors(self) -> None:
        self.__fires_sprites = pygame.sprite.Group()
        self.__borders_collision_sprites = pygame.sprite.Group()
        self.__init_spaceship()
        self.__init_asteroids()

    '''def __handle_game_events(self, event: pygame.event.Event) -> None:
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if self.__level < ONE_SHOOT_LEVEL:
                    self.__shoot_fire = True
                else:
                    self.__shoot_fire = False
                    self.__init_fire()
            case pygame.MOUSEBUTTONUP:
                self.__shoot_fire = False
            case pygame.MOUSEMOTION:
                if self.__spaceship_sprite.sprite is not None:
                    if pygame.mouse.get_focused():
                        self.__spaceship_sprite.sprite.actor.position = pygame.Vector2(pygame.mouse.get_pos())
                        if self.__level >= ONE_SHOOT_LEVEL:
                            for asteroid_sprite in self.__asteroids_sprites:
                                if pygame.mouse.get_rel()[0] > SPACESHIP["speed"].x:
                                    asteroid_sprite.actor.speed.y += 1
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        if self.__spaceship_sprite.sprite is not None:
                            self.__spaceship_sprite.sprite.actor.speed = -SPACESHIP["speed"].copy()
                    case pygame.K_RIGHT:
                        if self.__spaceship_sprite.sprite is not None:
                            self.__spaceship_sprite.sprite.actor.speed = SPACESHIP["speed"].copy()
                    case pygame.K_SPACE:
                        if self.__level < ONE_SHOOT_LEVEL:
                            self.__shoot_fire = True
                        else:
                            self.__shoot_fire = False
                            if self.__spaceship_sprite.sprite is not None:
                                self.__init_fire()
            case pygame.KEYUP:
                match event.key:
                    case pygame.K_LEFT:
                        if self.__spaceship_sprite.sprite is not None:
                            self.__spaceship_sprite.sprite.actor.speed = NULL_PYGAME_VECTOR2.copy()
                    case pygame.K_RIGHT:
                        if self.__spaceship_sprite.sprite is not None:
                            self.__spaceship_sprite.sprite.actor.speed = NULL_PYGAME_VECTOR2.copy()
                    case pygame.K_SPACE:
                        self.__shoot_fire = False
            case pygame.QUIT:
                self.__is_running = False
                pygame.quit()
                sys.exit()
                '''

    def __detect_borders_collisions(self) -> None:
        for actor_sprite in self.__borders_collision_sprites:
            for screen_border_name, screen_border_line in self.__screen_borders_lines.items():
                if actor_sprite.rect.colliderect(screen_border_line):
                    if screen_border_name == "left" and actor_sprite.actor.speed.x < 0:
                        actor_sprite.actor.speed.x = -actor_sprite.actor.speed.x
                    if screen_border_name == "right" and actor_sprite.actor.speed.x > 0:
                        actor_sprite.actor.speed.x = -actor_sprite.actor.speed.x
                    if screen_border_name == "top" and actor_sprite.actor.speed.y < 0:
                        actor_sprite.actor.speed.y = -actor_sprite.actor.speed.y
                    if screen_border_name == "bottom" and actor_sprite.actor.speed.y > 0:
                        actor_sprite.actor.speed.y = -actor_sprite.actor.speed.y
    '''
    def __detect_fires_collisions_with_asteroids(self):
        # hinted_asteroids_sprites = pygame.sprite.groupcollide(self.__asteroids_sprites, self.__fires_sprites, True, True)
        hinted_asteroids_sprites = pygame.sprite.groupcollide(self.__asteroids_sprites, self.__fires_sprites, False, True)
        for hinted_asteroid_sprite in hinted_asteroids_sprites:
            if hinted_asteroid_sprite.actor.diameter <= 10:
                hinted_asteroid_sprite.kill()
            else:
                hinted_asteroid_sprite.color = pygame.color.THECOLORS["yellow"]
                hinted_asteroid_sprite.actor.resize_on_center(-10)


    def __detect_fire_collisions_with_asteroids(self):
        if len(self.__fires_sprites) != 0:
            for fire_sprite in self.__fires_sprites:
                hinted_asteroids_sprites = pygame.sprite.spritecollide(fire_sprite, self.__asteroids_sprites,False)
                if len(hinted_asteroids_sprites) != 0:
                    for hinted_asteroid_sprite in hinted_asteroids_sprites:
                        if not hinted_asteroid_sprite.unhintable:
                            if  fire_sprite.rect.top - hinted_asteroid_sprite.rect.bottom <= fire_sprite.rect.height and fire_sprite.actor.speed.y < 0 :
                                if hinted_asteroid_sprite.actor.diameter <= ASTEROIDS["min_diameter"]:
                                    self.__player.score += 1
                                    hinted_asteroid_sprite.kill()
                                else:
                                    hinted_asteroid_sprite.actor.resize_on_center(-ASTEROIDS["min_diameter"])
                                    hinted_asteroid_sprite.color = pygame.color.THECOLORS["green"]
                                    hinted_asteroid_sprite.hinted = True
                            elif fire_sprite.rect.top - hinted_asteroid_sprite.rect.bottom <= fire_sprite.rect.height and fire_sprite.actor.speed.y > 0:
                                hinted_asteroid_sprite.actor.resize_on_center(ASTEROIDS["min_diameter"])
                                hinted_asteroid_sprite.color = pygame.color.THECOLORS["red"]
                                hinted_asteroid_sprite.hinted = True
                            fire_sprite.kill()


    def __detect_asteroid_out_of_game(self):
        for asteroid_sprite in self.__asteroids_sprites:
            if not self.__screen_rect.contains(asteroid_sprite.rect):
                asteroid_sprite.kill()
        if len(self.__asteroids_sprites) == 0:
            self.__to_next_level_or_end()
            

    def __detect_game_collisions(self):
        self.__detect_borders_collisions()
        # self.__handle_fires_collisions_with_asteroids()
        self.__detect_fire_collisions_with_asteroids()
        self.__detect_spaceship_collisions_with_asteroids()
        self.__detect_asteroid_out_of_game()



    def __update_actors(self) -> None:
        self.__spaceship_sprite.update()
        self.__asteroids_sprites.update()
        self.__fires_sprites.update()
    '''

    def __draw_screen_borders(self) -> None:
        self.__screen_borders_lines = {}
        screen_rect = self.__screen.get_rect()
        screen_borders = {
                          "left":   {"offset": pygame.Vector2(+1, 0), "start": screen_rect.topleft,    "end": screen_rect.bottomleft},
                          "right":  {"offset": pygame.Vector2(-1, 0), "start": screen_rect.topright,   "end": screen_rect.bottomright},
                          "top":    {"offset": pygame.Vector2(0, +1), "start": screen_rect.topleft,    "end": screen_rect.topright },
                          "bottom": {"offset": pygame.Vector2(0, -1), "start": screen_rect.bottomleft, "end": screen_rect.bottomright}
        }
        for border_name in WINDOW_BORDERS_NAME:
            offset = WINDOW_BORDER_LINE_OFFSET * screen_borders[border_name]["offset"] // 2
            border_line = pygame.draw.line(
                self.__screen,
                pygame.color.THECOLORS[WINDOW_BORDERS_COLOR[border_name]],
                pygame.Vector2(screen_borders[border_name]["start"]) + offset,
                pygame.Vector2(screen_borders[border_name]["end"]) + offset,
                width = WINDOW_BORDER_LINE_OFFSET
            )
            self.__screen_borders_lines[border_name] = border_line

    def __draw_score(self) -> None:
        font = pygame.font.SysFont(None, TEXT_SIZE)
        text_render = font.render(str(self.__player.score), True, pygame.Color(pygame.color.THECOLORS["white"]))
        self.__screen.blit(text_render,
                           (self.__screen_rect.right - TEXT_SIZE // 4 - text_render.get_rect().width, TEXT_SIZE // 4))
    '''
    def __draw_actors(self) -> None:
        self.__spaceship_sprite.draw(self.__screen)
        self.__asteroids_sprites.draw(self.__screen)
        self.__fires_sprites.draw(self.__screen)
        self.__draw_score()
    '''

    def __inside_game_loop(self) -> None:
        for event in pygame.event.get():
            self.__handle_game_events(event)
        self.__draw_screen_borders()
        if self.__shoot_fire:
            self.__init_fire()
        self.__detect_game_collisions()
        self.__update_actors()
        self.__draw_actors()

    def __init_end(self) -> None:
        self.__init_end_buttons()

    def __init_end_buttons(self) -> None:
        self.__end_buttons = pygame.sprite.Group()
        Button(
            pygame.Vector2(self.__screen_rect.width // 4, self.__screen_rect.bottom - 1.5 * TEXT_SIZE),
            pygame.Color(pygame.color.THECOLORS["orange"]),
            pygame.Color(pygame.color.THECOLORS["white"]),
            " Quit ",
            self.__end_buttons
        )
        self.__end_buttons.sprites()[0].center_at_width()
        Button(
            pygame.Vector2(3 * self.__screen_rect.width // 4, self.__screen_rect.bottom - 1.5 * TEXT_SIZE),
            pygame.Color(pygame.color.THECOLORS["green"]),
            pygame.Color(pygame.color.THECOLORS["white"]),
            "Replay",
            self.__end_buttons
        )
        self.__end_buttons.sprites()[1].center_at_width()
    
    def __handle_end_events(self, event: pygame.event.Event) -> None:
        match event.type:
            case pygame.MOUSEBUTTONDOWN:
                if self.__end_buttons.sprites()[0].rect.collidepoint(event.pos):
                    self.__is_running = False
                    pygame.quit()
                    sys.exit()
                elif self.__end_buttons.sprites()[1].rect.collidepoint(event.pos):
                    self.__player.score = 0
            case pygame.QUIT:
                self.__is_running = False
                pygame.quit()
                sys.exit()
    

    def __draw_top_5_scores(self) -> None:
        font = pygame.font.SysFont(None, TEXT_SIZE)
        i = 0.5
        text_render = font.render("Top 5 scores", True, pygame.Color(pygame.color.THECOLORS["white"]))
        self.__screen.blit(text_render, (self.__screen_rect.centerx - text_render.get_width() // 2, TEXT_SIZE * i))
        i += 1
        for player in self.__scores.players:
            text_render = font.render(player.name, True, pygame.Color(pygame.color.THECOLORS["white"]))
            self.__screen.blit(text_render, (TEXT_SIZE, TEXT_SIZE * i))
            text_render = font.render(str(player.score), True, pygame.Color(pygame.color.THECOLORS["white"]))
            self.__screen.blit(text_render,
                               (self.__screen_rect.right - TEXT_SIZE - text_render.get_rect().width, TEXT_SIZE * i))
            i += 1

    def __draw_end_buttons(self) -> None:
        self.__end_buttons.draw(self.__screen)
        self.__draw_top_5_scores()

    def __inside_end_loop(self) -> None:
        for event in pygame.event.get():
            self.__handle_end_events(event)
        self.__draw_end_buttons()

    def run(self) -> None:
        self.__is_running = True
        self.__frame_counter = 0
        self.__init_start()
        while self.__is_running:
            self.__clock.tick_busy_loop(FPS)
            self.__frame_counter += 1
            self.__screen.fill(GAME_COLOR)
            match self.__game_state:
                case "start":
                    self.__inside_start_loop()
                case "level":
                    self.__inside_level_loop()
                case "play":
                    self.__inside_game_loop()
                case "end":
                    self.__inside_end_loop()
            pygame.display.flip()


game = Game()
game.run()
