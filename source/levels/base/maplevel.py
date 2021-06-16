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
        self.map_last_pos[0] = self.surface.get_rect(bottomleft=(0, self.game_instance.renderer.get_rect().height)).topleft[0]
        self.map_last_pos[1] = self.surface.get_rect(bottomleft=(0, self.game_instance.renderer.get_rect().height)).topleft[1] - 100
        self.surface_offset[0] = self.surface.get_rect().topleft[0] - self.map_last_pos[0]
        self.surface_offset[1] = self.surface.get_rect().topleft[1] - self.map_last_pos[1]

    def display_assets(self, renderer):
        if self.map:
            if self.player:
                self.player.apply_camera_movement(self.map_last_pos, self.surfaces)
            #surface_rect = self.surface.get_rect(bottomleft=self.map_last_pos)
            renderer.blit(self.surface, self.map_last_pos)
            for surface in self.surfaces:
                renderer.blit(surface, self.surfaces[surface])
        for entity in self.entities:
            entity.draw(renderer)
        if self.player is not None:
            self.player.draw(renderer)
        if self.current_widget is not None:
            self.current_widget.draw(self.game_instance.renderer)

    def post_handle_events(self, event: pygame.event.Event):
        if self.player is not None:
            self.player.handle_events(event)
