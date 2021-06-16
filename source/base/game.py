from source.levels.mainmenulevel import *
import pygame
import pytmx
import time


class Game:
    def __init__(self, window_size, default_background_color):
        pygame.init()
        self.window = pygame.display
        self.window.set_caption("Super Ganio!")
        self.renderer = self.window.set_mode(window_size)
        self.defaultBackgroundColor = default_background_color
        self.running = False
        self.last_level = None
        self.current_level = None
        self.delta_time = 0.0

    def start(self):
        self.running = True
        self.move_to_level(MainMenu(self))
        previous_time = time.time()

        while self.running:
            time_now = time.time()
            self.delta_time = (time_now - previous_time)
            previous_time = time_now

            self.handle_events()
            self.tick(self.delta_time)
            self.draw(self.renderer)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.current_level:
                self.current_level.handle_events(event)

    def tick(self, delta_time):
        if self.current_level:
            self.current_level.tick(delta_time)

    def draw(self, renderer):
        if self.current_level:
            self.renderer.fill(self.current_level.background_color)
        else:
            self.renderer.fill(self.defaultBackgroundColor)

        if self.current_level:
            self.current_level.post_draw(self.renderer)

        self.window.flip()

    def move_to_level(self, level):
        self.last_level = self.current_level
        self.current_level = level

    def stop(self):
        self.running = False
