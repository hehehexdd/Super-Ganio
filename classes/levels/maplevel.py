from classes.levels.base.level import *
from classes.entities.camera import *
from classes.entities.player import *


class MapLevel(Level):
    def __init__(self, instance):
        super().__init__(instance)
        self.map = None

    def display_assets(self, renderer):
        if self.map:
            renderer.blit(self.map.make_map(), (0 - self.player.camera.offset.x, 0 - self.player.camera.offset.y))
        for entity in self.entities:
            entity.draw(renderer, self.player.camera)
        if self.player is not None:
            self.player.draw(renderer, None)
        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def post_handle_events(self, event: pygame.event.Event):
        if self.player is not None:
            self.player.handle_events(event)