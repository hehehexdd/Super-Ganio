from source.base.map import Map
from source.levels.base.level import *
from source.entities.camera import *
from source.entities.player import *


class MapLevel(Level):
    def __init__(self, instance):
        super().__init__(instance)
        self.map = None
        self.surface = None
        self.map_last_pos = [0, 0]

    def create_map(self, filename):
        self.map = Map(filename, self)
        self.surface = self.map.make_map()
        self.map_last_pos[0] = self.surface.get_rect(bottomleft=(0, self.game_instance.renderer.get_rect().height)).bottomleft[0]
        self.map_last_pos[1] = self.surface.get_rect(bottomleft=(0, self.game_instance.renderer.get_rect().height)).bottomleft[1] - 50

    def display_assets(self, renderer):
        if self.map:
            if self.player:
                self.player.apply_camera_movement(self.map_last_pos, self.drawables)
            surface_rect = self.surface.get_rect(bottomleft=self.map_last_pos)
            self.surface_offset = surface_rect.bottomleft
            renderer.blit(self.surface, surface_rect)
        for entity in self.entities:
            entity.draw(renderer)
        if self.player is not None:
            self.player.draw(renderer)
        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def post_handle_events(self, event: pygame.event.Event):
        if self.player is not None:
            self.player.handle_events(event)
