from classes.buttons.base.button import *


class Level:
    def __init__(self, instance: object):
        self.drawables = {}
        self.buttons = []
        self.gameInstance = instance

    def handle_events(self, event: pygame.event.Event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            for button in self.buttons:
                button.handle_event(ButtonEvent.Hover, mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                button.handle_event(ButtonEvent.Click, mouse_pos)

    def update(self):
        pass

    def display_assets(self, renderer):
        for drawable in self.drawables:
            renderer.blit(drawable, self.drawables.get(drawable))
        for btn in self.buttons:
            btn.draw(self.gameInstance.renderer)

    def move_assets(self):
        pass
