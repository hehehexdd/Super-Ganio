from source.buttons.base.button import *
from source.widgets.base.widget import *
from source.entities.base.entity import *


class Level:
    def __init__(self, instance: object):
        self.collisions = []
        self.entities = []
        self.player = None
        self.camera = None
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

    def hidden_tick(self, delta_time):
        pass

    def tick(self, delta_time):
        for entity in self.entities:
            if entity.start_ticking:
                entity.tick(delta_time)
        if self.player:
            if self.player.start_ticking:
                self.player.tick(delta_time)
        self.hidden_tick(delta_time)

    def post_draw(self, renderer):
        self.draw(renderer)

        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def draw(self, renderer):
        pass

    def check_collides_any(self, rect: tuple):
        for collision in self.collisions:
            if collision.colliderect(rect):
                return True
        if self.player:
            if rect.left < 0:
                return True
            elif rect.top < 0:
                return True
            elif rect.right > self.map.width:
                return True
            elif rect.bottom > self.map.height:
                return True
        return False

    def set_widget(self, widget: Widget):
        self.previous_widget = self.current_widget
        self.current_widget = widget

    def remove_widget(self):
        self.current_widget = None

