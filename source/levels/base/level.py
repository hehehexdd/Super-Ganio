from source.buttons.base.button import *
from source.widgets.base.widget import *
from source.entities.base.entity import *


class Level:
    def __init__(self, instance: object):
        self.drawables = {}
        self.surfaces = []
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
        for drawable in self.drawables:
            renderer.blit(drawable, self.drawables.get(drawable))
        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def check_collides_any(self, rect: tuple):
        if self.drawables:
            for drawable in self.drawables:
                temp = drawable.get_rect(bottomleft=self.drawables[drawable])
                #print(self.drawables[drawable])
                if temp.colliderect(rect):
                    return True
        return False

    def set_widget(self, widget: Widget):
        self.previous_widget = self.current_widget
        self.current_widget = widget

    def remove_widget(self):
        self.current_widget = None

