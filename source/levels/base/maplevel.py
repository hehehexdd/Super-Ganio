from source.levels.base.level import *
from source.entities.camera import *
from source.entities.player import *


class MapLevel(Level):
    def __init__(self, instance):
        super().__init__(instance)
        self.map = None

    def display_assets(self, renderer):
        if self.map:
            surface = self.map.make_map(self.player.camera.offset.x, self.player.camera.offset.y)
            renderer.blit(surface, surface.get_rect(bottomleft=(0 - self.player.camera.offset.x, self.game_instance.window.get_window_size()[1] - self.player.camera.offset.y)))#(0 - self.player.camera.offset.x, 0 - self.player.camera.offset.y))
        for entity in self.entities:
            entity.draw(renderer, self.player.camera)
        if self.player is not None:
            self.player.draw(renderer, None)
        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def post_handle_events(self, event: pygame.event.Event):
        if self.player is not None:
            self.player.handle_events(event)
