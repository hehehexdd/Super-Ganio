from game_data.source.levels.mainmenulevel import *
import pygame
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
        self.timer_functions = {}

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

    def set_timer(self, function, time_in_seconds):
        start_time = time.time()
        end_time = time_in_seconds + start_time
        self.timer_functions[function] = end_time

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.current_level:
                self.current_level.handle_events(event)

    def tick(self, delta_time):
        functions_to_remove = []
        for function in self.timer_functions:
            if time.time() >= self.timer_functions[function]:
                function()
                functions_to_remove.append(function)
        for function in functions_to_remove:
            self.timer_functions.pop(function, None)
        functions_to_remove.clear()
        if self.current_level:
            self.current_level.hidden_tick(delta_time)
            self.current_level.tick(delta_time)

    def draw(self, renderer):
        if self.current_level:
            self.renderer.fill(self.current_level.background_color)
        else:
            self.renderer.fill(self.defaultBackgroundColor)

        if self.current_level:
            self.current_level.post_draw(self.renderer)

        self.window.flip()

    def restart(self):
        self.last_level = None
        self.current_level = MainMenu(self)

    def move_to_level(self, level):
        self.last_level = self.current_level
        self.current_level = level

    def stop(self):
        self.running = False
