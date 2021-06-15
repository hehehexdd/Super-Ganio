from classes.buttons.base.button import *
from classes.widgets.base.widget import *
from classes.entities.base.Entity import *


class Level:
    def __init__(self, instance: object):
        self.drawables = {}
        self.entities = []
        self.current_widget = None
        self.previous_widget = None
        self.gameInstance = instance

    def handle_events(self, event: pygame.event.Event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if self.current_widget is not None:
                self.current_widget.handle_event(ButtonEvent.Hover, mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_widget is not None:
                self.current_widget.handle_event(ButtonEvent.Click, mouse_pos)

    def tick(self, delta_time):
        for entity in self.entities:
            if entity.start_ticking:
                entity.tick(delta_time)

    def display_assets(self, renderer):
        for drawable in self.drawables:
            renderer.blit(drawable, self.drawables.get(drawable))
        if self.current_widget is not None:
            self.current_widget.draw(self.gameInstance.renderer)

    def move_assets(self, move_by):
        pass

    def set_widget(self, widget: Widget):
        self.previous_widget = self.current_widget
        self.current_widget = widget

    def remove_widget(self):
        self.current_widget = None
