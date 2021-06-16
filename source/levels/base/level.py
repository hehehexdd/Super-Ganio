from source.buttons.base.button import *
from source.widgets.base.widget import *
from source.entities.base.entity import *


class Level:
    def __init__(self, instance: object):
        self.surfaces = {}
        self.surface_offset = [0, 0]
        self.entities = []
        self.player = None
        self.current_widget = None
        self.previous_widget = None
        self.game_instance = instance
        self.background_color = (0, 0, 0, 255)

    def handle_events(self, event: pygame.event.Event):
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if self.current_widget is not None:
                self.current_widget.handle_event(ButtonEvent.Hover, mouse_pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_widget is not None:
                self.current_widget.handle_event(ButtonEvent.Click, mouse_pos)

        self.post_handle_events(event)

    def post_handle_events(self, event: pygame.event.Event):
        pass

    def tick(self, delta_time):
        for entity in self.entities:
            if entity.start_ticking:
                entity.tick(delta_time)
        if self.player:
            self.player.tick(delta_time)

    def display_assets(self, renderer):
        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def check_collides_any(self, rect: tuple):
        for surface in self.surfaces:
            if surface.get_rect(topleft=self.surfaces[surface]).colliderect(rect):
                return True
        return False

    def set_widget(self, widget: Widget):
        self.previous_widget = self.current_widget
        self.current_widget = widget

    def remove_widget(self):
        self.current_widget = None

