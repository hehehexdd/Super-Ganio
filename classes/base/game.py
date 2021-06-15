from classes.levels.mainmenulevel import *
import pygame
import time


class Game:
    def __init__(self, window_size, default_background_color):
        pygame.init()
        self.window = pygame.display
        self.window.set_caption("Super Ganio!")
        self.renderer = self.window.set_mode(window_size)
        self.running = False
        self.defaultBackgroundColor = default_background_color
        self.level = None
        self.previous_level = None
        self.start_time = 0.0
        self.end_time = 0.0

    def start(self):
        self.running = True
        self.move_to_level(MainMenu(self))

        delta = self.end_time - self.start_time

        while self.running:
            if self.level:
                self.renderer.fill(self.level.background_color)
            else:
                self.renderer.fill(self.defaultBackgroundColor)

            if self.level:
                if delta > 0:
                    self.level.tick(delta)
                else:
                    self.level.tick(0.0)

            self.handle_events()

            self.start_time = time.time()
            if self.level:
                self.level.display_assets(self.renderer)
            self.end_time = time.time()

            self.window.flip()

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if self.level:
                self.level.handle_events(event)

    def move_to_level(self, level):
        self.previous_level = self.level
        self.level = level

    def stop(self):
        self.running = False
