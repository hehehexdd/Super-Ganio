from classes.levels.mainmenulevel import *


class Game:
    def __init__(self, window_size, default_background_color):
        pygame.init()
        self.window = pygame.display
        self.renderer = self.window.set_mode(window_size)
        self.running = False
        self.defaultBackgroundColor = default_background_color
        self.level = None
        self.previous_level = None

    def start(self):
        self.running = True
        self.move_to_level(MainMenu(self))

        while self.running:
            self.renderer.fill(self.defaultBackgroundColor)
            self.handle_events()

            if self.level:
                self.level.display_assets(self.renderer)

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
